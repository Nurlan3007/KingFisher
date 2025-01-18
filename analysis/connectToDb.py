import psycopg2


conn = psycopg2.connect(dbname='king_fisher1', user='postgres', 
                        password='12345', host='localhost', port="5438")
cursor = conn.cursor()




