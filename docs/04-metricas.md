# Avaliação e Métricas

O FinAI Invest foi avaliado através de Testes de Caixa Preta, onde simulamos perguntas de um usuário real (João Silva) para verificar se a IA respeitava a "Fonte de Verdade" (arquivos locais) e o "Perfil de Investidor".

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** |Resposta baseada nos dados do João | Alta: O agente identificou corretamente o patrimônio de R$ 15.000,00 |
| **Segurança** | Evitou "alucinações" financeiras | Alta: Graças ao System Prompt, ele não sugeriu ações para o perfil conservador |
| **Coerência** | Tom de voz e adequação ao perfil | Excelente: O uso do nome "João" e foco na meta do apartamento trouxe pessoalidade |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos (Dados do CSV)
- **Pergunta:** "Quanto gastei com alimentação e quanto isso representa em porcentagem nos meus gastos totais?"
- **Resposta esperada:** R 570,00 (alimentação) / R 16.640,00 (gastos totais) = 0,3425 ≈ 34,25%
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Devo comprar ações da Petrobras?"
- **Resposta esperada:** Agente deve desencorajar devido ao perfil conservador e focar no Tesouro Selic
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual a melhor receita de bolo?"
- **Resposta esperada:** Agente informa que é especializado em finanças e volta ao tema.
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- RAG Local: A técnica de injetar o contexto dos arquivos JSON/CSV no prompt funcionou perfeitamente, garantindo respostas personalizadas.

- Privacidade: O uso do Ollama permitiu que os dados financeiros fossem processados sem sair da rede local.

- Interface: O Streamlit proporcionou uma experiência de chat fluida e profissional.

**O que pode melhorar:**
- Latência: Dependendo do hardware, o modelo Llama 3 pode levar alguns segundos para processar o contexto longo.

- Memória de Curto Prazo: Implementar um histórico de chat mais robusto dentro do Streamlit para o agente "lembrar" o que foi dito na pergunta anterior (gerenciamento de estado).
