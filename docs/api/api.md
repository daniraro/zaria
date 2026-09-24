# API Documentation

## Endpoints

### Students

#### POST /students
Cadastra um novo aluno.

**Body:**
```json
{
  "name": "Ana Silva",
  "email": "ana@example.com"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Ana Silva",
  "email": "ana@example.com",
  "created_at": "2026-09-24T15:00:00",
  "updated_at": null
}
```

#### GET /students
Lista todos os alunos.

#### GET /students/{id}
Busca um aluno específico.

### Questions

#### POST /questions
Cadastra uma nova questão.

**Body:**
```json
{
  "text": "Qual a capital do Brasil?",
  "subject": "Geografia",
  "difficulty": "fácil"
}
```

#### GET /questions
Lista todas as questões.

#### GET /questions/{id}
Busca uma questão específica.

### Assessments

#### POST /assessments
Registra uma nova avaliação.

**Body:**
```json
{
  "student_id": 1,
  "question_id": 5
}
```

#### GET /assessments
Lista todas as avaliações.

### Answers

#### POST /answers
Registra uma resposta.

**Body:**
```json
{
  "assessment_id": 1,
  "text": "Brasília",
  "is_correct": true
}
```

#### GET /answers
Lista todas as respostas.
