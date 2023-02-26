import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import os

category = ['mens', 'womens']

Kappa = {}

for i in range(len(category)):
    print(i)
    # fetch data from the webpage
    URL = "https://kappa-usa.com/collections/%s-sale" % category[i]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    clothes = soup.find_all('div', {'data-aos': 'row-of-4'})

    # parse the data and store it in a dictionary
    for items in clothes:
        item = items.find('div', {'class':'grid-product__title grid-product__title--body'})
        item_name = item.text

        Kappa[item_name] = {
            'ProductCategory': '',
            'ProductPage': '',
            'ProductDescription': '',
            'OriginalPrice': '',
            'DiscountedPrice': '',
            'DiscountRate': '',
            'ImageLink': '',
        }
        Kappa[item_name]['ProductCategory'] = category[i]

        product_page = items.find('a', {'class': 'grid-product__link'})
        image_link = items.find('img', {'class': 'grid-product__image'})
        image_link = 'https:' + (image_link['data-src']).replace('{width}',str(180))
        Kappa[item_name]['ImageLink'] = image_link

        Kappa[item_name]['ProductPage'] = 'https://kappa-usa.com' + (product_page['href'])

        response = requests.get('https://kappa-usa.com' + (product_page['href']))
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('div', class_='product-single__description').p.text.strip()
        Kappa[item_name]['ProductDescription'] = (description.replace("'", "''"))

        price_span = items.find("div", {"class": "grid-product__price"})
        price_span = price_span.text.strip()
        pattern = r"\$\d+\.\d{2}"
        matches = re.findall(pattern, price_span)
        Kappa[item_name]['OriginalPrice'] = matches[0]
        Kappa[item_name]['DiscountedPrice'] = matches[1]
        Kappa[item_name]['DiscountRate'] = str(int(round(float(matches[0][1:len(matches[0])]) / float(matches[1][1:len(matches[1])]) -1, 2) * 100)) + '%'

clothing_info = pd.DataFrame.from_dict(Kappa, orient='index')
clothing_info.index.name = 'ProductName'
clothing_info.reset_index(inplace=True)
clothing_info.rename(columns={
    'ProductCategory': 'ProductCategory',
    'ProductName': 'ProductName',
    'ProductPage': 'ProductPage',
    'ProductDescription': 'ProductDescription',
    'OriginalPrice': 'OriginalPrice',
    'DiscountedPrice': 'DiscountedPrice',
    'DiscountRate': 'DiscountRate',
    'ImageLink': 'ImageLink'},
    inplace=True)

# get the directory where the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# construct the full file path
file_path = os.path.join(dir_path, 'clothing_info.sql')

# open the SQL script file for writing
with open(file_path, 'w') as file:
    # write the SQL script to create the table
    file.write('CREATE TABLE clothing_info (\n')
    file.write(' ProductName VARCHAR(255) PRIMARY KEY,\n')
    file.write(' ProductCategory VARCHAR(255),\n')
    file.write(' ProductPage VARCHAR(255),\n')
    file.write(' ProductDescription VARCHAR(1000),\n')
    file.write(' OriginalPrice VARCHAR(10),\n')
    file.write(' DiscountedPrice VARCHAR(10),\n')
    file.write(' DiscountRate VARCHAR(10),\n')
    file.write(' ImageLink VARCHAR(255)\n')
    file.write(');\n\n')

    for index, row in clothing_info.iterrows():
        file.write("INSERT INTO clothing_info (ProductName, ProductCategory, ProductPage, ProductDescription, OriginalPrice, DiscountedPrice, DiscountRate, ImageLink) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');\n".format(row['ProductName'], row['ProductCategory'], row['ProductPage'], row['ProductDescription'], row['OriginalPrice'], row['DiscountedPrice'], row['DiscountRate'], row['ImageLink']))
    