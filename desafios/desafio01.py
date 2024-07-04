"Desafio do dia: Cálculo de Bônus com Entrada do Usuário"

#Escreva um programa em Python que solicita ao usuário para 
#digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
#O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação
# com o bônus recebido."


nome = input("Digite seu nome:")
salario = float(input("Infome seu salario:"))
bonus = float(input("Infome seu bonus em %:"))

calculo_bonus = ((1000 + salario) * bonus)
print(f"Olá {nome}, o seu salario é {salario} e com bonus fica {calculo_bonus}")