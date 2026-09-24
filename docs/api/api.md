# API Documentation

## Base URL

```
http://localhost:8000
```

## Endpoints

### Students

#### GET /students/
Lista todos os estudantes.

**Resposta**: `200 OK`
```json
[{"id": 1, "name": "Ana Silva", "email": "ana@example.com"}]
```

#### POST /students/
Cria um novo estudante.

**Requisição**:
```json
{"name": "Bruno Santos", "email": "bruno@example.com"}
```

**Resposta**: `200 OK`
```json
{"id": 2, "name": "Bruno Santos", "email": "bruno@example.com"}
```

### Questions

#### GET /questions/
Lista todas as questões.

#### POST /questions/
Cria uma nova questão.

### Assessments

#### GET /assessments/
Lista todas as avaliações.

#### POST /assessments/
Cria uma nova avaliação.

### Answers

#### GET /answers/
Lista todas as respostas.

#### POST /answers/
Cria uma nova resposta.

## Autenticação

Endpoints protegidos requerem header:
```
Authorization: Bearer <token>
```
