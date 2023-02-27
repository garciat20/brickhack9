
# Budget Buddy

This project was created during RIT's annual hackathon, Brickhack, specifically BrickHack 9 which took place from February 25-26th, 2023. The purpose of this application is to webscrape the clothing brand Kappa's sale category (which was done using Python, Beautifulsoup4), obtain information (clothing name, original price, discounted price, discounted rate, and the link) about every discounted clothing in their men and women's categories. We then used PostgreSQL on the backend to develop a database of the all the clothing information, and used flask to host the information on a IOS application (using Swift). 

## Features

- Sorting by price (Ascending and Descending)
- Sorting by categories (Men and woemn)
- Seamless view of all the clothing through scrolling.
- Transition from clothing to the product page with a clic

## Technologies used

-Python (used to webscrape the data from the web through a usage of the requests libary and Beautifulsoup4 libaries)
-PostgreSQl (backend/database management of the collected clothing information 
-Flask (used to host the PostgreSQL data)
-Swift (used Xcode to display the data on IOS devices)

## Instructions

-Download Python here: https://www.python.org/downloads/ 
-Clone the file with a IDE like Visual Studio Code, pycharm, etc.
-In the terminal cd into the brickhack9 directory
-Download all files in the requirements.txt with pip install -r requirements.txt or pip3 install -r requirements.txt (for macOS users)
-Run the kappa_get_data.py file with python 'src/db/kappa_get_data.py' or python3 'src/db/kappa_get_data.py' (macOS), this will give you the up-to-date clothing catalogue. 
-Start the python server with Python 'src/server.py' or python3 'src/server.py'
-Run the swift code with a IDE like xCode. 
