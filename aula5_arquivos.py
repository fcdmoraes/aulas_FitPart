"""escrevendo um arquivo"""
# file = open('aula5.txt', 'w', encoding = 'utf8')
# # file = open('aula5.txt', 'a', encoding = 'utf8')

# file.write("texto1\n")
# file.write("texto2\n")
# file.write("texto3")

# file.close()

"""lendo um arquivo"""
# file = open('aula5.txt', 'r', encoding = 'utf8')

# # texto = file.read()
# # linha = file.readline()
# # print(linha)
# # linha = file.readline()
# # print(linha)

# for linha in file:
# 	print(linha)

# file.close()


"""trabalhando com csv"""
import csv
file = open('MSFT.csv', 'r', encoding = 'utf8')
leitor = csv.reader(file, delimiter = ',')
matriz = list(leitor)
file.close()

print(matriz[0])

file = open('MSFT(2).csv', 'w', encoding = 'utf8')

escritor = csv.writer(file)
escritor.writerows(matriz)

file.close()