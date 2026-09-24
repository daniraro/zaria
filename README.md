# Zaria

Plataforma de diagnóstico educacional para acompanhamento de desempenho de alunos.

## Estrutura do Projeto

```
zaria/
├── backend/          # API FastAPI
│   ├── app/          # Código da aplicação
│   ├── tests/        # Testes do backend
│   └── requirements.txt
├── frontend/         # Interface Streamlit
│   ├── pages/        # Páginas da aplicação
│   ├── components/   # Componentes reutilizáveis
│   ├── services/     # Serviços de API
│   └── requirements.txt
├── database/         # Scripts e seeds do banco
├── docs/             # Documentação do projeto
├── scripts/          # Scripts utilitários
├── docker/           # Dockerfiles
└── tests/            # Testes de integração
```

## Tecnologias

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** Streamlit
- **Infra:** Docker, Docker Compose

## Como Rodar

### Com Docker

```bash
docker-compose up --build
```

Acesse:
- Frontend: http://localhost:8501
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Sem Docker

1. **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. **Frontend:**
   ```bash
   cd frontend
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Documentação

- [MVP](docs/produto/mvp.md)
- [Requisitos](docs/requisitos/requisitos.md)
- [Arquitetura](docs/arquitetura/arquitetura.md)
- [Modelo de Dados](docs/banco/modelo-dados.md)
- [API](docs/api/api.md)

## Próximos Passos

- [ ] Implementar autenticação
- [ ] Adicionar gráficos de desempenho
- [ ] Criar sistema de recomendação de questões
- [ ] Importação em massa de questões
