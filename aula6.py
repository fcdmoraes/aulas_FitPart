# dicionario = {"python": "linguagem de programação de alto nível",
#  "sublime": "IDE para programação"}

# print(dicionario)
# print(dicionario['sublime'])

# dicionario['cobol'] = "linguagem de programação de baixo nível"

# print(dicionario)

# for x in dicionario:
# 	print(x)
# 	print(dicionario[x])

# del(dicionario['cobol'])
# print(dicionario)

import csv
import tkinter
from tkinter import filedialog, messagebox

janela = tkinter.Tk()
janela.withdraw()


def abrir():
	global leitor
	nome = filedialog.askopenfilename()
	# print(nome)
	# janela.mainloop()
	file = open(nome, 'r')
	leitor = csv.DictReader(file)
	leitor = list(leitor)
	# print(leitor)
	file.close()


matriz1 = []
matriz2 = []
matriz3 = []
def get_data():
	for linha in leitor:
		dicionario = {}
		# print(linha['Position Type Description'])
		if linha['Position Type Description'].upper() == "CASH":
			# print('Cash:', linha['Market Value / Net Equity (USD)'], 
			# 	'Conta:', linha['Sub Account Number'])
			print('Cash: {Market Value / Net Equity (USD)} - Conta: {Sub Account Number}'.format(**linha))
			dicionario['Cash'] = linha['Market Value / Net Equity (USD)']
			dicionario['Conta'] = linha['Sub Account Number']
			matriz1.append(dicionario)
		elif linha['Position Type Description'].upper() == "EQUITY SWAP":
			if linha["Issue Currency"] != "USD":
				print("Currency: {Swap Currency} - Rate: {Fx Rate Issue To USD}".format(**linha))
				dicionario['Currency'] = linha['Swap Currency']
				dicionario['Rate'] = linha['Fx Rate Issue To USD']
				matriz2.append(dicionario)
		elif linha['Position Type Description'].upper() == "INTEREST RATE SWAP":
			price = abs(float(linha["Price (USD)"])/100)
			print("Sec. Desc.: {} - Price: {}".format(linha["Security Description"], price))
			dicionario["Security Description"] = linha["Security Description"]
			dicionario["Price"] = price
			matriz3.append(dicionario)
		# matriz.append(dicionario)

# print(matriz)
def save(nome, matriz, fieldnames):
	file = open(nome, 'w')
	# fieldnames = ['Cash', 'Conta', 'Currency', 'Rate', 'Security Description', 'Price']
	escritor = csv.DictWriter(file, fieldnames, lineterminator='\n')
	escritor.writeheader()
	escritor.writerows(matriz)
	file.close()

try:
	abrir()
	get_data()
	save('output1.csv', matriz1, ['Cash', 'Conta'])
	save('output2.csv', matriz2, ['Currency', 'Rate'])
	save('output3.csv', matriz3, ['Security Description', 'Price'])
	messagebox.showinfo('ok','arquivos criados com sucesso')
except:
	messagebox.showerror('not ok', 'Problema com o arquivo')

# file = open('output1.csv', 'w')
# fieldnames = ['Cash', 'Conta']
# escritor = csv.DictWriter(file, fieldnames, lineterminator='\n')
# escritor.writeheader()
# escritor.writerows(matriz1)
# file.close()

# file = open('output2.csv', 'w')
# fieldnames = ['Currency', 'Rate']
# escritor = csv.DictWriter(file, fieldnames, lineterminator='\n')
# escritor.writeheader()
# escritor.writerows(matriz2)
# file.close()

# file = open('output3.csv', 'w')
# fieldnames = ['Security Description', 'Price']
# escritor = csv.DictWriter(file, fieldnames, lineterminator='\n')
# escritor.writeheader()
# escritor.writerows(matriz3)
# file.close()