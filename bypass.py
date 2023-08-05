import requests
import cloudscraper as cs

scraper = cs.create_scraper()

def extract_data_between_strings(input_string, left_string, right_string):
    left_index = input_string.find(left_string)
    if left_index == -1:
        return None

    left_index += len(left_string)

    right_index = input_string.find(right_string, left_index)
    if right_index == -1:
        return None

    return input_string[left_index:right_index]

def main(URLx):
    response = scraper.get(URLx)
    
    token = extract_data_between_strings(response.text, '<input type="hidden" name="FU" value="', '"')

    if token is None:
        print("Failed to extract token. FU1")
        return

    session = requests.Session()

    url = "https://search.technews24.site/blog.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    FU = token
    response = session.post(url,
                            data=f'FU={token}',
                            headers=headers)
    response_text = response.text

    url = extract_data_between_strings(response_text, 'id="verifying-source" action="', '"')
    fu2 = extract_data_between_strings(response_text, 'name="FU2" value="', '"')

    if url is None or fu2 is None:
        print("Failed to extract URL or FU2.")
        return

    content = f"FU2={fu2}"
    response = session.post(url, data=content, headers=headers)
    response_text = response.text

    # Parse response for FU4
    fu2 = extract_data_between_strings(response_text, 'name="FU2" value="', '"')

    # Third request
    url = "https://freethemesy.com/"
    content = f"FU2={fu2}"
    response = session.post(url, data=content, headers=headers)
    response_text = response.text

    # Parse response for FU5
    fu3 = extract_data_between_strings(response_text, 'name="FU3" value="', '"')

    # Fourth request
    url = "https://freethemesy.com/top-6-health-benefits-of-meditation/"
    content = f"FU3={fu3}"
    response = session.post(url, data=content, headers=headers)
    response_text = response.text

    # Fifth request
    fu4 = extract_data_between_strings(response_text, 'name="FU4" value="', '"')
    url = "https://freethemesy.com/career-guide-software-development-for-your-bright-future/"
    content = f"FU4={fu4}"
    response = session.post(url, data=content, headers=headers)
    response_text = response.text
    final_Url = extract_data_between_strings(response_text, """<div class="card" id="lastlink"> </div>
<br>
<div class="topnav">""", '</div>')
    return final_Url


# print(main('https://mlwbd.love/movie/hidayah-2023/'))