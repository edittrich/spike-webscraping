from bs4 import BeautifulSoup

with open('data/in/Arztsuche1.mhtml', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'lxml')
title = soup.title.string
print(f"Title of the HTML document: {title}")
