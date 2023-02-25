from bs4 import BeautifulSoup
import requests
import re

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
        'image_Link' : '',
    }
    
    product_page = items.find('a', {'class': 'grid-product__link'})
    image_likn = items.find('')

    Kappa[item_name]['product_Link'] = KAPPA_PRODUCT + (product_page['href'])
    price_span = items.find("div", {"class": "grid-product__price"})
    price_span = price_span.text.strip()
    pattern = r"\$\d+\.\d{2}"
    matches = re.findall(pattern, price_span)
    
    Kappa[item_name]['original_Price'] = matches[0]
    Kappa[item_name]['discounted_Price'] = matches[1]
    Kappa[item_name]['discounted_Percentage'] = str(int(round (float(matches[0][1:len(matches[0])]) / float(matches[1][1:len(matches[1])]) -1, 2) * 100)) + '%' 
    


print (Kappa)
