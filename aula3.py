##lista = [1,3,5]
####print(lista)
##
##lista2 = [1, 1.5, 'string', lista]
##print(lista2)
##
##print(lista2[1])
##
##print(len(lista2))

### imprimindo cada elemento da lista em uma linha
##i = 0
##while i < len(lista2):
##    print(lista2[i])
##    i += 1

##for elemento in lista2:
##    print(elemento)

### alterei um elemento específico da lista
##lista2[3] = 4
##print(lista2)

### alterar o elemento não altera a lista
##for elemento in lista2:
##    elemento = 0
##    print(elemento)
##
##print(lista2)

### mudamos a lista original
##i = 0
##while i < len(lista2):
##    lista2[i] = 0
##    i += 1
##
##print(lista2)

##print(lista + lista2)
##print(lista2 + lista)

##lista = []
##print(lista + [1] + [2])
##print(lista)

##i = 0
##while i < len(lista2):
##    lista = lista + [i]
##    i += 1
##
##print(lista)
##
##for i in lista:
##    lista2[i] = 0
##
##print(lista2)

##lista = []
##i = 5
##while i >= 0:
##    lista = lista + [i]
##    i -= 1
##
##print(lista)

##lista = []
##i = 0
##while i < 5:
##    lista = [i] + lista
##    i += 1
##    print(lista)
##
##print(lista)

### inserir um elemento no final lista
##lista = [1,3,5]
##lista.append(7)
##print(lista)

### removemos um elemento específico da lista
##lista.remove(1)
##print(lista)

### remove o primeiro elemento 1 da lista
##lista = [1,1,3,1,5]
##lista.remove(1)
##print(lista)

### remover o elemento 1 enquanto ele estiver na lista
##lista = [1,1,3,1,5]
##while 1 in lista:
##    lista.remove(1)
##    print(lista)
##
##print(lista)

### verificando se um número não está na lista
##lista = [1,2,3]
##print(4 not in lista)

##lista = [1,7,3,2,6,98,4,2,0]
##lista.sort()
##print(lista)
##
##lista = ['palavra', 'amendoa', 'caramelo', 'zebra']
##lista.sort()
##print(lista)
##
##lista.sort(reverse = True)
##print(lista)

##lista = [1,7,3,2,6,98,4,2,0]
##print(sorted(lista))
##print(lista)
##
##lista.reverse()
##print(lista)

##print([1]+[1]+[1])
##print([1]*3)

##lista = [1,3,5]
##lista.append(7)
##print(lista)
##
##### .insert(pos,numero) insere um numero na pos dada
##lista.insert(1,2)
##print(lista)
##
##### para tirar um número da posição específica usamos pop
##x = lista.pop(3)
##print(lista)
##print(x)


### Lista de Listas e For
### Exercício 1
##lista = [1,4,3,2,5,8]
##
##for elemento in lista:
##    print(elemento)

### Exercício 2
##n = int(input("digite um número inteiro: "))
##i = 0
##lista = []
##while i < n:
####    lista += [i]
####    lista.append(i)
####    lista.insert(i,i)
##    lista.insert(len(lista),i)
##    i += 1
##lista = list(range(0,n,1))

##print(lista)

### Exercício 3
##lista = [1,4,3,2,5,8]
##i = 0
##while i < len(lista):
##    print(lista[i])
##    i += 1

### Exercício 4
##lista = [1,4,3,2,5,8]
##pares = 0
##for elemento in lista:
##    if elemento % 2 == 0:
##        pares += 1
##
##print(pares)

##i = 0
##lista = []
##while i < 3:
##    n = int(input("digite um número: "))
##    lista.append(n)
##    i += 1
##
##print(max(lista))
##print(min(lista))
##print(sum(lista)/len(lista))

### Exercício 5
##lista = [1,4,3,8,2,5]
##maior = lista[0]
##for elemento in lista:
##    if elemento > maior:
##        maior = elemento
##
##print(maior)

### range(a,b,s) cria um tipo de lista que vai de a até b somando s sem incluir o b
##lista = list(range(1,7,2))
##print(lista)

### o passo s pode ser negativo
##lista = list(range(7,1,-1))
##print(lista)

### se a gente não passa s, ele assume s=1
##lista = list(range(3,8))
##print(lista)

### se não passamos a, ele assume a = 0
##lista = list(range(8))
##print(lista)

##for i in range(5):
##    print(i)

##lista = [1,4,3,8,2,5]
##for i in range(len(lista)):
####    print(lista[i])
##    lista[i] += 1
##
##print(lista)

##import random
##
##baralho = list(range(1,14))*4
##print(baralho)
##
##for i in range(10):
##    carta = baralho.pop(random.randint(0,len(baralho)-1))
##    print(carta)

##import random
##baralho = []
##naipes = ['copas', 'espadas','paus','ouros']
##for i in range(1,14):
##    for j in range(4):
##        carta = [i,naipes[j]]
##        baralho.append(carta)
####print(baralho)
##
##mao = []
##for i in range(5):
##    carta = baralho.pop(random.randint(0,len(baralho)-1))
##    mao.append(carta)
##
##print(mao)




lista1 = [1,2,3]
lista2 = [4,5]
lista3 = [6,7,8,9]

lista = [lista1,lista2,lista3]

for coluna in lista:
    for linha in coluna:
        print(linha)

