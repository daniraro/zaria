-- Seed inicial para o banco de dados Zaria

-- Inserir alunos de exemplo
INSERT INTO students (name, email) VALUES
    ('Ana Silva', 'ana@example.com'),
    ('Bruno Santos', 'bruno@example.com'),
    ('Carla Oliveira', 'carla@example.com');

-- Inserir questões de exemplo
INSERT INTO questions (text, subject, difficulty) VALUES
    ('Qual a capital do Brasil?', 'Geografia', 'fácil'),
    ('Quanto é 2 + 2?', 'Matemática', 'fácil'),
    ('Quem descobriu o Brasil?', 'História', 'médio'),
    ('Qual a fórmula da água?', 'Química', 'fácil'),
    ('Qual o planeta mais próximo do Sol?', 'Astronomia', 'médio');
