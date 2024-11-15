from bs4 import BeautifulSoup
from lxml import etree

with open('data/in/test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'lxml')
title = soup.title.string
print(f"Title of the HTML document: {title}")
paragraphs = soup.find_all('p')
for idx, p in enumerate(paragraphs, start=1):
    print(f"Paragraph {idx}: {p.text.strip()}")
