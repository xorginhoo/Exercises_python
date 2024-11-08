'''
1. Crie um programa que solicite um número ao usuário e informe se ele é par ou
ímpar.

'''
num = int(input("Digite um número:"))
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")

'''
2. Escreva um programa que peça dois números e mostre qual deles é o maior. Se
forem iguais, informe que são iguais.
'''
num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))

if num1>num2:
    print(f"O {num1} é maior que {num2}.")
elif num2>num1:
     print(f"O {num2} é maior que {num1}.")
else:
     print(f"O {num1} e {num2} são iguais.")

'''
3.Considerando duas notas, como verificar se um aluno foi aprovado, reprovado ou está
em recuperação?
'''
num1 = int(input("Digite a 1º nota:"))
num2 = int(input("Digite 2º nota:"))

media = (num1+num2)/2

if media>=7:
    print(f"{media} aprovado")
    
elif media<7 and media>3 :
     print(f"{media} recuperação")
     
else :
     print(f"{media} reprovado")

"""
4.Desenvolva um programa que solicite a idade do usuário e informe se ele é
menor de idade (menos de 18 anos), adulto (18 a 60 anos) ou idoso (mais de 60
anos).
"""
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("de menor")

elif idade >= 18 and idade < 60:
    print("adulto")
else:
    print("idoso")
    
"""
5.Faça um programa que pergunte a nota de um aluno (de 0 a 10) e exiba
"Aprovado" se a nota for 7 ou mais, "Reprovado" se a nota for 4 ou menos e
"Recuperação" se estiver entre 4 e 7.
"""

num = int(input("digite a nota de um aluno (de 0 a 10): "))

if num>=7:
    print(f"{num} aprovado")
elif num<7 and num>4 :
     print(f"{num} recuperação")
else :
     print(f"{num} reprovado")

"""
6.Crie um programa que pergunte a idade do usuário e informe se ele pode votar
(maior ou igual a 16 anos).
"""

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("pode votar")
else:
    print("NÃO PODE VOTAR")

"""
7.Escreva um programa que pergunte um número de 1 a 7 e informe o dia da
semana correspondente (1 para Domingo, 2 para Segunda, etc.).
"""

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido! Digite um número de 1 a 7.")

"""
8.Desenvolva um programa que solicite três lados e informe se é possível formar
um triângulo e, se sim, se é equilátero, isósceles ou escaleno.
"""

n1 = int(input("Digite o 1º lado: "))
n2 = int(input("Digite o 2º lado: "))
n3 = int(input("Digite o 3º lado: "))


if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:

    if n1 == n2 == n3:
        print("O triângulo é equilátero.")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Não é possível formar um triângulo.")

"""
9. Faça um programa que pergunte o salário de um funcionário e calcule o aumento:
10% se o salário for menor que 1000, senão, 5%.
"""

salario = float(input("Digite seu sálario: "))

if salario < 1000:
    aumento = (0.1*salario)+salario
    print(f"Seu salário agora é R${aumento:.2f} reais seu aumento foi de R${aumento-salario:.2f} reais")
else:
    aumento = (0.05*salario)+salario
    print(f"Seu salário agora é R${aumento:.2f} reais seu aumento foi de R${aumento-salario:.2f} reais")

"""
10. Escreva um programa que pergunte o preço de um produto e aplique um
desconto de 10% se o preço for maior que 100.
"""
vproduto = float(input("Digite o preço de um produto: "))

if vproduto > 100:
    vfinal = vproduto-(0.1*vproduto)
    print(f"Valor final R${vfinal:.2f} reais")
else:
     print(f"Valor final R${vproduto:.2f} reais")

"""
11.Desenvolva um programa que pergunte ao usuário se ele abasteceu com álcool
ou gasolina e informe o preço final baseado no tipo de combustível (gasolina: 6.50,
álcool: 5.00, considerando um desconto de 5% para álcool).
"""

preco_gasolina = 6.50
preco_alcool = 5.00
desconto_alcool = 0.05  

op = input("Abasteceu com álcool ou gasolina? (escreva 'alcool' ou 'gasolina'): ").lower()

if op == 'alcool':
    qtda = float(input("Digite a quantidade de álcool (em litros): "))
    valor_inicial = qtda * preco_alcool  
    valor_desconto = valor_inicial * desconto_alcool  
    preco_final = valor_inicial - valor_desconto 
    print(f"Valor inicial: R$ {valor_inicial:.2f}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor final para {qtda} litros de álcool: R$ {preco_final:.2f}")
elif op == 'gasolina':
    qtda = float(input("Digite a quantidade de gasolina (em litros): "))
    preco_final = qtda * preco_gasolina 
    print(f"Valor final para {qtda} litros de gasolina: R$ {preco_final:.2f}")
else:
    print("Opção inválida. Por favor, digite 'alcool' ou 'gasolina'.")

"""
12. Crie um programa que pergunte dois números e um operador (+, -, *, /) e exiba o
resultado da operação, tratando casos de divisão por zero.
"""
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")
elif operador == '-':
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")
elif operador == '*':
    resultado = n1 * n2
    print(f"{n1} * {n2} = {resultado}")
elif operador == '/':
    if n2 != 0:
        resultado = n1 / n2
        print(f"{n1} / {n2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operador inválido. Por favor, escolha entre +, -, * ou /.")
    
"""
13. Faça um programa que calcule o IMC (Índice de Massa Corporal) a partir do
peso e altura informados pelo usuário e classifique o resultado em: Abaixo do peso,
Peso normal, Sobrepeso, Obesidade.
"""
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: (em metros) "))

imc = peso/(altura**2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Classificação: {classificacao}")


    

