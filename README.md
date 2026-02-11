## 🤖 FinAI Invest - Agente Financeiro Inteligente
O FinAI Invest é um assistente virtual consultivo desenvolvido para transformar a gestão financeira pessoal. Ele utiliza IA Generativa local (Ollama/Llama 3) para analisar históricos de transações, perfis de investimento e metas reais, oferecendo orientações personalizadas e seguras para o usuário.


### Caso de Uso
O agente foca na jornada do cliente João Silva, um investidor conservador cujo objetivo atual é completar sua reserva de emergência e planejar a entrada de um apartamento para 2027. O sistema resolve o problema da falta de clareza financeira ao:

Analisar gastos automaticamente a partir de arquivos CSV.

Sugerir alocações baseadas em produtos reais disponíveis na base de conhecimento.

Manter o foco na meta, evitando sugestões de alto risco para perfis conservadores.


### Tecnologias Utilizadas
Linguagem: Python 3.12+

Interface: Streamlit (Web UI interativa)

Processamento de Dados: Pandas & JSON

Cérebro da IA: Ollama rodando o modelo Llama 3 (Execução 100% local para privacidade de dados).


### Como Executar o Projeto
Para rodar este projeto localmente, siga os passos abaixo:


1. Pré-requisitos
Possuir o Python instalado (recomendado o uso do Python Launcher py).

Ter o Ollama instalado e o modelo baixado via terminal:

```text
ollama pull llama3
```

2. Instalação das Dependências
Clone o repositório e, na pasta raiz, execute:

```text
py -m pip install pandas requests streamlit
```

3. Inicialização
Devido à arquitetura de caminhos dinâmicos utilizada para localizar a base de dados em /data, a execução deve partir da pasta src:

```text
cd src
py -m streamlit run app.py
```


## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

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
