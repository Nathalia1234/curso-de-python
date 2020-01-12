#Sistema de somar média e dividir com lista.

#Foi criado uma lista vazia chamada números.
numeros = []

#Tenta fazer , pegar o que o usúario digitar 
try:  
    #O usúario digita , o input converte para int e salva em n1.
    n1 = int (input("Informe o primeiro valor: "))
    #append adiciona valor da variável na lista.
    numeros.append(n1) 
    #O usúario digita , o input converte para int e salva em n2.
    n2 = int (input("Informe o segundo valor: "))
    #append adiciona valor da variável na lista.
    numeros.append(n2)
    #O usúario digita , o input converte para int e salva em n3.
    n3 = int (input("Informe o terceiro valor: "))
    #append adiciona valor da variável na lista.
    numeros.append(n3)
    #Caso dê erro.
except: 
    #Aparecerá essa mensagem.
    print("Por favor, digite apenas numeros.")

#sum é uma função que soma todos os elementos presentes em uma lista seja int ou float. 
#a variavel soma recebe a função sum que entre parenteses esta passando a lista  que foi criada.
soma = sum(numeros)

#len é uma função que devolve a quantidade de itens na lista.
media = soma / len(numeros)

print("A media e: " , media)

#ver como a lista ficou com os numeros que o usuario digitou.
print(numeros)