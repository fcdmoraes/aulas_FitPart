import MSFTdata

dados = MSFTdata.get_data()
##print(dados)


##for i in range(10):
##    print(dados[i])

lista_maximos = []
for linha in dados:
    maximo = float(linha[2])
    lista_maximos.append(maximo)

print(max(lista_maximos))

print(len(dados))

print(lista_maximos[0]*2)

'''maximos_suave[0] = (lista_maximos[0]+lista_maximos[1])/2'''
'''maximos_suave[n] = (lista_maximos[n]+lista_maximos[n+1])/2'''

##maximos_suave = []
##for n in range(0,len(lista_maximos)-1):
##    media = (lista_maximos[n] + lista_maximos[n+1])/2
##    maximos_suave.append(media)
##
##print(maximos_suave[0])
##print((lista_maximos[0]+lista_maximos[1])/2)
##print(max(maximos_suave))

""" buscar qual posição i da lista_maximos que é igual ao max,
ou seja, qual i que lista_maximos[i] = max(lista_maximos)"""

"""
1 - calcula o maior valor da lista_maximos
2 - varrer a lista_maximos inteira em busca do maior valor
3 - quando encontrar, imprimir o valor de dados[i][0]
sendo que dados[i] é linha do máximo e dados[i][0] é a data
dessa linha
"""

### se eu escrever: for i in lista_maximos
    ### i vai ser cada elemento da lista_maximos
### se eu escrever: for i in range(len(lista_maximos))
    ### i vai ser uma posição da lista_maximos
    ### ou seja, um número entre 0 e len(lista_maximos)-1
##maior_valor = max(lista_maximos)
##for i in range(len(lista_maximos)):
##    if lista_maximos[i] == maior_valor:
##        print(i)
##        print(dados[i][0])


##data = dados[0][0]
####print(data)
####print(data.split(' ')[0])
##dia = data.split(' ')[0]
##print(dia)
##print(dados[1][0])
##print(dia in dados[1][0])

##print(dados[-1])
"""
1 - pegar a data desejada
2 - criar uma planilha vazia pra esta data
3 - olhar cada linha da planilha dados
4 - se a data dessa linha conter a data desejada,
   incluir essa linha na nova planilha
"""
data = '2018-09-21'
##matriz = []
##for linha in dados:
##    if data in linha[0]:
##        matriz.append(linha)
##
matriz = list(filter(lambda linha: data in linha[0], dados))
matriz = list(map(lambda linha: linha[1].replace('.',','), matriz))

for linha in matriz:
    print(linha)

print(len(matriz))







