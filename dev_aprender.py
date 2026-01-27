# desafio dev aprende

"""
 Método 5Q's para montar algorítimo:
Analise criticamente o problema e descubra?
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1° Quais são os dados de entrada necessários?

2° O que devo fazer com estes dados?

3° Quais são as restriçôes deste problema?

4° Qual é o resultado esperado?

5° Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
Pseudocódigo

"""

# variáveis
# s = float(input("Digite o seu salário: "))
# h = float(input("Quantas horas voce trabalha por mes: "))
# ht = s / h
# print(f"Com o seu salário {s:.2f} suas horas esta saindo a {ht:.2f}  ")

# condicionais if elif else

# n1 = int(input("Digite um numero"))
# n2 = int(input("Digite o segundo codigo"))
# if n1 >= n2:
#     print(f"O primeiro número {n1} é maior que o segundo {n2}")
# else:
#     print(f"O segundo número {n2} é maior que o primeiro {n1}")

# s = input("Digite sua senha: ")
# if len(s) >= 6:
#     print("Senha valida")
# else:
#     print("Senha invalida")

# for
# idades = [13,15,18,30,50,75]
# # Exiba somente os maiores de 18 anos na tela
# for i in idades:
#     if i >= 18:
#         print(f'{i} Maior de idade')
#     else:
#         print(f'{i} Menor de idade')

#while


# tentativa = 0
# sc = "1234"
# while tentativa < 3:
#     s = input("Digite a senha correta: ")
#     if s == sc:
#         print("Bem vindo ao sistema: ")
#         break
#
#     else:
#         print("senha incorreta.")
#         tentativa = tentativa + 1
# else:
#     print("Numero de tentativa excedida!")

# nome = ""
# while nome == "":
#     nome = input("digite seu nome: ")
#
# print(f"Bem vindo {nome}")

# h = 0
# while h <= 17:
#     print(h)
#     h = h +1
#
# print('Hora de ver o por do sol')

import json
import random

# usuario = ""
# senha = ""
# tentativa = 0
# while usuario != "Claudiano" and s != "1234" and tentativa < 3:
#     usuario = input("Digite o Usuario: ")
#     senha = input("Digite sua senha: ")
#     tentativa = tentativa + 1
# if usuario == "claudiano" and s == "1234":
#     print("Bem vindo ao sistema")
# else:
#     print("Tente novamente em 30 minutos")

# Listas

# preco = [20,50,100]
# #       [ 0, 1, 2 ] o índice sempre começa pelo (0)
# print(preco[2])
#
# nomes = ['Brasil','EUA','México']
# print(nomes[0])
#
# # Encontra o índice automaticamente
# print(nomes.index('EUA'))

# manipular listas add novos itens
# salarios = [2500, 5000, 7000]
# # salario_usuario = float(input('Qual o seu salário: '))
# # salarios.append(salario_usuario)
# # print(salarios)
# # s = sum(salarios)
# # print(s)
# #
# total = 0
# for i in salarios:
#     total += i
# print(total)

# Projeto fatorial
# f = 0
# num = int(input('Digite um numero para ver o fatorial: '))
# if num > 0: #and type (num) == int:
#     fatorial = 1
#     for i in range (1, num + 1):
#         print(f' {fatorial} * {i}')
#         fatorial = fatorial * i
#         print(f'{fatorial}')
#     print(f'o fatorial de {num} é {fatorial}')
# else:
#         print('Digite o numero valido')
import random
# while True:
#     num = int(input("Digite um digito de 1 a 10: "))
#     numero = random.randint(1,10)
#
#     if num == numero:
#        print(f'Parabêns voce acertou: {numero}')
#        break
#
#     else:
#         print(f'Seu numero é: {num} o numero aleatorio: {numero} digite novamente')

# outro tipo de programa
# num = random.randint(1,10)
# acertou = False
#
# while acertou == False:
#     chute = int(input('Chute um numero: '))
#     if chute > num:
#        print('chute um valor menor')
#     elif chute < num:
#        print('chute um valor maior')
#     else:
#        print(f'Você acertou o nùmero {num} esta correto!!!')
#        acertou = True

velocidade = int(input('Digite a velocidade: '))
if velocidade <= 80:
    print('Não ouve multa')
elif velocidade > 80 and velocidade <= 90:
    print('Levou multa leve')
elif velocidade > 90 and velocidade <= 100:
    print('Levou multa grave')
else:
    print('Se ta doido multa gravíssima')


















