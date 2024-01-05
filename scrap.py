import requests
import csv
import urllib3
from bs4 import BeautifulSoup
# Adresse du site Internet 
url = "https://www.leboncoin.fr/recherche?category=10&text=appartement&locations=Grenoble_38000__45.19397_5.73206_4752&owner_type=private&real_estate_type=2&square=50-max&price=700-1300&rooms=2-4"
# commande get
#headers={'User-Agent':'Mozilla/5.0 (X11; Linux) Applewebkit(537.36(KHTML, like Gecko) Chromiun/78.0.3904.108'}
#headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101) Firefox/5.0'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}
http=urllib3.PoolManager()
resp = http.request("GET",url,headers=headers)
#response = urllib3.request("GET",url, headers=headers)
print(resp.status)
#response = requests.get(url, params={'g':'raspberry pi'})
print(resp)
print()



