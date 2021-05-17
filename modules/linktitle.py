from bs4 import BeautifulSoup
import requests
def get_title(link):
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.title:
        return soup.title.string
    else:
        return 'COULD NOT GET TITLE, YOU CAN OPEN LINK TO SEE WHAT IS IN IT'
    
    