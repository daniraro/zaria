# Database

Este diretório contém scripts e seeds para o banco de dados do projeto Zaria.

## Estrutura

- `seeds/`: Scripts SQL para popular o banco com dados iniciais
- `migrations/`: (futuro) Scripts de migração do schema

## Uso

Execute os seeds na ordem correta:

```bash
psql -d zaria -f seeds/seed_students.sql
psql -d zaria -f seeds/seed_questions.sql
```
