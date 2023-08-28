import requests

def domain():
    res = requests.get('https://densehospitableellipse.adnansidd99.repl.co')
    domainExt = res.json()['domain']
    return domainExt

# print(domain())