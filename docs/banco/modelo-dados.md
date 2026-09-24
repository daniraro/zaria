# Modelo de Dados

## Entidades

### students
- id (PK)
- name
- email (unique)
- created_at
- updated_at

### questions
- id (PK)
- text
- subject
- difficulty

### assessments
- id (PK)
- student_id (FK → students.id)
- question_id (FK → questions.id)
- answered_at

### answers
- id (PK)
- assessment_id (FK → assessments.id)
- text
- is_correct

## Diagrama ER

```
students 1──N assessments N──1 questions
                  │
                  1──N answers
```
