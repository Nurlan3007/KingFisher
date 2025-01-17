# сначала мы должный получить категории чтобы дальнейши мы могли по ним искать продукты
# 
import requests
from bs4 import BeautifulSoup
from connectToDb import cursor,conn

MAIN_URL = "https://kingfisher.kz/"

headers = {
    "Accept" : '*/*',
    "User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def getPageAndSoup(URL):
    req = requests.get(URL, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    return soup

def getCategoriesAndInsertToDb(soup):
    dropmenu = soup.find_all(class_="dropmenu")
    a = soup.find_all(class_="dropmenu a")
    for items in dropmenu:
        categoryText = items.find("span").text
        categoryHref = items.find("span").get('href')

        cursor.execute("""
            INSERT INTO categories(category, href) VALUES (%s, %s)
        """, (categoryText, categoryHref))

        cursor.execute('select id from categories order by id desc limit 1')
        lastId = cursor.fetchone()[0]

        print(categoryText,categoryHref)
        sub_categories = items.find_all("a")
        for sub_category in sub_categories:
            sub_category_text = sub_category.text
            sub_category_href = sub_category.get('href')
            print(sub_category_text, sub_category_href)
            
            cursor.execute("""
                INSERT INTO sub_categories(category_id, sub_category, href) VALUES(%s,%s,%s)
            """, (lastId, sub_category_text, sub_category_href))
            
        
        conn.commit()
        print('####')

if __name__ ==  'main':
    soup = getPageAndSoup(MAIN_URL)
    getCategoriesAndInsertToDb(soup)



