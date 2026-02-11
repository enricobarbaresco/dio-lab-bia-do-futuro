# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal - Interface Streamlit e Gerenciamento de Estado
├── agente.py           # # Lógica de integração com Ollama e Processamento de Dados
├── config.py           # Configurações - Funções de leitura e agregação (JSON/CSV)
└── requirements.txt    # Dependências do projeto
```

## Exemplo de requirements.txt

```
streamlit
pandas
ollama
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
