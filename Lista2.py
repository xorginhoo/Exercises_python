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

