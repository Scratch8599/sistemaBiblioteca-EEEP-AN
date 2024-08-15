import os, time, psycopg2 

def tableCreate(nameTable):
    # Integração ao PostGreeSQL
    conn = psycopg2.connect(database="    ", 
                        user="    ", 
                        password="    ")
    curr = conn.cursor()

    curr.execute('''
    CREATE TABLE if not exists %s(ID integer PRIMARY KEY, 
                Book      varchar(80), 
                Author    varchar(80), 
                Category  varchar(80),
                Edition   varchar(80),
                PublishYear       int,
                Publisher varchar(80),
                Quantity          int)
    ''', (nameTable))
