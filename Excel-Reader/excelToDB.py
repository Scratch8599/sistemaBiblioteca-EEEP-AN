import os, time, psycopg2 

def creatingTable(nameTable):
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
                PublishYear   integer,
                Publisher varchar(80),
                Quantity      integer)
    ''', (nameTable))

    curr.close()
    conn.commit()
    conn.close()

def insertingInfoOnTable(nameTable, book, author, category, edition, publishyear, publisher, quantity):
    # Integração ao PostGreeSQL
    conn = psycopg2.connect(database="    ", 
                        user="    ", 
                        password="    ")
    curr = conn.cursor()

    curr.execute('''
    INSERT INTO %s (Book, Author, Category, Edition, PublishYear, Publisher, Quantity) VALUES(%s, %s, %s, %s, %s, %s, %s)
    ''', (nameTable, book, author, category, edition, publishyear, publisher, quantity))
    # Essa caralhada de "%s" vai permitir que o excelReader funcione tranquilo; "%s" indica que uma variável vai ser aplicada no lugar

    curr.close()
    conn.commit()
    conn.close()