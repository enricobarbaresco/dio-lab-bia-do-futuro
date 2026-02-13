### 📂 Source Code (src)
Esta pasta contém o núcleo da aplicação FinAI Invest, organizada de forma modular para separar a interface, a lógica do agente e as configurações de dados.

### 🏗️ Estrutura da Pasta
app.py: Interface do usuário desenvolvida em Streamlit. Gerencia o chat e o estado da aplicação.

agente.py: Cérebro da aplicação. Contém a lógica de integração com o modelo Llama 3 (via Ollama) e o processamento das respostas.

config.py: Camada de dados. Responsável pela leitura, limpeza e agregação dos arquivos CSV e JSON.

### 🚀 Como Rodar o Programa
Siga os passos abaixo para executar a aplicação localmente:

## 1. Pré-requisitos
Possuir o Python 3.10+ instalado.

Ter o Ollama instalado e o modelo Llama 3 baixado:
```
ollama pull llama3
```
## 2. Instalação de Dependências
Navegue até a raiz do projeto e instale as bibliotecas necessárias:
```
pip install -r requirements.txt
```
## 3. Configuração dos Dados
Certifique-se de que os arquivos de dados estão na pasta correta:

data/transacoes.csv

data/perfil_investidor.json

## 4. Execução
Inicie a aplicação através do comando do Streamlit apontando para o arquivo app.py:
```
python -m streamlit run src/app.py
```
### 🛡️ Segurança e Privacidade
O código foi estruturado para que todo o processamento ocorra localmente. As informações financeiras lidas no config.py são enviadas apenas para a instância local do Ollama, garantindo que nenhum dado sensível seja compartilhado com APIs de terceiros na nuvem.
