import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        title = tag.get_text(strip=True)
        if title:
            headlines.append({"title": title})
    
    return headlines

def headline_generator(headlines):
    for headline in headlines:
        yield headline

if __name__ == "__main__":
    url = "https://www.bbc.com/news"  
    headlines = scrape(url)

    if headlines:
        print("\nTop Headlines:\n")
        for h in headline_generator(headlines[:10]):  
            print(f"- {h['title']}")
