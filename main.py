import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

# importando a pagina como texto
resposta = requests.get(url)
#print(resposta.text)

# transformando o texto e criando html para fazer raspagem
html = BeautifulSoup(resposta.text, 'html.parser')
#print(html)

# criando laço para pegar perguntas, data e votos
for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    # como a class foi igual para mais de uma classe, puxamos a informação pelo índice
    votos = pergunta.select('.s-post-summary--stats-item-number')[0]
    respostas = pergunta.select('.s-post-summary--stats-item-number')[1]
    visitas = pergunta.select('.s-post-summary--stats-item-number')[2]
    print(f'Pergunta: {titulo.text}')
    print(f'Data: {data.text}')
    print(f'Votos: {votos.text}')
    print(f'Respostas: {respostas.text}')
    print(f'Visitas: {visitas.text}\n')
