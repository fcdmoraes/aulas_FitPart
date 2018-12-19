import requests
from bs4 import BeautifulSoup
import csv

# url = "https://lista.mercadolivre.com.br/"

# r = requests.get(url)
# print(r)

# print(r.text)
# soup = BeautifulSoup(r.text, 'html.parser')

# # print(soup.prettify())
# # print(soup.head)
# head = soup.head
# # print(head.title)
# titulo = head.title
# print(titulo.get_text())
def busca(produto):
	url = "https://lista.mercadolivre.com.br/"+produto
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	# link = soup.find('a', class_="item__info-link")
	# print(link.prettify())
	# print(link['href'])
	links = soup.find_all('a', class_="item__info-link")
	# print(links)
	lista_produtos = []
	for link in links:
		# print(link['href'])
		end = link['href']
		preco = link.find('span', class_='price__fraction').get_text()
		dic = {'endereço': end, 'preço': preco}
		lista_produtos.append(dic)
	return (lista_produtos)

def busca2(url):
	# url = "https://lista.mercadolivre.com.br/"+produto
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	conteiners = soup.find_all('div', class_='item__info') # <- arrumar aqui
	# lista_produtos = []
	try:
		for cont in conteiners:
			link = cont.find('a', class_='item__info-title')
			end = link['href']
			preco = cont.find('span', class_='price__fraction').get_text()# <- arrumar aqui
			dic = {'endereço': end, 'preço': preco}
			lista_produtos.append(dic)
		prox = soup.find('li', class_='andes-pagination__button--next')
		link_prox = prox.a['href']
		print(link_prox)
		busca2(link_prox)
	except:
		return (lista_produtos)

lista_produtos = []
busca2('https://lista.mercadolivre.com.br/geladeira')
lista = lista_produtos

file = open('ml2.csv', 'w', encoding='utf8')
escritor = csv.DictWriter(file, fieldnames = ['preço','endereço'], lineterminator='\n')
escritor.writeheader()
escritor.writerows(lista)
file.close()