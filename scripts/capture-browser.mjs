import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';

const base = process.env.APP_URL || 'http://localhost:3000';
await mkdir('docs/screenshots', { recursive: true });
await mkdir('docs/evidence', { recursive: true });
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1080 } });
const page = await context.newPage();
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
const created = [];
try {
  const health = await context.request.get(`${base}/api/health`);
  assert.equal(health.status(), 200, 'The API must be live before taking application evidence.');
  await page.goto(base);
  await page.getByText('Notebook connected · saved to database').waitFor();
  for (const expression of ['log(1000)', 'sin(pi / 2)', 'sqrt(144) + 2^3']) {
    await page.locator('#expression').fill(expression);
    const response = page.waitForResponse((res) => res.url().endsWith('/api/calculations') && res.request().method() === 'POST');
    await page.locator('#calculate').click();
    const saved = await response;
    assert.equal(saved.status(), 201);
    created.push((await saved.json()).id);
    await page.getByText('Calculated & saved to your notebook.').waitFor();
    await page.waitForFunction(() => !document.querySelector('#calculate').disabled);
  }
  assert.equal(await page.locator('#result').textContent(), '20');
  await page.screenshot({ path: 'docs/screenshots/01-application-desktop.png', fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: 'docs/screenshots/02-application-mobile.png', fullPage: true });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'Mobile UI overflows');
  await page.setViewportSize({ width: 1440, height: 1080 });
  await page.locator('#mode-deg').click();
  await page.locator('#expression').fill('sin(30)');
  const degreeResponse = page.waitForResponse((res) => res.url().endsWith('/api/calculations') && res.request().method() === 'POST');
  await page.locator('#calculate').click();
  const degreeRow = await (await degreeResponse).json();
  created.push(degreeRow.id);
  await page.getByText('Calculated & saved to your notebook.').waitFor();
  await page.waitForFunction(() => !document.querySelector('#calculate').disabled);
  assert.equal(await page.locator('#result').textContent(), '0.5');
  await page.screenshot({ path: 'docs/screenshots/03-degrees.png', fullPage: true });
  await page.locator('#expression').fill('1/0');
  await page.locator('#calculate').click();
  await page.locator('#message.error').waitFor();
  await page.screenshot({ path: 'docs/screenshots/04-domain-error.png', fullPage: true });
  const id = created[0];
  const updated = await context.request.put(`${base}/api/calculations/${id}`, { data: { label: 'Browser smoke test' } });
  assert.equal(updated.status(), 200);
  assert.equal((await updated.json()).label, 'Browser smoke test');
  assert.deepEqual(errors, []);
  await writeFile('docs/evidence/browser-smoke.json', JSON.stringify({
    capturedAt: new Date().toISOString(), base, checks: ['live API', 'scientific result', 'degree mode', 'mobile width', 'domain error', 'label update', 'no JS errors'],
    screenshotsUseRealBackend: true,
  }, null, 2));
  if (process.env.PROMETHEUS_URL) {
    const url = process.env.PROMETHEUS_URL;
    const data = await (await context.request.get(`${url}/api/v1/targets`)).json();
    const targets = data.data.activeTargets.filter((t) => t.labels.job === 'orbit-api');
    assert.ok(targets.length >= 2 && targets.every((t) => t.health === 'up'), 'Both API replicas must be UP');
    await page.goto(`${url}/targets`);
    await page.getByText('orbit-api', { exact: false }).first().waitFor();
    await page.screenshot({ path: 'docs/screenshots/15-prometheus-targets.png', fullPage: true });
  }
  if (process.env.GRAFANA_URL && process.env.GRAFANA_PASSWORD) {
    const url = process.env.GRAFANA_URL;
    const authorization = `Basic ${Buffer.from(`admin:${process.env.GRAFANA_PASSWORD}`).toString('base64')}`;
    const metrics = await context.request.post(`${url}/api/ds/query`, {
      headers: { Authorization: authorization },
      data: { from: String(Date.now() - 300000), to: String(Date.now()), queries: [{
        refId: 'A', datasource: { type: 'prometheus', uid: 'prometheus' },
        expr: 'sum(orbit_http_requests_total{job="orbit-api"})', instant: true,
        intervalMs: 10000, maxDataPoints: 100,
      }] },
    });
    assert.equal(metrics.status(), 200, 'Grafana datasource query failed');
    const frames = (await metrics.json()).results?.A?.frames || [];
    assert.ok(frames.some((frame) => frame.schema?.fields?.some((field, index) =>
      field.type === 'number' && frame.data?.values?.[index]?.some((value) =>
        typeof value === 'number' && value > 0))), 'Grafana must have real metric values before capture');
    await page.goto(`${url}/login`);
    await page.getByRole('textbox', { name: /email or username/i }).fill('admin');
    await page.locator('input[type="password"]').fill(process.env.GRAFANA_PASSWORD);
    await page.getByRole('button', { name: /log in/i }).click();
    await page.waitForURL((address) => !address.pathname.includes('/login'));
    await page.goto(`${url}/d/orbit-api?from=now-15m&to=now&kiosk`);
    await page.getByText('HTTP requests / second', { exact: true }).waitFor();
    await page.waitForTimeout(12000);
    await page.screenshot({ path: 'docs/screenshots/16-grafana-dashboard.png', fullPage: true });
  }
  console.log('Browser smoke tests passed; screenshots captured from the live application.');
} finally {
  // Remove only records created by this tool; preserve the user's notebook.
  for (const id of created) await context.request.delete(`${base}/api/calculations/${id}`);
  await browser.close();
}
