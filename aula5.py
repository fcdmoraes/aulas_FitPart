# def f(x):
# 	return x*x+3

# def soma(x,y):
# 	print(x+y)
# 	return x + y

# # print(f(1))
# # print(f(3))
# # print(soma(3,6))
# z = soma(3,7)
# print(z)

# lista = []
# x = lista.append(3)

# print(lista)
# print(x)

# x = print(10)
# print(x)

# x = int(1.5)
# print(x)

import MSFTdata

matriz = MSFTdata.get_data()

def get_column(dia,mes,col):
	data = "2018-{}-{}".format(mes,dia)
	lista1 = []
	for linha in matriz:
		if data in linha[0]:
			lista1.append(linha[col])
	return lista1

def print_list(lista):
	for elemento in lista:
		print(elemento)

def save_list(lista):
	file = open("saida.csv", 'w', encoding = 'utf8')
	for elemento in lista:
		file.write(elemento)
		file.write('\n')
	file.close()

def save_matrix(matriz, mes, dia):
	data = "2018-{}-{}".format(mes,dia)
	file = open("MSFT.csv", 'w', encoding = 'utf8')
	for linha in matriz:
		if data in linha[0]:
			for elemento in linha:
				file.write(elemento)
				file.write(',')
			file.write('\n')
	file.close()


x = get_column('28','09',5)
# print_list(x)
save_list(x)
save_matrix(matriz, '09', '28')

# sublista = lista1[0:10]
# print(sublista)