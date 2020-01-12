#O sistema será um dicionário de frutas que é uma estrutura de dados.
# 'Identificador': conteudo.

#No dicionário de frutas foi mostrado valores em três jeitos:
#Valor normal, Valor em lista e Valor em dicionário.
tabela_frutas = { 'tomate' :1.90,  
                            'banana' : [3.00,6.00] ,  
                            'abacaxi' :4.00,
                            'maçã':{ 'verde' :0.50, 'vermelho' :1.00}
                         }
#irá printar o preço do tomate
print(tabela_frutas['tomate'])
#irá printar o valor na posição 1 que é o 6.00
print(tabela_frutas['banana'][1])
#irá printar o valor da maçã verde
print(tabela_frutas[ 'maçã' ]['verde'])