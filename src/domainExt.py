import requests
from bs4 import BeautifulSoup

def domain():
    res = requests.get('https://mlwbd.com')
    soup = BeautifulSoup(res.text, 'html.parser')
    returnData = soup.find('a', {'class': 'btn-solid-lg page-scroll'})
    domainName = returnData['href'].split('.')
    return domainName[1]

domainExt = str(domain())

# print(domainExt)