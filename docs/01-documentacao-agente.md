# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A paralisia de decisão e a falta de educação financeira. Muitos brasileiros possuem capital para investir, mas sentem-se inseguros diante da complexidade dos produtos financeiros ou não sabem como alinhar seus objetivos pessoais (aposentadoria, compra de imóvel, reserva de emergência) aos ativos disponíveis no mercado.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um Orientador de Investimentos Proativo. Ele utiliza o modelo GPT-4 para analisar o montante disponível, o horizonte de tempo e as preferências do cliente, cruzando esses dados com o seu perfil de investidor (suitability) para sugerir alocações diversificadas e educativas, explicando o "porquê" de cada sugestão.
Privacidade Total: Diferente de soluções baseadas em nuvem, o FinAI Invest utiliza processamento local via Ollama, garantindo que o montante e os objetivos financeiros do usuário nunca saiam de sua máquina.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que buscam sair da poupança ou otimizar seus investimentos atuais, mas que preferem uma interface de diálogo acessível em vez de planilhas complexas ou aplicativos bancários tradicionais.

---

## Persona e Tom de Voz

### Nome do Agente
FinAI Invest

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo e Consultivo. O agente não apenas entrega uma resposta, ele ensina o conceito por trás dela. Ele se comporta como um mentor financeiro que preza pela segurança e pelo crescimento patrimonial sustentável do cliente.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível, mas Profissional. Evita "juridiquês" financeiro desnecessário, mas mantém a sobriedade que o tema exige. É direto quando o assunto é risco e acolhedor ao explicar conceitos básicos.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o FinAI. Para começarmos a planejar o seu futuro, quanto você gostaria de investir hoje e qual o seu principal objetivo?"
- Confirmação: "Entendido. Você busca segurança para sua reserva de emergência com liquidez imediata. Deixe-me estruturar uma sugestão para você."
- Erro/Limitação: "No momento, não tenho acesso a cotações em tempo real de ações específicas, mas posso te explicar as melhores estratégias para renda variável de longo prazo."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Browser| B[Interface Streamlit]
    B --> C{Ollama}
    C -->|Modelo Local| D[Llama 3 / Mistral]
    D --> E[Lógica de Suitability]
    E --> D
    D --> F[Resposta na Tela]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit (Web UI moderna e interativa no navegador) |
| LLM | Ollama executando modelos como Llama3-8b ou Mistral |
| Base de Conhecimento | Arquivo JSON contendo matrizes de risco (Conservador, Moderado, Arrojado) |
| Validação | Camada de filtragem via Regex ou System Prompt no Ollama |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

[x] System Prompt Rígido: Instruir o Ollama a atuar estritamente como consultor, proibindo palpites sobre política, esportes ou conselhos médicos.

[x] Estrutura de Decisão: Forçar o modelo a perguntar "Qual seu prazo?" e "Qual sua tolerância a perdas?" antes de citar qualquer produto (ex: Tesouro Direto ou CDB).

[x] Aviso de Isenção local: Exibir um disclaimer fixo no rodapé do Streamlit sobre riscos de mercado.

### Limitações Declaradas
> O que o agente NÃO faz?

Não solicita senhas ou dados bancários do usuário.

Não substitui a consulta a um assessor de investimentos certificado (CVM/ANBIMA) para decisões complexas.

O agente depende do hardware local (CPU/GPU do usuário) para velocidade de resposta.

Não possui acesso à internet para buscar o valor do Dólar ou Selic do dia (a menos que você configure uma API de terceiros).
