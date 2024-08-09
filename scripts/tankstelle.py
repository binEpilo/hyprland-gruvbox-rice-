#!/bin/python

# imports

import requests, re
from bs4 import BeautifulSoup

# scraper einrichten

#die auskommentierte line ist ohne onlinegebrauch
html = requests.get("https://www.benzinpreis-aktuell.de/86650-wemding-aktuelle-dieselpreise?umkreis=0")

soup = BeautifulSoup(html.content, 'html.parser')

# dieses re zeug sorgt dafür, dass einfach irgendeine klasse mit dem gegebenen beginn gefunden wird
try:
    tankstelle_esso = soup.find(class_=re.compile(r'ns_newsquare ns_tsa ns_tstype_esso ns_count_\d+')).find(class_="ns_price tfx4").find('i').find('i').find('i')

    span = tankstelle_esso.find('span')
    span.decompose()

    preis = tankstelle_esso.get_text()

    print(f"{preis}€/l")
except AttributeError:
    print("Closed!")
