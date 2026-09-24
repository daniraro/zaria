# Zaria

Plataforma de diagnóstico educacional para acompanhamento de desempenho de alunos.

## Estrutura do Projeto

```
zaria/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   ├── core/
│   │   │   ├── security.py
│   │   │   └── auth.py
│   │   ├── database/
│   │   │   ├── connection.py
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── student.py
│   │   │   ├── question.py
│   │   │   ├── assessment.py
│   │   │   ├── answer.py
│   │   │   └── ...
│   │   ├── schemas/
│   │   │   ├── student.py
│   │   │   ├── question.py
│   │   │   ├── assessment.py
│   │   │   ├── answer.py
│   │   │   └── ...
│   │   ├── routes/
│   │   │   ├── students.py
│   │   │   ├── questions.py
│   │   │   ├── assessments.py
│   │   │   ├── answers.py
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── performance.py
│   │   │   ├── analytics.py
│   │   │   ├── diagnosis.py
│   │   │   └── ...
│   │   └── repositories/
│   │       ├── student.py
│   │       ├── question.py
│   │       └── ...
│   ├── tests/
│   │   ├── test_students.py
│   │   ├── test_questions.py
│   │   └── ...
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── diagnostico.py
│   │   ├── desempenho.py
│   │   └── perfil.py
│   ├── components/
│   │   ├── cards.py
│   │   ├── charts.py
│   │   └── tables.py
│   ├── services/
│   │   └── api.py
│   └── assets/
│       ├── images/
│       └── styles/
│
├── database/
│   ├── seeds/
│   └── README.md
│
├── docs/
│   ├── produto/
│   │   └── mvp.md
│   ├── requisitos/
│   │   └── requisitos.md
│   ├── arquitetura/
│   │   └── arquitetura.md
│   ├── banco/
│   │   └── modelo-dados.md
│   └── api/
│       └── api.md
│
├── scripts/
│   ├── seed.py
│   ├── import_questions.py
│   └── backup.py
│
├── docker/
│   ├── backend/
│   │   └── Dockerfile
│   └── frontend/
│       └── Dockerfile
│
├── tests/
│   └── integration/
│
├── .gitignore
├── .env.example
├── docker-compose.yml
└── README.md
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
   python -m venv .venv
   source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
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
