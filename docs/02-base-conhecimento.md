# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, atendimento de forma mais coerente e eficiente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre dúvidas e necessidades de aprendizado do usuário |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis e adequados ao perfil do usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto Fundo Imobiliário (FII) substituiu o Fundo Multimercado, devido uma maior aceitabilidade e conhecimento a respeito desse tipo de investimento.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados são acessados localmente através das bibliotecas pandas (para os arquivos CSV) e json (para os arquivos JSON). O script realiza a leitura dos arquivos dentro da pasta data/ no momento da inicialização do agente, conforme o trecho de código abaixo:

```python
import json
import panda as pd

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('/data/transacoes.csv')
historico = pd.read_csv('/data/historico_atendimento.csv')
produtos = json.load(open('/data/produtos_financeiros.json'))
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são consultados dinamicamente e injetados no System Prompt. Utilizamos uma técnica de "Context Injection" onde, a cada pergunta do usuário, o código seleciona as metas do João e o catálogo de produtos disponíveis, enviando-os como instruções de sistema para o Ollama. Isso força o modelo local a responder apenas com base no inventário real de produtos fornecido.

```text  
DADOS DO USUÁRIO:
{ 
 "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "Conservador",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
]
}

PERFIL DO INVESTIDOR:
{
  "perfis": [
    {
      "tipo": "Conservador",
      "objetivo": "Preservação de capital e liquidez",
      "tolerancia_risco": "Baixa",
      "alocacao_sugerida": ["renda_fixa"],
      "mensagem_alerta": "Priorizamos a segurança da sua reserva acima de tudo."
    },
    {
      "tipo": "Moderado",
      "objetivo": "Crescimento equilibrado com segurança",
      "tolerancia_risco": "Média",
      "alocacao_sugerida": ["renda_fixa", "fundo"],
      "mensagem_alerta": "Buscamos um pouco mais de ganho, aceitando pequenas oscilações."
    },
    {
      "tipo": "Arrojado",
      "objetivo": "Maximização de ganhos no longo prazo",
      "tolerancia_risco": "Alta",
      "alocacao_sugerida": ["renda_fixa", "fundo", "acoes"],
      "mensagem_alerta": "Você entende que o mercado oscila, visando o potencial do futuro."
    }
  ]
}

PRODUTOS DISPONÍVEIS:
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "11,5% ao ano (aproximadamente 0,95% ao mês)",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

TRANSAÇÕES DO USUÁRIO:
data,descricao,categoria,valor,tipo
2026-01-10,Aporte Tesouro Selic,renda_fixa,1000.00,entrada
2026-01-25,Rendimento CDB,proventos,12.50,entrada
2026-02-01,Novo Aporte LCI,renda_fixa,2000.00,entrada
2026-02-10,Taxa de Custódia,taxas,10.00,saida

HISTÓRICO DE ATENDIMENTO:
data,canal,tema,resumo,resolvido
2026-02-01,chat,Perfil,Definido perfil como Conservador,sim
2026-02-05,chat,Aporte,Cliente deseja investir R$ 5.000,sim
2026-02-10,chat,Sugestão,Explicado funcionamento do Tesouro Selic,sim
2026-02-11,chat,Dúvida,Diferença entre CDB e LCI para prazo de 1 ano,sim
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
### INSTRUÇÕES DE SISTEMA ###
Atue como o FinAI Invest. Use os dados abaixo para orientar o usuário.
Não sugira produtos fora da lista. Se o perfil for Conservador, proíba Renda Variável.

### DADOS DO USUÁRIO ###
- Nome: João Silva (Perfil: Moderado)
- Patrimônio: R$ 15.000,00
- Meta Prioritária: Completar reserva de emergência (Faltam R$ 5.000,00)
- Restrição: Marcou que NÃO aceita riscos no momento.

### RESUMO DE GASTOS ###
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Saúde: R$ 188,00
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90
- Saldo disponível aproximado: R$ 2.511,10

### HISTÓRICO DE ATENDIMENTO ###
- 2026-02-01: Perfil definido como Conservador.
- 2026-02-10: Explicado funcionamento do Tesouro Selic.

### PRODUTOS DISPONÍVEIS (JSON) ###
1. Tesouro Selic (Baixo Risco, 100% Selic)
2. CDB Liquidez Diária (Baixo Risco, 102% CDI)
3. Fundo Imobiliário - FII (Médio Risco, Variável)

### PERGUNTA DO USUÁRIO ###
"Tenho R$ 2.000 extras este mês. Onde coloco para bater minha meta mais rápido?"
```
