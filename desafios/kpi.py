"Desafio do dia: Cálculo de Bônus com Entrada do Usuário"

#Escreva um programa em Python que solicita ao usuário para 
#digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
#O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação
# com o bônus recebido."


nome = input("Digite seu nome:")
salario = float(input("Informe seu salario:"))
bonus = float(input("Informe seu bonus em %:"))

calculo_bonus = (1000 + salario * bonus)
print(f"Olá {nome}, o seu salario é {salario} e com bonus fica {calculo_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?



#Exercício 1
   
nome2 = input('Digite seu nome:')
print(len(nome2)) 


#Exercício 2
num1 = input('Digite um valor:')
num2 = input('Digite outro valor:')

sum = len(num1) + len(num2)
print(sum)

