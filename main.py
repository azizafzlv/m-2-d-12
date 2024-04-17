import requests 
from bs4 import BeautifulSoup


base_url = 'https://dominopizza.ru/'
response = requests.get(base_url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

novinki = soup.find('div', {'id': 'novinki'})
novinki_pizza = novinki.find_all('div', {'class': 'col'})

pizza_list = []

for pizza in novinki_pizza:
    pizza_content = pizza.a.div.find('div', {'class': 'product-card-content'})
    pizza_content_name = pizza_content.find('div', {'class': 'product-name'})
    pizza_content_description = pizza_content.find('div', {'class': 'description-container'})
    pizza_content_price = pizza_content.find('div', {'class': 'price'})
    
    pizza_picture = pizza.a.div.find('div', {'class': 'product-picture'})
    pizza_list.append({
        'name': pizza_content_name.get_text(),
        'description': pizza_content_description.get_text(),
        'price': pizza_content_price.get_text(),
        'picture_url': pizza_picture.picture.img.get('src')
        })

print('Новинки')    
for pizza in pizza_list:
    print('--------------------------------')
    print(f'Название: {pizza["name"]}')
    print(f'Состав: {pizza["description"]}')
    print(f'Цена: {pizza["price"]}')
    print(f'Ссылка до картинки: {pizza["picture_url"]}')
    print('--------------------------------')



