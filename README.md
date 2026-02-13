# FinAI Invest - Educador Financeiro Inteligente

Um assistente virtual consultivo que utiliza IA Generativa local para transformar a gestão financeira pessoal, oferecendo orientações personalizadas e seguras baseadas em análise de dados reais.

---

## Sobre o Projeto

O FinAI Invest resolve um problema comum: a paralisia de decisão financeira. Muitos brasileiros possuem capital para investir, mas sentem-se inseguros diante da complexidade dos produtos financeiros ou não sabem como alinhar seus objetivos pessoais aos ativos disponíveis no mercado.

### Solução Implementada

O agente atua como um mentor financeiro proativo que:

- Analisa automaticamente históricos de transações (CSV)
- Cruza perfil de investidor com produtos financeiros disponíveis
- Sugere alocações personalizadas baseadas em metas reais
- Explica o "porquê" de cada recomendação de forma educativa
- Mantém privacidade total: processamento 100% local via Ollama

### Caso de Uso Real

O sistema foi desenvolvido focando na jornada de João Silva, um analista de sistemas de 32 anos com perfil conservador que busca:

- Completar sua reserva de emergência (R$ 15.000 até junho/2026)
- Juntar entrada para apartamento (R$ 50.000 até dezembro/2027)

---

## Diferenciais

**Privacidade Absoluta**: Ao utilizar Ollama com modelo Llama 3, todos os dados financeiros sensíveis são processados localmente, nunca saindo da máquina do usuário.

**Anti-Alucinação**: Sistema de "Fonte de Verdade" via System Prompt força a IA a citar apenas produtos presentes na base de conhecimento, evitando sugestões indevidas.

**Educativo**: Não apenas responde, mas ensina conceitos financeiros de forma acessível, transformando "juridiquês" em orientações práticas.

---

## Arquitetura

```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Streamlit (UI)     │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Ollama API Local   │
│  (porta 11434)      │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Llama 3 (Local)    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────────────┐
│  Base de Conhecimento       │
│  • perfil_investidor.json   │
│  • produtos_financeiros.json│
│  • transacoes.csv           │
│  • historico_atendimento.csv│
└─────────────────────────────┘
```

---

## Estrutura do Repositório

```
lab-agente-financeiro/
│
├── data/                              # Base de conhecimento
│   ├── perfil_investidor.json         # Perfil e metas do João Silva
│   ├── produtos_financeiros.json      # Catálogo de produtos (Tesouro, CDB, FII)
│   ├── transacoes.csv                 # Histórico de gastos e aportes
│   └── historico_atendimento.csv      # Atendimentos anteriores
│
├── src/                               # Código da aplicação
│   ├── app.py                         # Interface Streamlit + gerenciamento de estado
│   ├── agente.py                      # Integração com Ollama + lógica de RAG
│   └── config.py                      # Funções de leitura e agregação de dados
│
├── docs/                              # Documentação completa
│   ├── 01-documentacao-agente.md      # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md        # Estratégia de dados e RAG
│   ├── 03-prompts.md                  # System prompt e exemplos
│   ├── 04-metricas.md                 # Testes e avaliação
│   └── 05-pitch.md                    # Roteiro de apresentação
│
├── assets/                            # Diagramas e recursos visuais
├── requirements.txt                   # Dependências Python
└── README.md                          # Este arquivo
```

---

## Como Executar

### Pré-requisitos

1. **Python 3.12+** instalado
2. **Ollama** instalado e configurado
3. Modelo Llama 3 baixado:

```bash
ollama pull llama3
```

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/lab-agente-financeiro.git
cd lab-agente-financeiro
```

2. Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

### Execução

**IMPORTANTE**: Devido à arquitetura de caminhos dinâmicos, execute a partir da pasta `src`:

```bash
cd src
py -m streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

---

## Engenharia de Prompts

### System Prompt (Resumo)

```
Você é o FinAI Invest, especializado em orientação financeira para João Silva.

REGRAS CRÍTICAS:
1. FONTE DE VERDADE: Use APENAS dados dos arquivos fornecidos
2. PERFIL CONSERVADOR: Priorize Tesouro Selic e CDB para reserva de emergência
3. SEGURANÇA: Nunca garanta rentabilidade. Sempre avise sobre riscos
4. EDUCAÇÃO: Explique o "porquê" de cada sugestão
5. OBJETIVIDADE: Use valores reais do João para personalizar respostas
```

### Técnicas Aplicadas

- **Few-Shot Prompting**: Exemplos de perguntas e respostas ideais
- **Context Injection**: Dados JSON/CSV injetados dinamicamente no prompt
- **Guardrails**: Regras rígidas contra alucinação e sugestões inadequadas

Ver documentação completa em [`docs/03-prompts.md`](docs/03-prompts.md)

---

## Base de Conhecimento

### Dados Mockados Utilizados

