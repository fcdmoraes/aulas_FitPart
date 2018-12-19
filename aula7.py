### API
## json - java script object notation
## "{'keyword': valor}"

### web crawler
## html

# cmd: pip install requests
# terminal: pip3 install requests

import requests
import time
import csv

chave = 'TN1GWKC8BTNTPZ7P'
# fc = "USD"
# tc = "BRL"
# url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(fc,tc,chave)
# r = requests.get(url)

# print(r)
# print(r.text)
# json = r.json()
# # print(json)
# print(json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

def cambio(fc,tc):
	url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(fc,tc,chave)
	r = requests.get(url)
	json = r.json()
	# print(r.text)
	print(fc,tc)
	try:
		return (json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
	except:
		return 'Deu ruim'

# x = cambio('USD','BRL')
# print(x)
# moedas = ['USD','EUR','BTC','KRW','JPY']
# for moeda in moedas:
# 	x = cambio(moeda,'BRL')
# 	print(x)

# while True:
# 	x = cambio('USD','BRL')
# 	print(x)
# 	time.sleep(5)

def cartoes(ini,fim,pag):
	url = "http://www.transparencia.gov.br/api-de-dados/cartoes?mesExtratoInicio={}&mesExtratoFim={}&pagina={}".format(ini,fim,pag)
	r = requests.get(url)
	return r.json()

# x = cartoes('10/2017','11/2017',1)
# # print(x)
# print(len(x))
# print(x[0]["valorTransacao"])
# print(x[0]["estabelecimento"]["nome"])
# print(x[0]["portador"]["nome"])

pagina = 1
valores = []
estabelecimentos = []
nomes = []
lista = []
while pagina < 3:
	x = cartoes('10/2017','11/2017', pagina)
	pagina += 1
	if x == []:
		break
	for gasto in x:
		valor = gasto['valorTransacao'].replace('.','').replace(',','.')
		estabelecimento = gasto["estabelecimento"]["nome"]
		nome = gasto["portador"]["nome"]
		valores.append(float(valor))
		estabelecimentos.append(estabelecimento)
		nomes.append(nome)
		dic = {'nome': nome, 'valor': valor, "estabelecimento": estabelecimento}
		lista.append(dic)
	print(pagina)
	file = open('cartoes.csv', 'w')
	escritor = csv.DictWriter(file, fieldnames=['nome','valor','estabelecimento'], lineterminator = '\n')
	escritor.writeheader()
	escritor.writerows(lista)
	file.close()
print(max(valores))



