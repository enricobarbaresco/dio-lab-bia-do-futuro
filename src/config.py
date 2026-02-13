import pandas as pd
import json
import os

def carregar_dados():
    # Caminhos dos arquivos (ajuste conforme sua estrutura de pastas)
    caminho_transacoes = 'data/transacoes.csv'
    caminho_perfil = 'data/perfil_investidor.json'
    
    dados = {}
    
    if os.path.exists(caminho_transacoes):
        df = pd.read_csv(caminho_transacoes)
        dados['saldo_total'] = df['valor'].sum()
        dados['gastos_recentes'] = df.to_dict(orient='records')
    
    if os.path.exists(caminho_perfil):
        with open(caminho_perfil, 'r', encoding='utf-8') as f:
            dados['perfil'] = json.load(f)
            
    return dados
