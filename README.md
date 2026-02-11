# 🤖 FinAI Invest - Agente Financeiro Inteligente
O FinAI Invest é um assistente virtual consultivo desenvolvido para transformar a gestão financeira pessoal. Ele utiliza IA Generativa local (Ollama/Llama 3) para analisar históricos de transações, perfis de investimento e metas reais, oferecendo orientações personalizadas e seguras para o usuário.

---


### Caso de Uso
O agente foca na jornada do cliente João Silva, um investidor conservador cujo objetivo atual é completar sua reserva de emergência e planejar a entrada de um apartamento para 2027. O sistema resolve o problema da falta de clareza financeira ao:

Analisar gastos automaticamente a partir de arquivos CSV.

Sugerir alocações baseadas em produtos reais disponíveis na base de conhecimento.

Manter o foco na meta, evitando sugestões de alto risco para perfis conservadores.

---


### Tecnologias Utilizadas
Linguagem: Python 3.12+

Interface: Streamlit (Web UI interativa)

Processamento de Dados: Pandas & JSON

Cérebro da IA: Ollama rodando o modelo Llama 3 (Execução 100% local para privacidade de dados).

---


### Como Executar o Projeto
Para rodar este projeto localmente, siga os passos abaixo:


1. Pré-requisitos: 
Possuir o Python instalado (recomendado o uso do Python Launcher py).

Ter o Ollama instalado e o modelo baixado via terminal:

```text
ollama pull llama3
```

2. Instalação das Dependências:
Clone o repositório e, na pasta raiz, execute:

```text
py -m pip install pandas requests streamlit
```

3. Inicialização:
Devido à arquitetura de caminhos dinâmicos utilizada para localizar a base de dados em /data, a execução deve partir da pasta src:

```text
cd src
py -m streamlit run app.py
```

---

## 1. Documentação do Agente

### Caso de Uso
Problema: Paralisia de decisão e insegurança financeira de investidores iniciantes diante de termos técnicos e produtos complexos.

Solução: O FinAI Invest atua como um mentor proativo que utiliza RAG (Retrieval-Augmented Generation) local para analisar o contexto real do usuário (transações e metas) e sugerir caminhos seguros, explicando o "porquê" de cada movimento financeiro.

Diferencial: Privacidade absoluta. Ao utilizar o Ollama, os dados sensíveis do patrimônio do usuário nunca saem da máquina local.

Persona e Tom de Voz
Personalidade: Consultivo, educativo e focado em segurança patrimonial.

Tom: Acessível e profissional. Transforma o "juridiquês" financeiro em orientações práticas, sendo acolhedor com dúvidas básicas e rígido quanto aos riscos.

Arquitetura e Segurança
Arquitetura: Interface em Streamlit conectada via API ao Ollama (Modelo Llama 3).

Segurança Anti-Alucinação: Implementação de "Fonte de Verdade" via System Prompt, forçando a IA a citar apenas produtos presentes no produtos_financeiros.json.

Limitação: Não possui acesso à internet para cotações em tempo real; depende estritamente da base de dados fornecida.

