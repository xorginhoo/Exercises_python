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
    

