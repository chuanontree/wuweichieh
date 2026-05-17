// SWILE GUIDE — Cloudflare Worker proxy for Groq API
//
// 部署步驟：
// 1. 前往 https://dash.cloudflare.com → Workers & Pages → Create
// 2. 貼上此檔案內容並部署
// 3. 在 Worker 設定 → Variables → Secrets 新增：
//    GROQ_API_KEY = 你的 Groq API key（https://console.groq.com）
// 4. 把 Worker URL 填入 index.html 的 WWCAI_PROXY

const ALLOWED_ORIGIN = 'https://chuanontree.github.io';

const CORS = {
  'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: CORS });
    }

    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    const origin = request.headers.get('Origin') || '';
    if (origin !== ALLOWED_ORIGIN) {
      return new Response('Forbidden', { status: 403 });
    }

    try {
      const body = await request.json();
      const upstream = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${env.GROQ_API_KEY}`,
        },
        body: JSON.stringify(body),
      });

      const data = await upstream.json();
      return new Response(JSON.stringify(data), {
        status: upstream.status,
        headers: { 'Content-Type': 'application/json', ...CORS },
      });
    } catch (e) {
      return new Response(JSON.stringify({ error: { message: e.message } }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...CORS },
      });
    }
  },
};
