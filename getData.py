from bs4 import BeautifulSoup
import requests
import pandas as pd 
import re
from sqlalchemy import create_engine

engine = engine = create_engine('postgresql://brickhack9:brickhack9@localhost:4999/brickhack9')


URL = "https://kappa-usa.com/collections/mens-sale"
response = requests.get(URL)
KAPPA_PRODUCT = 'https://kappa-usa.com'
# print(response) 
soup =  BeautifulSoup(response.content, 'html.parser')
clothes = soup.find_all('div', {'data-aos': 'row-of-4'})

Kappa = {}

for items in clothes:
    item = items.find('div', {'class':'grid-product__title grid-product__title--body'})
    item_name = item.text
    
    Kappa[item_name] = {
        'product_Link' : '',
        'original_Price' : '',
        'discounted_Price' : '',
        'discounted_Percentage' : '',
        'image_Link' : [],
    }
    
    product_page = items.find('a', {'class': 'grid-product__link'})
    image_link = items.find('img', {'class': 'grid-product__image'})
    image_link = 'https:' + (image_link['data-src']).replace('{width}',str(180))
    Kappa[item_name]['image_Link'].append(image_link)
    
    Kappa[item_name]['product_Link'] = KAPPA_PRODUCT + (product_page['href'])
    price_span = items.find("div", {"class": "grid-product__price"})
    price_span = price_span.text.strip()
    pattern = r"\$\d+\.\d{2}"
    matches = re.findall(pattern, price_span)
    Kappa[item_name]['original_Price'] = matches[0]
    Kappa[item_name]['discounted_Price'] = matches[1]
    Kappa[item_name]['discounted_Percentage'] = str(int(round (float(matches[0][1:len(matches[0])]) / float(matches[1][1:len(matches[1])]) -1, 2) * 100)) + '%'

clothing_info = pd.DataFrame(columns= ['Product Name', 'Product Page', 'Original Price', 'Discounted Price', 'Discount Rate', 'Image Link'])
for clothes in Kappa: 
    print (clothes)
    clothing_info = clothing_info.append({'Product Name': clothes, 'Product page': Kappa[clothes]['product_Link'], 'Original Price': Kappa[clothes]['original_Price'], 'Discounted Price': Kappa[clothes]['discounted_Price'], 'Discount Rate': Kappa[clothes]['discounted_Percentage'], 'Image Link': Kappa[clothes]['image_Link']}, ignore_index = True)

clothing_info.to_sql('Kappa.sql', con=engine)


