from db import supabase
from crud import InserirPrefeito
from interface import Interface

a = 0

while a != 5:

    Interface()
    a = int(input())

    if a == 1:
        muni = input("Digite o municipio: ")
        regi = input("Digite a região: ")
        popu = input("Digite a população: ")
        nome = input("Digite um nome: ")
        cpfi = input("Digite o CPF: ")
        part = input("Digite o partido: ")
        stat = input("Digite o status (Eleito/Não eleito): ")
        tel = input("Digite o telefone: ")
        emai = input("Digite o email: ")
        espo = input("Digite o nome da esposa: \n")

        InserirPrefeito(muni,regi,popu, nome, cpfi, part, stat, tel,
                        emai, espo)

    
    

    
    

    



