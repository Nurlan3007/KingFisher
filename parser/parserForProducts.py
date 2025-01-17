import requests
from bs4 import BeautifulSoup
from connectToDb import cursor,conn
from parser.parserForCategoryInsertDb import getPageAndSoup
import re

MAIN_URL = "https://kingfisher.kz"

headers = {
    "Accept" : '*/*',
    "User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


def getCategories():
    cursor.execute("SELECT * FROM sub_categories")
    sub_categories = cursor.fetchall()
    return sub_categories

# soup = getPageAndSoup(URL)
# # print(soup)

# title = soup.find_all("a", class_='title')
# price = soup.find_all("span", class_='price')
# descript = soup.find_all("span", class_='descript')
# image = soup.find_all("a", class_="image")
# print(price[0],title[0],descript[0],image[0])


def getAllProductsAndInsertToDb(sub_categories):
    city = 'Almaty'
    i = 0
    for sub_category in sub_categories:

        url = MAIN_URL + sub_category[-1]
        sub_category_id = sub_category[0]
        print(sub_category_id)
        
        soup_sub_category = getPageAndSoup(url)
        titles = soup_sub_category.find_all("a", class_='title')
        prices = soup_sub_category.find_all("span", class_='price')
        descripts = soup_sub_category.find_all("span", class_='descript')
        images = soup_sub_category.find_all("a", class_="image")

        for j in range(len(titles)):
            title = titles[j].text.strip()
            price = prices[j].text.strip()
            descript = descripts[j].text.strip()
            image = images[j].get("style")

            price = re.sub(r'[^\d.]', '', price)

            print(title)
            print(price)
            print(descript)
            print(image)

            cursor.execute("""
                INSERT INTO products (title, image, price, descripts, city, sub_category_id) VALUES(%s,%s,%s,%s,%s,%s)
            """,(title, image, price, descript, city, sub_category_id))



if __name__ == "__main__":
    sub_categories = getCategories()
    getAllProductsAndInsertToDb(sub_categories)
    conn.commit()



