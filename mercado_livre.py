import requests
from bs4 import BeautifulSoup
import re
import os
import time

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

url_base = 'https://lista.mercadolivre.com.br/'

def buscarProduto():
    produto_nome = input('Qual produto você deseja procurar? ' + RED)
    print(RESET)
    print('Buncando resultados...')
    time.sleep(1)
    os.system('clear')
    print('Resultados de: ' + RED + produto_nome + RESET)

    for i in range(0, len(produto_nome)):
        produto_nome = re.sub(' ', '-', produto_nome)

    response = requests.get(url_base + produto_nome)

    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('div', attrs={'class': 'andes-card'})


    for produto in produtos:
        print('\n')

        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

        link = produto.find('a', attrs={'class': 'ui-search-link'})

        simbolo = produto.find('span', attrs={'class': 'price-tag-symbol'})
        preco = produto.find('span', attrs={'class': 'price-tag-fraction'})
        separador = produto.find('span', attrs={'class': 'price-tag-decimal-separator'})
        cents = produto.find('span', attrs={'class': 'price-tag-cents'})

        if(simbolo and preco and separador and cents):
            titulo = titulo.text
            link = link['href']
            valor = simbolo.text + preco.text + separador.text + cents.text

            print(BOLD + 'Produto: ', BLUE + titulo + RESET)
            print(BOLD + 'Link do produto: ', CYAN + link + RESET)
            print(BOLD + 'Preço do produto: ', GREEN + valor + RESET)

        elif(simbolo and preco):
            titulo = titulo.text
            link = link['href']
            valor = simbolo.text + preco.text

            print(BOLD + 'Produto: ', BLUE + titulo + RESET)
            print(BOLD + 'Link do produto: ', CYAN + link + RESET)
            print(BOLD + 'Preço do produto: ', GREEN + valor + RESET)

        else:
            titulo = titulo.text
            link = link['href']

            print(BOLD + 'Produto: ', BLUE + titulo + RESET)
            print(BOLD + 'Link do produto: ', CYAN + link + RESET)
            print(BOLD + 'Preço do produto: ', RED + 'NaN' + RESET)

        print('\n')


while True:
    buscarProduto()
    a = input('Pressione '+ RED +'Enter'+ RESET +' para uma nova busca! Ou '+ RED +'Digite'+ RESET +' qualquer coisa para finalizar: \n')
    os.system('clear')

    if(a != ''):
        break