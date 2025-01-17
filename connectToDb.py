import psycopg2


conn = psycopg2.connect(dbname='kingFisher', user='postgres', 
                        password='root', host='localhost', port="5433")
cursor = conn.cursor()




