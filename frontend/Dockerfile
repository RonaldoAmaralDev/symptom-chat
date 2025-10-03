FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 5173

# Executa o Vite e abre o navegador automaticamente
CMD sh -c "npm run dev -- --host & sleep 5 && xdg-open http://localhost:5173 || true && wait"
