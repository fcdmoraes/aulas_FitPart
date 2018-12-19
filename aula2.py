### dentro de um print podemos usar '\n' para pular uma linha
##print('texto1\ntexto2')
### já o '\t' serve para tar uma tabulação
##print('texto1\ttexto2')
### duas barras serve para imprimir uma barra
##print('texto\\texto')
### \' serve para imprimir '
##print('\'texto\'')
### uma barra antes de um enter serve para continuar escrevendo o texto na linha de baixo
##print('texto \
##muito grande', end = '-')
### o end indica o que deve ser impresso no fim da linha. O padrão é um '\n'
##print('texto3','text4')

### o .format() serve para substituir valores em um string. Os valores entram em ordem, onde aprece {}
##altura = 75
##largura = 82
##peso = 12
####print('altura:', altura, 'cm')
##texto = 'altura: {}cm, largura: {}cm, peso:{}kg'.format(altura, largura, peso)
##print(texto)

##v0 = float(input("digite a velocidade inicial"))
##y0 = float(input("digite a posição inicial"))
##t = float(input("digite um instante de tempo"))
##
##yt = y0+v0*t-5*t**2
##print(yt)

##### Lista 1 #####

### Ex 1:

##idade = int(input("digite sua idade: "))
##if idade >= 18:
##    print('você é maior de idade')
##else:
##    print('você é menor de idade')

##### Lista Etrutura Condicionais #####
### Ex 5:
##idade = int(input("digite sua idade: "))
##salario = float(input("digite seu salário: "))
##sexo = input("digite seu sexo [f/m/o]: ")
####if idade < 0 or idade > 150:
####    print('ERRO')
####if idade > 0 and idade < 150:
####    print("OK")
##if 0 < idade < 150:
##    print("OK")
##else:
##    print("ERRO")
##if salario > 0:
##    print("OK")
##else:
##    print("ERRO")
####if sexo == 'f' or sexo == 'm' or sexo == 'o':
####    print("OK")
##if sexo != 'f' and sexo != 'm' and sexo != 'o':
##    print("ERRO")
##else:
##    print("OK")

##### Lógica booleana
##print(True and True)
##print(True and False)
##print(True or False)
##print(False or True and False)
##print(True or False and True)
##print(False or False and True)
##print(True or False and False)
##print((True or False) and False)


##### desafio 2
##n1 = int(input())
##n2 = int(input())
##n3 = int(input())
##n4 = int(input())
####if n1>=n2 and n1>=n3 and n1>= n4:
####    print(n1)
##maior = n1
##if n2 > maior:
##    maior = n2
##if n3 > maior:
##    maior = n3
##if n4 > maior:
##    maior = n4
##print(maior)

### revisão while
### lista - while
##### ex 1:
##n = int(input())
##contador = 0
##while contador < n:
##    print(contador+1, end = ' ')
##    contador = contador + 1

### ex 2:
##n = int(input())
##contador = 0
##soma = 0
##while contador < n:
##    soma += contador + 1 # soma = soma + contador + 1
##    contador += 1 # contador = contador + 1
##print(soma)

### ex 4:
##contador = 0
##while contador < 10:
##    contador += 1
##    print("9x{:02} = {:02}".format(contador, contador*9))

### ex 6:
soma = 0
while True:
    n = int(input())
    soma += n
    if n == 0:
        break
print(soma)

##### desafio 1
### 1 + 1\2 + 1\4 + ...
##termo = 1
##contador = 0
##soma = 0
##while contador < 20:
##    soma = soma + termo # soma += termo
##    termo = termo/2 # termo /= 2
##    contador += 1
##print("{:.10f}".format(soma))

### desafio 2










    




    
    









    









    


















    












