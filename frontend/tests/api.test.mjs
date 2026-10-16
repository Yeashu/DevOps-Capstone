import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatNumber, request } from '../src/api.js';

test('results show useful precision and reject nonfinite values', () => {
  assert.equal(formatNumber(0.1 + 0.2), '0.3');
  assert.equal(formatNumber(Infinity), '—');
  assert.equal(formatNumber(-0), '0');
});
test('API returns actionable backend errors', async () => {
  globalThis.fetch = async () => new Response(JSON.stringify({ detail: 'Undefined calculation' }), { status: 422 });
  await assert.rejects(request('/evaluate'), /Undefined calculation/);
});
test('delete handles empty 204 response', async () => {
  globalThis.fetch = async () => new Response(null, { status: 204 });
  assert.equal(await request('/calculations/1', { method: 'DELETE' }), null);
});
test('proxy HTML errors produce a readable fallback', async () => {
  globalThis.fetch = async () => new Response('<html>502</html>', { status: 502 });
  await assert.rejects(request('/calculations'), /Something went wrong/);
});
