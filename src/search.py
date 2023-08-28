import json
from bs4 import BeautifulSoup
import cloudscraper as cs
from main import domainExt
scraper = cs.create_scraper()

def search(query: str):
    url = f"https://mlwbd.{domainExt}?s={query}"
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_items = []

        for item in soup.find_all('div', {'class': 'result-item'}):
            title = item.find('div', {'class': 'title'}).text.strip()
            link = item.find('a')['href']
            image = item.find('img')['src']
            movie_name = link.split('/')[4]

            search_item = {
                'title': title,
                'link': link,
                'image': image,
                'movie_name': movie_name
            }

            search_items.append(search_item)

        return json.dumps(search_items, ensure_ascii=False)
    else:
        print(f"Failed to fetch the search results. Status Code: {response.status_code}")
        return "[]"