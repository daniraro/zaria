# Requisitos do Projeto Zaria

## Requisitos Funcionais

### RF01 - Cadastro de Estudantes
- O sistema deve permitir cadastro de novos estudantes
- O sistema deve validar email único

### RF02 - Realizar Diagnóstico
- O sistema deve permitir que estudantes realizem avaliações diagnósticas
- O sistema deve registrar respostas e calcular acertos

### RF03 - Visualizar Desempenho
- O sistema deve exibir dashboard com métricas de desempenho
- O sistema deve mostrar evolução ao longo do tempo

### RF04 - Gerar Recomendações
- O sistema deve identificar áreas fracas do estudante
- O sistema deve sugerir tópicos para estudo

## Requisitos Não Funcionais

### RNF01 - Performance
- API deve responder em até 500ms
- Dashboard deve carregar em até 2 segundos

### RNF02 - Segurança
- Senhas devem ser hasheadas com bcrypt
- API deve usar autenticação JWT

### RNF03 - Escalabilidade
- Sistema deve suportar até 1000 usuários simultâneos
