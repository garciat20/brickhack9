
# Budget Buddy

This project was created during RIT's annual hackathon, Brickhack, specifically BrickHack 9 which took place from February 25-26th, 2023. The purpose of this application is to webscrape the clothing brand Kappa's sale category (which was done using Python, Beautifulsoup4), obtain information (clothing name, original price, discounted price, discounted rate, and the link) about every discounted clothing in their men and women's categories. We then used PostgreSQL on the backend to develop a database of the all the clothing information, and used flask to host the information on a IOS application (using Swift). 

## Features

- Sorting by price (Ascending and Descending)
- Sorting by categories (Men and woemn)
- Seamless view of all the clothing through scrolling.
- Transition from clothing to the product page with a clic

##Technologies used

-Python (used to webscrape the data from the web through a usage of the requests libary and Beautifulsoup4 libaries)
-PostgreSQl (backend/database management of the collected clothing information 
-Flask (used to host the PostgreSQL data)
-Swift (used Xcode to display the data on IOS devices)
