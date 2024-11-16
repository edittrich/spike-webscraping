from bs4 import BeautifulSoup
from selenium import webdriver


def scraper(page_source):
    soup = BeautifulSoup(page_source, 'lxml')
    print(soup.prettify())

    return


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("https://arztsuchehessen.de/")
page_source = driver.page_source

scraper(page_source)

driver.quit()
