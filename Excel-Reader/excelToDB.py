import os, time, psycopg2 

def tableCreate():
    # Integração ao PostGreeSQL
    conn = psycopg2.connect(database="    ", 
                        user="    ", 
                        password="    ")
    curr = conn.cursor()

    curr.execute('''
    CREATE TABLE if not exists Livros(ID integer )
    ''')
