# import aula9
from aula9 import *
import tkinter as tk
import csv

# Funcionario('Jair', 12000, 63, 17)

# print(Funcionario.lista)

root = tk.Tk()

def criar():
	Funcionario(nome.get(), float(salario.get()), int(idade.get()), Funcionario.numero)
	print(Funcionario.lista)

def salvar():
	lista = []
	for func in Funcionario.lista:
		dicionario = {}
		dicionario['nome'] = func.nome
		dicionario['salario'] = func.salario
		dicionario['idade'] = func.idade
		dicionario['id'] = func.id
		lista.append(dicionario)
	
	header = ['nome','salario','idade','id']
	file = open('funcionarios.csv', 'w')
	escritor = csv.DictWriter(file, fieldnames = header, lineterminator = '\n')
	escritor.writeheader()
	escritor.writerows(lista)
	file.close()

def importar():
	file = open('funcionarios.csv', 'r')
	leitor = list(csv.DictReader(file))
	file.close()

	for func in leitor:
		nome = func['nome']
		salario = func['salario']
		idade = func['idade']
		registro = func['id']
		Funcionario(nome, salario, idade, registro)
	print(Funcionario.lista)

tk.Label(root, text = 'Nome:').pack()
nome = tk.Entry(root)
nome.pack()

tk.Label(root, text = 'Salario:').pack()
salario = tk.Entry(root)
salario.pack()

tk.Label(root, text = 'Idade:').pack()
idade = tk.Entry(root)
idade.pack()

tk.Button(root, text = 'Criar', command = criar).pack()

tk.Button(root, text = 'Salvar', command = salvar).pack()

tk.Button(root, text = 'Importar', command = importar).pack()

root.mainloop()