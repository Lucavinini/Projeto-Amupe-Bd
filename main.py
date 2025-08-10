from db import supabase
from crud import InserirPrefeito

InserirPrefeito(
    municipio="Abreu e Lima",
    regiao="Nordeste",
    populacao=50000,
    prefeito="João da Silva",
    cpf="12345678900",
    partido="ABC",
    status="eleito",
    telefone="(87) 99999-9999",
    email="joao@example.com",
    esposas="Maria da Silva"
)


