import requests

def get_domain():
    res = requests.get('https://densehospitableellipse.adnansidd99.repl.co')
    domainName = res.json()['domain']
    return domainName