import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }


def get_html(url):
    response = requests.get(url, headers=headers)
    return response.text


def parse_ya(text):
    url = ''
    html = get_html(url)
    soup = BeautifulSoup(html)
    try:
        answer = soup.find('div', {'class': 'fact-answer typo typo_text_l typo_line_m fact__answer'}).text
    except AttributeError:
        answer = "Error"
    return answer
