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

"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = float(input("Digite um número real: "))

print("Produto do dobro do primeiro com metade do segundo:", (2 * n1) * (n2 / 2))
print("Soma do triplo do primeiro com o terceiro:", (3 * n1) + n3)
print("Terceiro elevado ao cubo:", n3 ** 3)

"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
h = float(input("Digite sua altura: "))

print (f"Seu peso ideal é {(72.7*h) - 58:.2f}")


"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""
h = float(input("Digite sua altura: "))

print("masculino:")
print (f"a) Seu peso ideal é {(72.7*h) - 58:.2f}")
print("")
print("feminino:")
print (f"b) Seu peso ideal é {(62.1*h) - 44.7:.2f}")

"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar
uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que

leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a
quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
pagar. Imprima os dados do programa com as mensagens adequadas.
"""

limite = 50 
multakg = 4.00 

peso = float(input("Digite o peso de peixes trazido por João (em quilos): "))

excesso = 0
multa = 0

if peso > limite:
    excesso = peso - limite
    multa = excesso * multakg

if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} quilos")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print("João não precisa pagar multa. Peso dentro do limite.")
