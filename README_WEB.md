# AppFilmes — Web Frontend (Netflix style)

## Como usar

1. Instale dependências:
   ```bash
   npm install
   ```
2. Configure a API: por padrão o frontend usa `http://localhost:4000` (variável REACT_APP_API_URL não é usada em Vite; altere `src/api.js` se necessário).
3. Rode em desenvolvimento:
   ```bash
   npm run dev
   ```
4. Backend: certifique-se de que o backend (Express) esteja rodando em `http://localhost:4000` com os endpoints:
   - `GET /works/popular?type=movie`
   - `GET /works/popular?type=tv`
   - `GET /works/search?q=...`
   - `GET /works/tmdb/:kind/:id`
   - `GET /works/:id/predictions` (opcional)

OBS: Para popular com TMDB é necessário `TMDB_API_KEY` no backend.

## Deploy
Você pode hospedar o build em qualquer serviço estático (Vercel, Netlify, Surge) ou servir via Node static server.

