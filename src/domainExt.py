import requests
from bs4 import BeautifulSoup

def get_domain():
    try:
        res = requests.get('https://mlwbd.com')
        soup = BeautifulSoup(res.text, 'html.parser')
        returnData = soup.find('a', {'class': 'btn-solid-lg page-scroll'})
        domainNamehref = returnData["href"]
        domainSplit = domainNamehref.split(".")
        domain_name = domainSplit[1].split('/')[0]
        return domain_name
    except Exception as e:
        return print(e)