export async function request(path, options = {}) {
  const response = await fetch(`/api${path}`, {
    ...options,
    headers: { 'Content-Type': 'application/json', ...options.headers },
    signal: AbortSignal.timeout(10000),
  });
  if (!response.ok) {
    let detail = 'Something went wrong. Please try again.';
    try {
      const body = await response.json();
      detail = typeof body.detail === 'string' ? body.detail : 'Check your expression and try again.';
    } catch { /* Preserve readable fallback when a proxy returns HTML. */ }
    throw new Error(detail);
  }
  return response.status === 204 ? null : response.json();
}

export function formatNumber(value) {
  if (!Number.isFinite(value)) return '—';
  return Number(value.toPrecision(12)).toString();
}
