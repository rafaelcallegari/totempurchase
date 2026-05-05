# Totem Purchase — CLAUDE.md

## 📊 Status do Projeto

**Última atualização:** BLOCO 1 ✅ Concluído

### Roadmap de Blocos

| Fase | Bloco | Status | Descrição |
|------|-------|--------|-----------|
| 1 | **BLOCO 1 — Infraestrutura & DB** | ✅ | SQLAlchemy + SQLite, 6 tabelas, seed com 8 produtos |
| 2 | **BLOCO 2 — Carrinho por Sessão** | ⏳ | Sessions multi-usuário, checkout com CPF opcional |
| 3 | **BLOCO 3 — Recomendações & Pagamento** | ⏳ | Upsell/downsell por categoria, simulação de pagamento |
| 4 | **BLOCO 4 — Frontend Integrado** | ⏳ | React conectado ao backend, fluxo completo Menu → Carrinho → Pagamento |
| 5 | **BLOCO 5 — Documentação Final** | ⏳ | README, instruções, cleanup |

---

## Visão Geral
Sistema de autoatendimento (totem) para pedidos em restaurantes/lanchonetes.
Stack: Python FastAPI (backend) + React + TypeScript + Tailwind (frontend).

## Estrutura do Projeto
```
totempurchase/
├── backend/                          # FastAPI API REST
│   ├── main.py                       # Entry point
│   ├── config.py                     # Configurações (DATABASE_URL, env)
│   ├── requirements.txt              # Dependências Python
│   ├── test.db                       # SQLite (desenvolvimento)
│   └── app/
│       ├── database_config.py        # Engine, SessionLocal, get_db()
│       ├── database/
│       │   ├── __init__.py
│       │   └── memory.py             # [DESCONTINUADO - para remover]
│       ├── models/
│       │   ├── produto.py            # Pydantic schemas (request/response)
│       │   └── database.py           # SQLAlchemy models (6 tabelas)
│       ├── routes/
│       │   ├── produtos.py           # ✅ GET /produtos, GET /produtos/{id}
│       │   ├── carrinho.py           # ⏳ Placeholder para BLOCO 2
│       │   └── pedidos.py            # ⏳ Placeholder para BLOCO 2
│       └── services/                 # [CRIADO NA PRÓXIMA FASE]
├── scripts/
│   └── seed.py                       # Popular DB com produtos iniciais
├── .env.example                      # Template de variáveis
├── config.py                         # Settings globais
└── frontend/                         # React + Vite + Tailwind
    └── src/
        ├── pages/                    # MenuPage | CartPage | PaymentPage
        ├── components/               # ProductCard | CartItem
        ├── store/cartStore.ts        # Estado global (Zustand)
        ├── services/api.ts           # Chamadas HTTP (Axios → /api proxy)
        └── types/index.ts            # Interfaces TypeScript
```

---

## 🗄️ Database - SQLAlchemy Models (BLOCO 1 ✅)

### Tabelas Criadas

1. **produtos** — Catálogo de produtos
   ```
   id (PK) | nome | preco | categoria | descricao | criado_em
   ```

2. **sessions** — Sessão de cliente
   ```
   id (PK, UUID) | criada_em | atualizada_em
   ```

3. **cart_items** — Itens no carrinho
   ```
   id (PK) | session_id (FK) | produto_id (FK) | quantidade | criado_em
   ```

4. **orders** — Pedidos finalizados
   ```
   id (PK) | session_id (FK) | cpf | total | status | criado_em
   ```

5. **order_items** — Itens do pedido
   ```
   id (PK) | pedido_id (FK) | produto_id (FK) | quantidade | preco_unitario | subtotal
   ```

6. **analytics_events** — Rastreamento de eventos
   ```
   id (PK) | tipo_evento | session_id (FK) | produto_id (FK) | pedido_id (FK) | dados_adicionais (JSON) | criado_em
   ```

---

## Como Executar

### Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
python -m scripts.seed              # Popular banco com produtos iniciais
python -m uvicorn main:app --reload --port 8000
```

**API disponível em:** `http://localhost:8000`  
**Swagger UI:** `http://localhost:8000/docs`  
**ReDoc:** `http://localhost:8000/redoc`

### Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev     # http://localhost:3000
```

---

## 🚀 APIs Disponíveis (BLOCO 1 ✅)

| Método | Endpoint | Status | Descrição |
|--------|----------|--------|-----------|
| GET | /produtos | ✅ | Listar todos os produtos |
| GET | /produtos/{id} | ✅ | Obter produto específico |
| POST | /produtos | ✅ | Criar novo produto |
| ⏳ | /sessions | ⏳ | BLOCO 2 — Criar sessão |
| ⏳ | /sessions/{id}/cart | ⏳ | BLOCO 2 — Listar carrinho |
| ⏳ | /sessions/{id}/cart/items | ⏳ | BLOCO 2 — Adicionar item |
| ⏳ | /sessions/{id}/checkout | ⏳ | BLOCO 2 — Finalizar pedido |
| ⏳ | /recommendations | ⏳ | BLOCO 3 — Recomendações |
| ⏳ | /payments/simulate | ⏳ | BLOCO 3 — Pagamento simulado |

---

## 📋 Convenções de Código

- **Backend:** snake_case, português para domínio, inglês para código
- **Frontend:** PascalCase componentes, camelCase funções/vars, TypeScript strict
- **Tailwind:** botões mínimo `min-h-[56px]`, texto mínimo `text-lg` (totem)
- **Commits:** Português imperativo — "feat(BLOCO-X):", "fix:", "refactor:"
- **Database:** Nomes descritivos, use relacionamentos (FK) ao invés de IDs soltos

---

## 🎯 Contexto de Design (Totem Físico)

- Tela touch vertical ~15", resolução 1080x1920 típica
- Usuário em pé, distância ~60-80cm da tela
- Fluxo máximo: Menu → Carrinho → Pagamento (3 telas)
- Cor primária: laranja `#f97316` (orange-500 Tailwind)
- Touch targets: mínimo 56px, ideal 80px+
- Sem hover states — é touch, não mouse
- Tempo alvo por pedido: 60-90 segundos

---

## 🧪 Teste Rápido do BLOCO 1 ✅

```bash
# Terminal 1 — Backend
cd backend && python -m uvicorn main:app --reload --port 8000

# Terminal 2 — Teste GET /produtos
curl http://localhost:8000/produtos

# Esperado:
# [
#   {"id": 1, "nome": "Hamburguer Clássico", "preco": 20.0, "categoria": "lanche", ...},
#   ...
# ]
```

---

## 🔄 Próximos Passos — BLOCO 2

**Carrinho por Sessão & Checkout**

1. Criar endpoint `POST /sessions` → retorna `session_id`
2. Criar rotas de carrinho com `session_id` no path:
   - `POST /sessions/{session_id}/cart/items` — adicionar produto com quantidade
   - `DELETE /sessions/{session_id}/cart/items/{product_id}` — remover
   - `GET /sessions/{session_id}/cart` — listar
   - `GET /sessions/{session_id}/cart/total` — total
3. Criar checkout:
   - `POST /sessions/{session_id}/checkout` — finalizar pedido (CPF opcional)
4. Atualizar frontend para usar sessions

**Estimado:** 2-2,5h

---

## 📌 Agentes Disponíveis

- `/ux` — Especialista em UI/UX para totens
- `/dev` — Desenvolvedor full-stack FastAPI + React

---

## 📝 Git Branches

- `main` — Produção (protegida)
- `develop` — Integração (base para features)
- `feature/arquitetura-backend` — BLOCO 1, 2, 3... (atual)
