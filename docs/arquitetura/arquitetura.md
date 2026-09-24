# Arquitetura do Sistema Zaria

## Visão Geral

O Zaria utiliza uma arquitetura baseada em microsserviços com separação clara entre backend e frontend.

## Componentes

### Backend
- **Framework**: FastAPI (Python)
- **Banco de Dados**: PostgreSQL com SQLAlchemy Async
- **Autenticação**: JWT
- **Estrutura**: MVC (Models, Routes, Services, Repositories)

### Frontend
- **Framework**: Streamlit (Python)
- **Comunicação**: API REST
- **Componentes**: Cards, Charts, Tables

### Banco de Dados
- **Tabelas Principais**: students, questions, assessments, answers
- **ORM**: SQLAlchemy

## Fluxo de Dados

1. Frontend faz requisições para API do Backend
2. Backend processa e interage com Banco de Dados
3. Respostas são retornadas como JSON
4. Frontend renderiza dados para o usuário

## Tecnologias

- Python 3.11+
- FastAPI
- SQLAlchemy Async
- Streamlit
- PostgreSQL
