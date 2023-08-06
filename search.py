import json
from bs4 import BeautifulSoup
import cloudscraper as cs
scraper = cs.create_scraper()

def search(query: str):
    url = f"https://mlwbd.media/?s={query}"
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_items = []

        for item in soup.find_all('div', {'class': 'result-item'}):
            title = item.find('div', {'class': 'title'}).text.strip()
            link = item.find('a')['href']
            image = item.find('img')['src']

            search_item = {
                'title': title,
                'link': link,
                'image': image,
            }

            search_items.append(search_item)

        return json.dumps(search_items, ensure_ascii=False)
    else:
        print(f"Failed to fetch the search results. Status Code: {response.status_code}")
        return "[]"