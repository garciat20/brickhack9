import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# create a connection to the PostgreSQL database
# engine = create_engine('postgresql://brickhack9:brickhack9@localhost:5432/brickhack9')

# fetch data from the webpage
URL = "https://kappa-usa.com/collections/mens-sale"
response = requests.get(URL)
soup =  BeautifulSoup(response.content, 'html.parser')
clothes = soup.find_all('div', {'data-aos': 'row-of-4'})

# parse the data and store it in a dictionary
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
    image_link = items.find('img', {'class': 'grid-product__image'})
    image_link = 'https:' + (image_link['data-src']).replace('{width}',str(180))
    Kappa[item_name]['image_Link'] = image_link
    
    Kappa[item_name]['product_Link'] = 'https://kappa-usa.com' + (product_page['href'])
    price_span = items.find("div", {"class": "grid-product__price"})
    price_span = price_span.text.strip()
    pattern = r"\$\d+\.\d{2}"
    matches = re.findall(pattern, price_span)
    Kappa[item_name]['original_Price'] = matches[0]
    Kappa[item_name]['discounted_Price'] = matches[1]
    Kappa[item_name]['discounted_Percentage'] = str(int(round(float(matches[0][1:len(matches[0])]) / float(matches[1][1:len(matches[1])]) -1, 2) * 100)) + '%'

# convert the dictionary to a pandas DataFrame
clothing_info = pd.DataFrame.from_dict(Kappa, orient='index')
clothing_info.index.name = 'ProductName'
clothing_info.reset_index(inplace=True)
clothing_info.rename(columns={'product_Link': 'ProductPage',
                              'original_Price': 'OriginalPrice',
                              'discounted_Price': 'DiscountedPrice',
                              'discounted_Percentage': 'DiscountRate',
                              'image_Link': 'ImageLink'},
                     inplace=True)

# write the DataFrame to a SQL file
with open('src/db/clothing_info.sql', 'w') as f:
    f.write("DROP TABLE IF EXISTS buddy_table; \n")
    f.write(f"CREATE TABLE buddy_table (")
    for i, column in enumerate(clothing_info.columns):
        f.write(f"{column} ")
        if i != len(clothing_info.columns) - 1:
            f.write("VARCHAR(255), ")
        else:
            f.write("VARCHAR(255));\n\n")
    
    for index, row in clothing_info.iterrows():
        f.write(f"INSERT INTO buddy_table (ProductName, ProductPage, OriginalPrice, DiscountedPrice, DiscountRate, ImageLink)VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}');\n")
        
print(clothing_info)
