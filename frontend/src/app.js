import { request, formatNumber } from './api.js';

const $ = (selector) => document.querySelector(selector);
const input = $('#expression');
let mode = 'rad';
let lastResult = null;
let busy = false;
let historyBusy = false;

function message(text, error = false) {
  $('#message').textContent = text;
  $('#message').classList.toggle('error', error);
}

function invalidateResult() {
  lastResult = null;
  $('#result').textContent = '0';
  message('Ready when you are.');
}

function setMode(next) {
  mode = next;
  for (const item of ['rad', 'deg']) {
    $(`#mode-${item}`).classList.toggle('active', item === mode);
    $(`#mode-${item}`).setAttribute('aria-pressed', String(item === mode));
  }
  $('#display-mode').textContent = mode === 'rad' ? 'RADIANS' : 'DEGREES';
  invalidateResult();
}

function insert(text) {
  input.focus();
  input.setRangeText(text, input.selectionStart, input.selectionEnd, 'end');
  invalidateResult();
}

function element(tag, className, text) {
  const node = document.createElement(tag);
  node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function renderHistory(rows) {
  const container = $('#history');
  container.replaceChildren();
  $('#history-count').textContent = rows.length === 100 ? '100+' : String(rows.length);
  if (!rows.length) {
    const empty = element('div', 'empty-state');
    empty.append(element('span', '', '⌁'), element('h3', '', 'A fresh page.'),
      element('p', '', 'Your calculations will appear here. Try an example to get started.'));
    container.append(empty);
    return;
  }
  for (const row of rows) {
    const article = element('article', 'history-item');
    const meta = element('div', 'history-meta');
    meta.append(element('span', '', row.label || 'Calculation'), element('span', '', row.angle_mode.toUpperCase()));
    const reuse = element('button', 'history-expression', row.expression);
    reuse.title = 'Reuse this expression';
    reuse.addEventListener('click', () => {
      setMode(row.angle_mode);
      input.value = row.expression;
      input.focus();
    });
    const bottom = element('div', 'history-bottom');
    bottom.append(element('strong', '', `= ${formatNumber(row.result)}`));
    const actions = element('div', 'history-actions');
    const rename = element('button', '', 'Label');
    rename.setAttribute('aria-label', `Label calculation ${row.id}`);
    rename.addEventListener('click', async () => {
      const label = window.prompt('Give this calculation a label (up to 80 characters)', row.label);
      if (label === null) return;
      try {
        await request(`/calculations/${row.id}`, { method: 'PUT', body: JSON.stringify({ label }) });
        await loadHistory();
      } catch (error) { message(error.message, true); }
    });
    const remove = element('button', '', 'Delete');
    remove.setAttribute('aria-label', `Delete calculation ${row.id}`);
    remove.addEventListener('click', async () => {
      remove.disabled = true;
      try {
        await request(`/calculations/${row.id}`, { method: 'DELETE' });
        await loadHistory();
      } catch (error) { message(error.message, true); remove.disabled = false; }
    });
    actions.append(rename, remove);
    bottom.append(actions);
    article.append(meta, reuse, bottom);
    container.append(article);
  }
}

async function loadHistory() {
  if (historyBusy) return;
  historyBusy = true;
  $('#refresh').disabled = true;
  try {
    const rows = await request('/calculations?limit=100');
    renderHistory(rows);
    $('#status-dot').classList.add('online');
    $('#connection-status').textContent = 'Notebook connected · saved to database';
  } catch {
    $('#status-dot').classList.remove('online');
    $('#connection-status').textContent = 'Notebook offline · check the API connection';
  } finally {
    historyBusy = false;
    $('#refresh').disabled = false;
  }
}

async function evaluate() {
  if (busy) return;
  if (!input.value.trim()) { message('Enter an expression first.', true); input.focus(); return; }
  busy = true;
  const expression = input.value;
  const submittedMode = mode;
  $('#calculate').disabled = true;
  message('Calculating…');
  try {
    const row = await request('/calculations', {
      method: 'POST', body: JSON.stringify({ expression, angle_mode: submittedMode }),
    });
    if (input.value === expression && mode === submittedMode) {
      lastResult = row.result;
      $('#result').textContent = formatNumber(row.result);
      message('Calculated & saved to your notebook.');
    }
    await loadHistory();
  } catch (error) {
    lastResult = null;
    $('#result').textContent = '—';
    message(error.name === 'TypeError' ? 'Cannot reach the calculator API. Please try again.' : error.message, true);
  } finally {
    busy = false;
    $('#calculate').disabled = false;
  }
}

$('#mode-rad').addEventListener('click', () => setMode('rad'));
$('#mode-deg').addEventListener('click', () => setMode('deg'));
$('#calculate').addEventListener('click', evaluate);
$('#refresh').addEventListener('click', loadHistory);
$('#keypad').addEventListener('click', (event) => {
  const button = event.target.closest('[data-insert]');
  if (button) insert(button.dataset.insert);
});
$('#clear').addEventListener('click', () => { input.value = ''; invalidateResult(); input.focus(); });
$('#backspace').addEventListener('click', () => {
  const start = input.selectionStart, end = input.selectionEnd;
  input.focus();
  input.setRangeText('', start === end ? Math.max(0, start - 1) : start, end, 'end');
  invalidateResult();
});
input.addEventListener('input', invalidateResult);
input.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') { event.preventDefault(); evaluate(); }
  if (event.key === 'Escape') { input.value = ''; invalidateResult(); }
});
for (const button of document.querySelectorAll('[data-example]')) {
  button.addEventListener('click', () => {
    setMode('rad');
    input.value = button.dataset.example;
    input.focus();
  });
}
$('#copy-result').addEventListener('click', async () => {
  if (lastResult === null) return;
  try { await navigator.clipboard.writeText(String(lastResult)); message('Result copied.'); }
  catch { message('Copy is unavailable in this browser. Select the result instead.', true); }
});
$('#help-button').addEventListener('click', () => $('#guide').showModal());
$('#close-guide').addEventListener('click', () => $('#guide').close());
loadHistory();
