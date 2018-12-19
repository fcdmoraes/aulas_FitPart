from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import smtplib
import getpass

# my_pass = getpass.getpass('Digite sua senha: ')

my_email = 'flavio.moraes.lc@gmail.com'
my_pass = 'programar123'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(my_email, my_pass)

def send_email(noticia):
	assunto = noticia['titulo']
	texto = noticia['texto']
	destinatario = 'flavio.moraes.lc@gmail.com'
	msg = 'Subject: {}\n\n**{}**\n\n{}'.format(assunto, assunto, texto)
	msg = msg.encode('utf8')
	server.sendmail(my_email, destinatario, msg)


path = os.getcwd() # pegando o diretório em que o __main__ está salvo -> ex: C:\Desktop
path = os.path.join(path,"chromedriver.exe") # juntar o diretório com o chromedriver.exe -> C:\Desktop\chromedriver.exe 
print(path)
driver = webdriver.Chrome(path)
# url = 'https://www.valor.com.br'
# driver.get(url)

# driver.find_element_by_id('login-valor').click()

# time.sleep(5)
# iframes = driver.find_elements_by_tag_name('iframe')
# print(len(iframes))

# iframe = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(iframe)

# url = 'https://login.globo.com/login/6668?url=&tam=WIDGET'
# driver.get(url)

# login = driver.find_element_by_id('login')
# password = driver.find_element_by_id('password')

# login.send_keys('login@email.com')
# password.send_keys('minha senha')
# password.submit()

url = "https://www.valor.com.br/impresso"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
noticias = soup.find_all('a', class_ = 'valor-impresso-indice-node-title')

lista_noticias = []
for noticia in noticias:
	titulo = (noticia.get_text())
	link = "https://www.valor.com.br" + noticia['href']
	lista_noticias.append({"titulo": titulo, 'link': link})

# for i in range(len(lista_noticias)):
for i in range(2):
	url = lista_noticias[i]["link"]
	# print(url)
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	texto = soup.find('div', id = "node-body").get_text()
	lista_noticias[i]["texto"] = texto
	send_email(lista_noticias[i])
	# print(texto)

for i in range(2):
	print(lista_noticias[i]['texto'])
	print('\n')

server.quit()
driver.quit()
