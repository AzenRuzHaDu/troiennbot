import requests
from bs4 import BeautifulSoup
import random

r = requests.get('https://br.m.wikiquote.org/wiki/Krennlavario%C3%B9_ha_troio%C3%B9-lavar_brezhonek')

soup = BeautifulSoup(r.content, 'html.parser')

titres = []
titres_S = []

t = soup.find_all('span', class_="mw-headline")
for i in t:
    titres.append(i.text)
titres.append("Troienn")

#put "$" before elements of the list
K = "$"
titres_S = [K + x for x in titres]


def user_interact(query_user):

    if query_user == "$Troienn":
        num_query_user = random.randint(1, 37)

    else:
        if not query_user in titres_S:
            return "error"
        num_query_user = titres_S.index(query_user) + 1

    c = soup.find('section', id=f'mf-section-{num_query_user}')

    li = c.find_all("li")
    return random.choice(li).text
