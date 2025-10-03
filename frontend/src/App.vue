<template>
  <div class="layout">
    <header class="nav">
      <div class="container">
        <h1 class="brand">💊 Symptom Chat</h1>
        <nav class="links">
          <router-link to="/" exact>Chat</router-link>
          <router-link to="/dashboard">Dashboard</router-link>
          <router-link to="/receita">Receita Médica</router-link>
        </nav>
      </div>
    </header>

    <main class="main container">
      <router-view />
    </main>

    <footer class="footer">
      © 2025 Symptom Chat — Projeto Educacional
    </footer>
  </div>
</template>

<script setup></script>

<style>
:root{
  --bg: #f7f7f8; --text: #0f172a; --muted: #64748b;
  --brand: #16a34a; --brand-700: #15803d;
  --card: #fff; --shadow: 0 8px 24px rgba(0,0,0,.06);
  --radius: 16px; --container: 1100px;
}
*{box-sizing:border-box} html,body,#app{height:100%;margin:0}
body{background:var(--bg);color:var(--text);font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial}
a{text-decoration:none;color:inherit}
.layout{min-height:100vh;display:flex;flex-direction:column}
.nav{background:linear-gradient(180deg,var(--brand),var(--brand-700));color:#fff;position:sticky;top:0;z-index:10;box-shadow:var(--shadow)}
.container{max-width:var(--container);margin:0 auto;padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{font-size:18px;font-weight:800;letter-spacing:.2px}
.links{display:flex;gap:18px;align-items:center}
.links a{color:#fff;opacity:.95;padding:8px 12px;border-radius:10px;transition:all .16s ease;font-weight:600}
.links a:hover{background:rgba(255,255,255,.12);opacity:1;transform:translateY(-1px)}
.links .router-link-active,.links .router-link-exact-active{background:rgba(255,255,255,.22);box-shadow:inset 0 0 0 1px rgba(255,255,255,.28)}
.main{flex:1;max-width:var(--container);width:100%;margin:24px auto;padding:0 20px 24px}
.footer{text-align:center;color:var(--muted);padding:12px 20px;border-top:1px solid rgba(2,6,23,.06);background:#fff}
@media (max-width:680px){.container{flex-wrap:wrap}.links{width:100%;justify-content:space-between}.brand{font-size:16px}}
</style>
