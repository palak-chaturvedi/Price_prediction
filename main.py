import time
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


avg_price_list = []
prices_list =[]
name = []
configuration = []
chrome_drive = "C:/Users/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive)

count = 0




driver.get("https://housing.com/in/buy/searches/Pskwz0ocdh7q42r5")
time.sleep(3)
previous_height =driver.execute_script("return document.body.scrollHeight")


no_of_pagedowns = 2000

while True:
    print(count)
    if (count > 10000):
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    soup = BeautifulSoup(driver.page_source,"html.parser")
    sects = soup.find_all('div', class_="css-kjafn5")
    for sect in sects:
        props = sect.find_all('div', class_="css-v64o2m")
        for prop in props:
            Price = prop.find('div', class_="css-70qvj9")
            price = Price.find('div', class_="css-18rodr0")
            prices_list.append(price.text)
            Add = prop.find('div', class_="css-ltqa49")
            address = Add.find('h3', class_="css-zekqfr")
            name.append(address.text)
            Features = prop.find('div', class_="css-mifb2i")
            Multi = Features.find_all('div', class_="css-ebj250")
            # for multi in Multi:

            config = Multi[0].find('div', class_="css-1ty8tu4")
            configuration.append(config.text)
            if(len(Multi)==3):
                avg_price = Multi[2].find('div', class_="css-1ty8tu4")
                avg_price_list.append(avg_price.text)
            else:
                avg_price = Multi[1].find('div', class_="css-1ty8tu4")
                avg_price_list.append(avg_price.text)
            # info = [price.text,address.text, config.text, avg_price.text]
            # print(info)
            count+=1

    if new_height == previous_height:

        break

data = pd.DataFrame(list(zip(name, configuration, prices_list, avg_price_list)),
                    columns=['Name','Configuration','Price','Average Price'])
# print(data)
file = 'Data.csv'
a =data.to_csv(file,index = False)








