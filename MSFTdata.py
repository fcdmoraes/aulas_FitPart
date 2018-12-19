import requests
"""programa para pegar dados da MSFT na NASDAQ"""
def get_data():
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo'

  r = requests.get(url)

  d = (r.json()["Time Series (5min)"])

  matriz = []
  for data in d:
    dados = d[data]
    linha = [data,dados['1. open'],dados['2. high'],dados['3. low'],dados['4. close'],dados['5. volume']]
    matriz.append(linha)

  return matriz