import pandas as pd
import matplotlib.pyplot as plt
from connectToDb import conn,cursor

cursor.execute("""
    select title,price from products
    order by price desc limit 15;
""")
result = cursor.fetchall()

df = {'title': [], 'price': []}
for i in result:
    df['title'].append(i[0])
    df['price'].append(i[1])

df = pd.DataFrame(df)

print(df)

plt.figure(figsize=(12, 6))
plt.barh(df["title"], df["price"], color="skyblue")
plt.xlabel("Цена (₸)")
plt.ylabel("Продукт")
plt.title("Топ-10 продуктов по цене")
plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()
