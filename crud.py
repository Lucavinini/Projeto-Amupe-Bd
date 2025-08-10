from db import supabase

from db import supabase

def InserirPrefeito(municipio, regiao, populacao, prefeito, cpf, partido, status, telefone, email, esposas):
    dados = {
        "municipio": municipio,
        "regiao": regiao,
        "populacao": populacao,
        "prefeito": prefeito,
        "cpf": cpf,
        "partido": partido,
        "status": status,
        "telefone": telefone, 
        "email": email,
        "esposas": esposas
    }

    # Inserção no banco
    res = supabase.table("prefeitos").insert(dados).execute()

    if res.data:
        print("Novo registro adicionado")
    else:
        print("Erro ao inserir os dados: ", res)
