# Modelo de Dados

## Entidades Principais

### Student (Estudante)
- `id`: Integer (PK)
- `name`: String
- `email`: String (unique)
- `created_at`: DateTime
- `updated_at`: DateTime

### Question (Questão)
- `id`: Integer (PK)
- `text`: Text
- `subject`: String
- `grade_level`: Integer

### Assessment (Avaliação)
- `id`: Integer (PK)
- `student_id`: Integer (FK -> Student)
- `title`: String
- `completed_at`: DateTime

### Answer (Resposta)
- `id`: Integer (PK)
- `question_id`: Integer (FK -> Question)
- `assessment_id`: Integer (FK -> Assessment)
- `selected_option`: String
- `is_correct`: Boolean

## Relacionamentos

- Student (1) ── (N) Assessment
- Assessment (1) ── (N) Answer
- Question (1) ── (N) Answer

## Índices

- `students.email`: unique index
- `questions.subject`: index
- `assessments.student_id`: index
- `answers.assessment_id`: index
