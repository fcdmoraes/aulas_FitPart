####print(2+2)
##print('digite um número')#imprime um texto
##x = input() #lê uma entrada do usuário
##x = float(x) # converte a entrada para float
##print(x*2) #imprime o dobro da entrada
####print(x%2 == 0)
##if x%2 == 0:
##    print('seu número é par')
##    if x>0:
##        print('e positivo')
##    elif x == 0:
##        print('e nulo')
##    else:
##        print('e negativo')
##else:
##    print('seu número é ímpar')
##    if x>0:
##        print('e positivo')
##    else:
##        print('e negativo')

##print(True and True)
##print(True and False)
##print(True or False)

##print(True or True and False )
##print((True or True) and False )

##print('Alo Mundo!')

##print('digite um número')
##x = input()
##print('O numero digitado foi ' + x)

##x = input('digite um número: ')
##print('O número digitado foi', x)

##x = float(input('digite um número: '))
##y = float(input('digite um número: '))
##print('a soma é', x+y)

##x = float(input('digite a medida em metros: '))
##print('a medida convertida vale ',x*100,'cm', sep = '')


##import random
##
##moeda = random.randint(0,1)
##if moeda == 0:
##    print('cara')
##else:
##    print('coroa')

##import random
##
####i = 0
####while i < 3:
######    print(i)
####    i = i + 1
####    print(i)
####print('end')
##i = 0
##count = 0
##while i < 1000000:
##    moeda = random.randint(0,1)
##    if moeda == 0:
####        print('cara')
##        count += 1
####    else:
####        print('coroa')
##    i += 1 ## i = i + 1
##print(count/1000000)


##i = 0
##soma = 0
##while i <= 100:
##    soma += i
##    i += 1
##print(soma)

##i = 1
##produto = 1
##while i <= 100:
##    produto *= i
##    i += 1
##print(produto)

##while True:
##    x = input("para parar digite 'pare'")
##    if x == 'pare':
##        break

import random

r = random.randint(1,10)
while True:
    chute = int(input('chute um número inteiro emtre 1 e 10: '))
    if r == chute:
        break
##    else:
##        print('tente novamente')
    elif r > chute:
        print('chute mais alto')
    elif r < chute:
        print('chute mais baixo')
print('acertou')
    
##print (random.randint.__doc__)






    






