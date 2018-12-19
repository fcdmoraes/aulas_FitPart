class Cavalo(object):
	numero = 0
	def __init__(self, npatas, cor, peso):
		self.npatas = npatas
		self.cor = cor
		self.peso = peso
		# print(self)
		Cavalo.numero += 1

	def engorda(self, dieta):
		print("peso antigo:", self.peso)
		self.peso += dieta
		print("peso atual:", self.peso)

	def __repr__(self):
		return "cor: {}, peso: {}".format(self.cor, self.peso)

# print('numero:', Cavalo.numero)
# pocoto = Cavalo(4, 'marrom', 800)
# pedepano = Cavalo(4, 'branco', 850)
# print('numero:', Cavalo.numero)

# print(pocoto.cor)
# print(pedepano.cor)
# print(pocoto)
# print(pedepano)

# pocoto.engorda(30)
# pedepano.engorda(20) # Cavalo.engorda(pedepano, 20)

# pocoto.crina = 'cinza'
# print(pocoto.crina)
# # print(pedepano.crina)
# # print(dir(pocoto))
# print(pocoto)
# print(pedepano)

# print(dir(Cavalo))

class Funcionario(object):
	numero = 0
	lista = []

	def __init__(self, nome, salario, idade, registro):
		self.nome = nome
		self.salario = salario
		self.idade = idade
		self.id = registro
		Funcionario.numero += 1
		Funcionario.lista.append(self)

	def __repr__(self):
		# return "{},{},{}".format(self.nome, self.idade, self.salario)
		return self.nome

	def busca_id(registro):
		for objeto in Funcionario.lista:
			if objeto.id == registro:
				return objeto

	def busca_nome(nome):
		for objeto in Funcionario.lista:
			if objeto.nome == nome:
				return objeto

	def aumento(nome = None, registro = None, bonus = 0):
		if nome != None:
			objeto = Funcionario.busca_nome(nome)
		else:
			objeto = Funcionario.busca_id(registro)
		objeto.salario += bonus

if __name__ == '__main__':
	Funcionario('Osmar', 1500, 19, 0)
	Funcionario('Carlos', 2200, 21, 1)
	Funcionario('Beatriz', 2500, 20, 2)

	print(Funcionario.lista)

	f2 = Funcionario.busca_id(2)
	print(f2.salario)

	Funcionario.aumento(nome = 'Osmar', bonus = 200)
	osmar = Funcionario.busca_nome('Osmar')
	print(osmar.salario)