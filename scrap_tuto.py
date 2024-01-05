import requests
import csv
from bs4 import BeautifulSoup
# Adresse du site Internet 
url = "http://quotes.toscrape.com/"
# commande get
response = requests.get(url)
# Parse 
html = BeautifulSoup(response.text,'html.parser')
# extraire
quotes_html = html.find_all('span',class_="text")
authors_html = html.find_all('small',class_="author")
# assembl as list
quotes = list()
for quote in quotes_html:
	quotes.append(quote.text)
authors = list()
for author in authors_html:
	authors.append(author.text)
for t in zip(quotes,authors):
	print(t)
