import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('uni-names.csv', 'w'))
f.writerow(['Name', 'Link'])


page = requests.get('https://www.4icu.org/pk/pakistani-universities.htm')

soup = BeautifulSoup(page.text, 'html.parser')


uni_name_list = soup.find('tbody')

uni_name_list_items = uni_name_list.find_all('a')

for uni_name in uni_name_list_items:
    names = uni_name.contents[0]
    links = 'https://web.archive.org' + uni_name.get('href')
    f.writerow([names, links])
