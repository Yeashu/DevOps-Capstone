import { cp, mkdir, rm, readFile, writeFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';

execFileSync(process.execPath, ['--check', 'src/app.js'], { stdio: 'inherit' });
execFileSync(process.execPath, ['--check', 'src/api.js'], { stdio: 'inherit' });
await rm('dist', { recursive: true, force: true });
await mkdir('dist/assets', { recursive: true });
for (const file of ['app.js', 'api.js', 'styles.css']) {
  await cp(`src/${file}`, `dist/assets/${file}`);
}
const source = await readFile('index.html', 'utf8');
const hash = createHash('sha256').update(await readFile('src/app.js')).digest('hex').slice(0, 12);
await writeFile('dist/index.html', source.replaceAll('./src/', './assets/'));
await writeFile('dist/build.json', JSON.stringify({ version: '1.0.0', bundle: hash }));
console.log(`Orbit production build complete · ${hash} · no external browser dependencies`);
