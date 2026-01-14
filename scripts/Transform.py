import pandas as pd

def transform(dados):
    df = pd.DataFrame(dados)                                            # Gerando um data frame pandas a partir do dados dos usuarios

    df['fullName'] = df['firstName'] + ' ' + df['lastName']             # Criando uma coluna de fullName

    df = df.drop(columns=['firstName', 'lastName'])                     # Removendo as colunas que nao serao necessarias 

    df['age'] = df['age'].astype(str)                                   # Mudando o tipo de dado da idade

    nova_ordem = ['id','fullName','age', 'email', 'gender']             # Definindo uma nova ordem de colunas para o data framew
    df = df[nova_ordem]
    print('Limpeza dos dados realizada')
    return df