import requests
from bs4 import BeautifulSoup
from csv import writer
responce = requests.get('https://www.leaders.jo/kitchen-appliances/')

soup = BeautifulSoup(responce.text,'html.parser')
products = soup.findAll(class_='product')

with open('leadersElectric.csv','w') as csv_file:
    csv_writer=writer(csv_file)
    headers = ['Title','image link',]

    for item in products:
        title =item.find(class_='card-title').get_text().replace('\n','')
        print(title)
        price = item.find(class_="price-section price-section--withTax").find(class_='price price--withTax price--main').get_text().replace('\n','')
        print(price)
        image = item.find(class_='card-img-container').find('img')['src']
        print(image)
