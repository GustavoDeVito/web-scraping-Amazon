from bs4 import BeautifulSoup
from selenium import webdriver

from config import driver_path

data_amazon = []

def get_url(search):
    url = 'https://www.amazon.com.br/s?k={}&ref=nb_sb_noss_1'
    search = search.replace(' ', '+')
    return url.format(search)

driver = webdriver.Edge(executable_path=driver_path)

driver.get(url=get_url('placa de video'))

soup = BeautifulSoup(driver.page_source, 'html.parser')

element = soup.find_all('div', {'data-component-type':'s-search-result'})[0]

img_product = element.find('span', {'data-component-type':'s-product-image'}).find('img')['src']

name_product = element.find('h2').find('span').text

price_product = element.find('span', class_='a-price').find('span', class_='a-offscreen').text

driver.quit()

data_amazon.append({
    'img': img_product,
    'name': name_product,
    'price': price_product,
})

print(data_amazon)