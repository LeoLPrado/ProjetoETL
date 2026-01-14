from scripts.Extract import extract
from scripts.Transform import transform
from scripts.Load import load

def rodar_pipeline():
    quantidade_cadastros = 50
    dados = extract(quantidade_cadastros)
    
    if dados:
        df_limpo = transform(dados)

        load(df_limpo)
        
if __name__ == "__main__":
    rodar_pipeline()