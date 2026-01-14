# nome = input("Qual o seu nome: ")
# idade = input("Qual a sua idade: ")
# peso = input("Qual o seu peso: ")
# print(f"Olá {nome}! Com: {idade} anos de idade e pesando: {peso} quilos esta muito fofinho.")
from datetime import date
hoje = date.today()
dia = int(input("Dia = "))
mes = int(input("Mes = "))
ano = int(input("Ano = "))
ano_atual = hoje.year
idade = ano_atual - ano
if (hoje.month, hoje.day) < (mes, dia):
    idade -= 1
print(f"Voçê nasceu no dia {dia} de {mes} de {ano} este ano voce completa:{idade}. correto?")
