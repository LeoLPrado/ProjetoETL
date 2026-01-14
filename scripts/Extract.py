import requests
import pandas as pd

def extract(quantidade):
    url = "https://dummyjson.com/users"                         # Pegando a URL da API escolhida

    parametros = {                                              # Definindo os parametros do get
    'limit': quantidade,
    'select': 'firstName,lastName,age,email,gender'
    }

    try:
        resposta = requests.get(url, params=parametros)             # Buscando na API
        dados = resposta.json()['users']                            # Guardando na variavel 'dados' as informacoes dos users
        print(f'Status da requisição: {resposta.status_code}')
        return dados
        
    except Exception as e:
        print(f'Erro na Extração: {e}')
        return []                                                   # Retorna uma lista vazia