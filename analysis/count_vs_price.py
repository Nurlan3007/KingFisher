import pandas as pd
import matplotlib.pyplot as plt
from connectToDb import conn,cursor

cursor.execute("""
    select sub_category_id, sub_category, count(*), sum(price) as price from products
    inner join sub_categories on sub_category_id = sub_categories.id
    group by sub_category_id, sub_category
    order by price desc;
""")
result = cursor.fetchall()

df = {'sub_category': [], 'count': [], 'price': []}
for i in result:
    df['sub_category'].append(i[1])
    df['count'].append(i[2])
    df['price'].append(i[3])

df = pd.DataFrame(df)

top_10 = df.nlargest(10, "price")

print(top_10)

plt.figure(figsize=(12, 6))
plt.scatter(top_10["count"], top_10["price"], color="skyblue")
plt.xlabel("Количество")
plt.ylabel("Общая стоимость (₸)")
plt.title("Scatter Plot: Количество vs Общая стоимость")
plt.grid(True)
plt.show()

