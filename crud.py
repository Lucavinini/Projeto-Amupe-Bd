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


def BuscarPrefeitoPorNomeCpf():

    nome_prefeito = input("Digite o nome do prefeito: ")
    cpf_prefeito = input("Digite o CPF do prefeito: ")

    # Consulta no Supabase
    resultado = supabase.table("prefeitos") \
        .select("*") \
        .eq("prefeito", nome_prefeito) \
        .eq("cpf", cpf_prefeito) \
        .execute()

    # Verifica se encontrou algum registro
    if resultado.data:
        print("\nPrefeito encontrado:")
        for prefeito in resultado.data:
            print(f"Nome: {prefeito['prefeito']}")
            print(f"Município: {prefeito['municipio']}")
            print(f"Região: {prefeito['regiao']}")
            print(f"População: {prefeito['populacao']}")
            print(f"CPF: {prefeito['cpf']}")
            print(f"Partido: {prefeito['partido']}")
            print(f"Status: {prefeito['status']}")
            print(f"Telefone: {prefeito['telefone']}")
            print(f"Email: {prefeito['email']}")
            print(f"Esposa: {prefeito['esposas']}")
    else:
        print("Nenhum prefeito encontrado com esse nome e CPF.")


def DeletarPrefeito():
    cpf_prefeito = input("Digite o CPF do prefeito a ser deletado: ")

    # Confirmação
    confirmacao = input(f"Tem certeza que deseja deletar o prefeito com CPF {cpf_prefeito}? (s/n): ").lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return

    resultado = supabase.table("prefeitos").delete().eq("cpf", cpf_prefeito).execute()

    if resultado.data:
        print("Prefeito deletado com sucesso!")
    else:
        print("Nenhum prefeito encontrado com esse CPF.")


def EditarPrefeito():
    cpf_prefeito = input("Digite o CPF do prefeito que deseja editar: ")

    # Busca o prefeito no BD
    resultado = supabase.table("prefeitos").select("*").eq("cpf", cpf_prefeito).execute()

    if not resultado.data:
        print("Nenhum prefeito encontrado com esse CPF.")
        return

    prefeito = resultado.data[0]
    print("\nPrefeito encontrado:")
    print(prefeito)

    # Solicita novos dados (mantém o antigo se deixar vazio)
    novo_nome = input(f"Nome ({prefeito['prefeito']}): ") or prefeito['prefeito']
    novo_municipio = input(f"Município ({prefeito['municipio']}): ") or prefeito['municipio']
    nova_regiao = input(f"Região ({prefeito['regiao']}): ") or prefeito['regiao']
    nova_populacao = input(f"População ({prefeito['populacao']}): ") or prefeito['populacao']
    novo_partido = input(f"Partido ({prefeito['partido']}): ") or prefeito['partido']
    novo_status = input(f"Status ({prefeito['status']}): ") or prefeito['status']
    novo_telefone = input(f"Telefone ({prefeito['telefone']}): ") or prefeito['telefone']
    novo_email = input(f"Email ({prefeito['email']}): ") or prefeito['email']
    nova_esposa = input(f"Esposa ({prefeito['esposas']}): ") or prefeito['esposas']

    # Atualiza no banco
    supabase.table("prefeitos").update({
        "prefeito": novo_nome,
        "municipio": novo_municipio,
        "regiao": nova_regiao,
        "populacao": nova_populacao,
        "partido": novo_partido,
        "status": novo_status,
        "telefone": novo_telefone,
        "email": novo_email,
        "esposas": nova_esposa
    }).eq("cpf", cpf_prefeito).execute()

    print("Prefeito atualizado com sucesso!")

