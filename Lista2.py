#1) Faça um Programa que peça e mostre a mensagem "Alo mundo" na tela.
print ("Alo mundo")

#2) Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = input("Digite um número: ")
print(f"o número escolhido foi o número {num}")
#ou
print ("o número escolhido foi o número "+ str(num))

#3) Faça um Programa que peça dois números e imprima a soma.
n1 = float(input("Digite o 1º número: ")) 
n2 = float(input("Digite o 2º número: "))  
soma = n1 + n2 
print(f"a soma de {n1} + {n2} = {soma}")

#4) Faça um Programa que peça as 4 notas bimestrais e mostre a média.
numeros = []
for i in range(4):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)  

soma = sum(numeros)  
print(f"A soma é {soma/4:.2f}.")

#ou

n1 = float(input("Digite a nota da unidade 1: "))
n2 = float(input("Digite a nota da unidade 2: "))
n3 = float(input("Digite a nota da unidade 3: "))
n4 = float(input("Digite a nota da unidade 4: "))
media = (n1 + n2 + n3 + n4)/4
 
print(f"media: {media:.2f}")

#5) Faça um Programa que converta metros para centímetros.
metro = float(input("digite valor em metros: ")) 
print (f"{metro*100} cm")

#6)Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("digite valor do raio de um círculo:")) 
print (f"{3.14*(raio**2)} cm")

#7)Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = int(input("digite o valor do lado do quadrado: "))
print (f"A area do quadrado é {lado**2} e o dobro é {(lado**2)*2}")

"""
8)Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
horasvalor = float(input("Digite o valor que ganha por hora: "))
horastrabalhadas = float(input("Digite as horas trabalhadas no mês: "))

print (f"Seu salário esse mês é de {horasvalor * horastrabalhadas}")

"""
9)Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius.
o C = 5 * ((F-32) / 9).
"""

F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5*((F-32)/9)

print (f"a temperatura {F:.1f} fahrenheit em celsius é {C:.2f}")

#10)Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input("Digite a temperatura em Celsius: "))
F = C * (9/5) + 32

print (f"a temperatura {C:.1f} Celsius em fahrenheit é {F:.2f}")


