<template>
  <div class="receita-container">
    <div class="card">
      <h1>📈 Receita</h1>
      <p>Esta funcionalidade está em desenvolvimento.</p>
      <p class="info">
        Em breve você poderá enviar a sua receita e o sistema irá informar os melhores locais para compra e te dar dicas.
      </p>
    </div>
  </div>
</template>

<script setup>
// Nenhuma lógica necessária por enquanto
</script>

<style scoped>
.receita-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  background: #f7f7f9;
  color: #333;
  font-family: "Segoe UI", Roboto, sans-serif;
}

.card {
  background: #fff;
  padding: 40px 60px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 500px;
}

.card h1 {
  font-size: 1.8rem;
  margin-bottom: 10px;
  color: #222;
}

.card p {
  font-size: 1rem;
  margin: 6px 0;
}

.info {
  color: #777;
  font-size: 0.95rem;
  margin-top: 10px;
}
</style>
