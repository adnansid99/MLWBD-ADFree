import requests
from bs4 import BeautifulSoup

def domain():
    res = requests.get('https://mlwbd.com')
    soup = BeautifulSoup(res.text, 'html.parser')
    returnData = soup.find('a', {'class': 'btn-solid-lg page-scroll'})
    domainNamehref = returnData["href"]
    domainSplit = domainNamehref.split(".")
    return domainSplit[1]

# print(domain())