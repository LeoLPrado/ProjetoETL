import sqlalchemy
import pandas as pd

def load(df):
    engine = sqlalchemy.create_engine('sqlite:///data/bancoSample.db')

    try:
        df.to_sql('Users', con=engine, if_exists='replace', index=False)
        print(f'Sucesso, {len(df)} linhas carregadas na tabela de usuarios')

    except Exception as e:
        print(f'Erro ao carregar no banco: {e}')