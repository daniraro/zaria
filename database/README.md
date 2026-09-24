# Database

Este diretório contém scripts e seeds para o banco de dados do projeto Zaria.

## Estrutura

- `seeds/`: Scripts SQL para popular o banco com dados iniciais

## Uso

Execute os seeds após criar as tabelas:

```bash
psql -U postgres -d zaria -f seeds/initial_data.sql
```
