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
Considerando duas notas, como verificar se um aluno foi aprovado, reprovado ou está
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
Desenvolva um programa que solicite a idade do usuário e informe se ele é
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
    
  
