#O sistema precisa calcular a média.
#Primeiro: Definir os três números.
#Segundo: Somar os números.
#Terceiro: Dividir pela quantidade de números.
#Quarto: Mostrar o resultado. 
#Input exibe a mensagem e pega o que o usúario digitar. 


try: 
    n1 = int (input("Informe o primeiro valor: "))
    n2 = int (input("Informe o segundo valor: "))
    n3 = int (input("Informe o terceiro valor: "))
except: 
    print("Por favor, digite apenas números.")

soma = n1 + n2 + n3 

media = soma / 3

print("A média é: " , media)
