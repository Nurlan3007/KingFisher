import requests
from bs4 import BeautifulSoup
from connectToDb import cursor,conn

MAIN_URL = "https://kingfisher.kz"

headers = {
    "Accept" : '*/*',
    "User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


def getPageAndSoup(URL):
    req = requests.get(URL, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    return soup

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

sub_categories = getCategories()
# print(sub_categories)
# print(sub_categories)
i = 0
for sub_category in sub_categories:
    if i == 3: break
    url = MAIN_URL + sub_category[-1]
    print(url)
    soup_sub_category = getPageAndSoup(url)
    titles = soup_sub_category.find_all("a", class_='title')
    prices = soup_sub_category.find_all("span", class_='price')
    descript = soup_sub_category.find_all("span", class_='descript')
    image = soup_sub_category.find_all("a", class_="image")

    for j in range(len(titles)):
        title = titles[j].text
        price = prices[j].text
        print(title)
        print(price)
        # print()
        print("#"*30)
    i += 1

# print(soup)