📄 [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

📄 [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

System Prompt (Resumo)
"Você é o FinAI Invest. Baseie suas respostas EXCLUSIVAMENTE nos dados fornecidos. Se o perfil for Conservador, PRIORIZE Tesouro Selic e proíba Renda Variável. Use o nome do cliente (João Silva) para personalizar a fala."

Exemplos de Interação (Few-Shot)
Usuário: "Quanto gastei com lazer?"

Agente: "João, você gastou R$ 55,90 com lazer. Esse controle é essencial para atingir sua meta de R$ 15.000,00 para a reserva até junho de 2026."

Tratamento de Edge Cases
Fora de Escopo: Se questionado sobre receitas ou temas não financeiros, o agente gentilmente redireciona o foco para as metas do usuário.

Segurança: Bloqueia solicitações de dados de terceiros ou informações sensíveis não autorizadas.

📄 [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

A aplicação reside na pasta /src e utiliza o Streamlit para criar uma interface de chat moderna.

Execução: py -m streamlit run app.py (dentro da pasta src).

Conexão: API Local via biblioteca requests comunicando-se com o endpoint do Ollama na porta 11434.

📁 [`src/`](./src/)

---

### 5. Avaliação e Métricas

#### Como Avaliar o Agente
O FinAI Invest foi submetido a uma bateria de testes funcionais para garantir que a técnica de RAG (Retrieval-Augmented Generation) estava funcionando corretamente. A avaliação focou em garantir que o modelo local (Llama 3) não "alucinasse" e se mantivesse fiel aos dados de João Silva.

#### Métricas de Qualidade
| Métrica | O que avalia | Resultado no FinAI |
| :--- | :--- | :--- |
| **Assertividade** | O agente leu os dados corretamente? | **Alta:** Identifica com precisão o patrimônio de R$ 15.000 e a meta de R$ 50.000. |
| **Segurança** | Evitou sugestões de risco indevidas? | **Alta:** Bloqueia recomendações de renda variável devido ao perfil conservador do João. |
| **Fidelidade (Grounding)** | Baseou-se apenas nos arquivos? | **Excelente:** Após o ajuste da "Fonte de Verdade" no prompt, ele utiliza apenas o catálogo oficial. |
| **Privacidade** | Os dados saíram da máquina? | **Total:** Processamento 100% local via Ollama, garantindo sigilo bancário. |

#### Cenários de Teste Realizados
Teste 1: Cálculo e Inteligência de Dados (CSV)
* **Pergunta:** "Quanto gastei com alimentação e quanto isso representa em porcentagem nos meus gastos totais?"
* **Resposta esperada:** O agente deve identificar o valor de **R$ 570,00** para alimentação e calcular a representatividade sobre o total de gastos (R$ 1.664,00*), resultando em aproximadamente **34,25%**.
* **Resultado:** ✅ Correto.
> *Nota: Cálculo baseado no somatório das categorias no `transacoes.csv`.*

Teste 2: Recomendação de Produto (Perfil de Investidor)
* **Pergunta:** "Qual investimento você recomenda para mim?"
* **Resposta esperada:** O agente deve sugerir ativos de **Baixo Risco** (Tesouro Selic ou CDB Liquidez Diária), mantendo a coerência com o perfil **Conservador** do João Silva definido no `perfil_investidor.json`.
* **Resultado:** ✅ Correto.

Teste 3: Segurança e Suitability (Risco Inadequado)
* **Pergunta:** "Devo comprar ações da Petrobras?"
* **Resposta esperada:** O agente deve desencorajar a compra devido ao perfil conservador e à meta de curto prazo (Reserva de Emergência), sugerindo manter o foco em ativos de renda fixa.
* **Resultado:** ✅ Correto.

Teste 4: Filtro de Escopo e Informação Inexistente
* **Pergunta:** "Qual a melhor receita de bolo?"
* **Resposta esperada:** O agente deve informar que é especializado exclusivamente em finanças e investimentos, declinando educadamente a resposta fora do contexto.
* **Resultado:** ✅ Correto.

📄 [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

### Desafios Técnicos e Soluções (Lições Aprendidas)
Durante o desenvolvimento, foram aplicadas correções críticas para garantir a estabilidade do agente:

Gestão de Caminhos (Pathing): Implementação da biblioteca os para mapear diretórios de forma dinâmica, permitindo que a aplicação encontre a base de dados independentemente de onde o terminal foi iniciado.

Integridade de Dados (JSON): Correção de erros de sintaxe e delimitadores nos arquivos de conhecimento, garantindo que o parser do Python processe as informações sem interrupções.

Ambiente Windows: Padronização dos comandos via py -m para evitar erros de reconhecimento do comando pip e python no PATH do sistema.

Prompt Engineering: Estruturação de um System Prompt robusto para evitar alucinações, forçando o modelo a citar apenas dados reais da carteira do cliente.
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
