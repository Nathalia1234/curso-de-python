#Sistema de somar média e dividir com lista.

#Foi criado uma lista vazia chamada numeros.
numeros = []

# volta = True   # volta é verdade
# while(volta):  # enquanto volta for verdade 
# print('oi')    #printa Oi .. porém volta será sempre verdade, então vai dá um loop de Oi rsrsrsr

continuar = True  #Continuar será verdadeiro
while(continuar): #Enquanto Continuar for verdadeiro 
    try:  #Tente fazer 
        numero = float(input("Informe um número:")) #O usúario vai digitar um número, o input vai 
                                                    #transformar em float e esse número ficará armazenado
                                                    #na variável número
        numeros.append(numero)  #O número digitado pelo usúario será armazenado na lista. 
    except:  #Caso dê erro, será informado essa mensagem abaixo.
        print("Por favor digite apenas números")

    escolha = input("Você deseja continuar? [S/N]") #A cada número informado aparecerá essa pergunta,
                                                    #para saber se o usúario quer continuar informando
                                                    #os números.
    #A função .lower serve para  transformar o conteúdo da variável em minusculo
    if(escolha.lower() == 's'): #Se o usúario digitou 's minusculo'
        continuar = True   #continuar será verdadeiro
    elif(escolha.lower() ==  'n'): #Senão 
        continuar = False #Continuar será falso 
    else: #Caso o usúario digite uma letra que não seja 's' ou 'n' 
        print("Por favor, digite S ou N") #Aparecerá essa mensagem informando para o usúario
                                          # informar apenas S ou N


#sum() é uma função que soma todos os elementos presentes em uma lista, seja int ou float. 
#A variável soma recebe a função sum que entre parenteses esta passando a lista  que foi criada.
soma = sum(numeros)

#len() é uma função que devolve a quantidade de itens na lista.
media = soma / len(numeros)

print("A média é: " , media)

#Ver como a lista ficou com os numeros que o usuario digitou.
print("Os números que estão na lista são: ",numeros)