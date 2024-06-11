from bs4 import BeautifulSoup
import requests
import pandas as pd

name_list, price_list, rating_list, link_list, specifications_list, image_list = [], [], [], [], [], []
info = [name_list, price_list, rating_list, link_list, specifications_list, image_list]

for page in range(1,21):
    url = f'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'
    basePath = 'https://www.flipkart.com'
    response = requests.get(url)
    htmlText = response.content
    soup = BeautifulSoup(htmlText, 'lxml')

    flipkart = {}
    phones = soup.find_all('a', 'CGtC98')
    for phone in phones:
        name = phone.find('div', 'KzDlHZ').get_text()
        # name = ' ' if(phone.find('div', 'KzDlHZ')==None) else phone.find('div', 'KzDlHZ').get_text()
        price = int(phone.find('div', 'Nx9bqj _4b5DiR').get_text().replace('₹', '').replace(',', ''))
        rating = 0 if(phone.find('div', 'XQDdHH')==None) else float(phone.find('div', 'XQDdHH').get_text())
        link = basePath + phone['href']
        tags = phone.find_all('li', 'J+igdf')
        specifications = [li.get_text() for li in tags]
        image = phone.find('img', 'DByuf4')['src']

        detail = [name,price,rating,link,specifications,image]

        for inf, det in zip(info,detail):
            inf.append(det)

    print(f"Page {page} is collected.")

columns = ['Name', 'Price', 'Rating', 'Link', 'specifications', 'Image']

for column, inf in zip(columns, info):
    flipkart[column] = inf

myData = pd.DataFrame(flipkart, columns=columns)

myData.to_csv(r'C:\Users\admin\OneDrive\Desktop\flipkartPhones.csv')
