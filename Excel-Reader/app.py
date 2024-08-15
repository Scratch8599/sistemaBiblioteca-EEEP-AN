import os, time, pandas as pd, psycopg2, excelReader as eR, excelToDB as eDB

nameTable = input("Defina para qual tabela os livros serão armazenados: \n")

if eR.searchingForUndefinedData() == "Undefined Data":
    print(f'Há informações faltando')
else:
    eDB.creatingTable(nameTable)
    eR.addingInfoOnDataBase(nameTable)