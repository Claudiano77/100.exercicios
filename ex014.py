# c = float(input('Informe a temperatura em °C: '))
# f = 9 * c / 5 + 32
# print(f'A temperatura em {c}°C corresponde a {f}°F!')

def c_f(c):
    return c * 9/5 + 32

def f_c(f):
    return (f - 32 ) * 5/9

print("Converso de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = int(input("Escolha a opção (1 ou 2) "))

if opcao == 1:
    c = float(input("Digite a temperatura em °C "))
    print(f"{c:.2f} °C = {c_f(c):.2f} °F ")
elif opcao == 2:
    f = float(input("Digite a temperatura em °F "))
    print(f"{f:.2f} °F = {f_c(f):.2f} °C ")