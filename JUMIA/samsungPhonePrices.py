import requests 
from bs4 import BeautifulSoup
import csv

#store the url in page
page = requests.get("https://www.jumia.com.ng/mobile-phones/samsung/")
# parse the page to the bs library
soup = BeautifulSoup(page.content, 'html.parser')

#store the div that contains the data you want to obtain in a container
content = soup.find("div", class_="-paxs row _no-g _4cl-3cm-shs")

# store all of the items
resultList = content.find_all("article", class_="prd _fb col c-prd")

# create a csv file
with open('jumia_samsung_prices.csv', mode='w', newline='') as outputFile:
    samsung_prices = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    samsung_prices.writerow(['Name', 'Price', 'Stars'])
    
    # loop to obtain the name of the product, price and stars of each item, and insert the result into the csv file
    for result in resultList:
        title = result.find("h3").text.strip()
        price = result.find("div", class_="prc").text.strip()
        amount = price[1:]
        stars = result.find("div", class_ = "rev").text[:3]
        samsung_prices.writerow([title,amount,stars])
