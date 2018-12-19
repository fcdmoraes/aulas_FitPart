# import blpapi
# import os
# import sys

# # Pegando o diretório em que o arquivo está salvo
# diretorio = os.getcwd()
# # Adiciona a pasta do blpapi nessa pasta
# diretorio = os.path.join(diretorio, "blpapi_cpp_3.12.2.1")
# # Adiciona o bin no nome do diretorio
# diretorio = os.path.join(diretorio, "bin")

# print(diretorio)

# # Inserindo o diretorio no path do sistema
# sys.path.insert(0, diretorio)

# print(sys.path)

import blpapi

# cria um objeto para configurar as opções da sessão
options = blpapi.SessionOptions()
# IP de quem vai hospedar o servidor
options.setServerHost('192.168.1.48')
# Definir a porta de acesso
options.setServerPort(8194)

# cria um objeto para a sessão
session = blpapi.Session(options)

# iniciando a sessão
if not session.start():
	print("Erro ao iniciar a sessão")

try:
	# Abrindo um serviço que registra os acessos de API da bloomberg
	if not session.openService("//blp/refdata"):
		print("Falha ao abrir o serviço")

	# Acessando o registro de acessos da API da bloomberg
	refDataService = session.getService("//blp/refdata")

	# Montamos a requisição
	request = refDataService.createRequest("HistoricalDataRequest")
	request.getElement("securities").appendValue("IBM US Equity")
	request.getElement("securities").appendValue("MSFT US Equity")
	request.getElement("fields").appendValue("PX_LAST")
	request.getElement("fields").appendValue("OPEN")
	request.set("periodicityAdjustment", "ACTUAL")
	request.set("periodicityAdjustment", "DAILY")
	request.set("startDate", "20181125")
	request.set("endDate", "20181126")
	request.set("maxDatePoints", 100)

	session.sendRequest(request)

	# Imprimimos cada mensagem da resposta
	while(True):
		ev = session.nextEvent(500)
		for msg in ev:
			print(msg)

		if ev.eventType() == blpapi.Event.RESPONSE:
			break
except:
	pass