| Arquivo | Tipo | Finalidade |
|---------|------|------------|
| `perfil_investidor.json` | JSON | Perfil conservador, renda mensal R$ 5.000, patrimônio R$ 15.000 |
| `produtos_financeiros.json` | JSON | Tesouro Selic, CDB, LCI/LCA, FII, Fundo de Ações |
| `transacoes.csv` | CSV | Gastos categorizados (moradia, alimentação, transporte...) |
| `historico_atendimento.csv` | CSV | Contexto de interações anteriores |

### Estratégia de RAG (Retrieval-Augmented Generation)

Os dados são carregados via `pandas` e `json`, formatados e injetados no System Prompt a cada interação:

```python
import json
import pandas as pd

perfil = json.load(open('../data/perfil_investidor.json'))
produtos = json.load(open('../data/produtos_financeiros.json'))
transacoes = pd.read_csv('../data/transacoes.csv')
historico = pd.read_csv('../data/historico_atendimento.csv')
```

O contexto completo (perfil + produtos + resumo financeiro) é enviado ao Ollama para garantir respostas baseadas em fatos.

Ver detalhes em [`docs/02-base-conhecimento.md`](docs/02-base-conhecimento.md)

---

## Avaliação e Métricas

### Testes Realizados

| Teste | Pergunta | Resultado |
|-------|----------|-----------|
| **Cálculo de Dados** | "Quanto gastei com alimentação?" | ✅ R$ 570,00 (34,25% do total) |
| **Recomendação** | "Qual investimento você recomenda?" | ✅ Tesouro Selic (perfil conservador) |
| **Segurança** | "Devo comprar ações da Petrobras?" | ✅ Desencorajou devido ao perfil |
| **Escopo** | "Qual a melhor receita de bolo?" | ✅ Declinou educadamente |

### Métricas de Qualidade

| Métrica | Avaliação | Observação |
|---------|-----------|------------|
| **Assertividade** | Alta | Identifica corretamente patrimônio e metas |
| **Segurança** | Alta | Bloqueia sugestões de risco indevidas |
| **Fidelidade** | Excelente | Usa apenas catálogo oficial (anti-alucinação) |
| **Privacidade** | Total | Processamento 100% local via Ollama |

Ver testes completos em [`docs/04-metricas.md`](docs/04-metricas.md)

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.12+
- **Interface**: Streamlit (UI web interativa)
- **LLM**: Ollama + Llama 3 (execução local)
- **Processamento**: Pandas (CSV) + JSON nativo
- **Comunicação**: Biblioteca `requests` (API REST)

---

## Lições Aprendidas

### Desafios Técnicos Superados

1. **Gestão de Caminhos**: Implementação da biblioteca `os` para mapear diretórios dinamicamente, permitindo execução independente do terminal

2. **Integridade de Dados**: Correção de erros de sintaxe em JSON para garantir parsing sem interrupções

3. **Ambiente Windows**: Padronização via `py -m` para evitar erros de PATH

4. **Prompt Engineering**: Estruturação robusta do System Prompt para evitar alucinações, forçando citação apenas de dados reais

5. **Latência**: Dependência de hardware local para velocidade de resposta (trade-off da privacidade)

---

## Demonstração

### Exemplos de Interação

**Usuário**: "Quanto gastei com lazer?"

**FinAI**: "João, você gastou R$ 55,90 com lazer. Esse controle é essencial para atingir sua meta de R$ 15.000,00 para a reserva até junho de 2026."

---

**Usuário**: "O Fundo Imobiliário é uma boa agora?"

**FinAI**: "Embora o FII tenha rendimento de ~0,95% ao mês, ele é de risco médio. Como seu perfil é Conservador e você está focado na Reserva de Emergência, recomendo primeiro atingir sua meta de R$ 15.000,00 no Tesouro Selic antes de diversificar."

---

## Documentação Completa

- **Caso de Uso e Arquitetura**: [`docs/01-documentacao-agente.md`](docs/01-documentacao-agente.md)
- **Estratégia de Dados**: [`docs/02-base-conhecimento.md`](docs/02-base-conhecimento.md)
- **Engenharia de Prompts**: [`docs/03-prompts.md`](docs/03-prompts.md)
- **Testes e Avaliação**: [`docs/04-metricas.md`](docs/04-metricas.md)
- **Roteiro de Pitch**: [`docs/05-pitch.md`](docs/05-pitch.md)

---

## Segurança e Privacidade

- ✅ Processamento 100% local (Ollama)
- ✅ Dados financeiros nunca saem da máquina
- ✅ System Prompt com guardrails contra alucinação
- ✅ Validação de perfil antes de sugestões
- ✅ Disclaimer sobre riscos de mercado

---

## Licença

Este projeto foi desenvolvido para fins educacionais como parte de um desafio de IA Generativa.

---

## Autor

Desenvolvido como solução completa do desafio de Agente Financeiro Inteligente, demonstrando aplicação prática de RAG, prompt engineering e processamento local de dados sensíveis.

**Nota**: O agente foi projetado para fins consultivos e educacionais. Não substitui a consulta a um assessor de investimentos certificado (CVM/ANBIMA) para decisões financeiras complexas.
