from db import supabase
from crud import InserirPrefeito, BuscarPrefeitoPorNomeCpf, DeletarPrefeito, EditarPrefeito
from interface import Interface

while True:

    Interface()
    comando = input("Digite uma opção: ")

    match comando:
        case "1":
            BuscarPrefeitoPorNomeCpf() 
        case "2":      
            muni = input("Digite o municipio: ")
            regi = input("Digite a região: ")
            popu = input("Digite a população: ")
            nome = input("Digite um nome: ")
            cpfi = input("Digite o CPF: ")
            part = input("Digite o partido: ")
            stat = input("Digite o status (Eleito/Não eleito): ")
            tel = input("Digite o telefone: ")
            emai = input("Digite o email: ")
            espo = input("Digite o nome da esposa:")
            print("\n")

            InserirPrefeito(muni,regi,popu, nome, cpfi, part, stat, tel, emai, espo)
        case "3":
            EditarPrefeito()
        case "4":
            DeletarPrefeito()
        case "5":
            print("Bye bye..")
            break
        case _:
            print("Opção Inválida")

        