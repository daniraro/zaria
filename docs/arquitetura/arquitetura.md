# Arquitetura do Sistema Zaria

## Visão Geral

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Frontend   │────▶│   Backend    │────▶│  Database   │
│  Streamlit  │     │   FastAPI    │     │ PostgreSQL  │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Componentes

### Frontend (Streamlit)
- Interface web para usuários
- Consome API do backend
- Páginas: Dashboard, Diagnóstico, Desempenho, Perfil

### Backend (FastAPI)
- API REST
- Autenticação JWT (futuro)
- Regras de negócio
- Repositórios de dados

### Database (PostgreSQL)
- Armazenamento de alunos, questões, avaliações e respostas
- Migrations e seeds

## Estrutura de Diretórios

Ver README.md na raiz do projeto.
