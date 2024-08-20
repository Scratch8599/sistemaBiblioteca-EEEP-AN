import time, os, psycopg2, pandas as pd

conn = psycopg2.connect(database='Teste', 
                        user='postgres', 
                        password='1969', 
                        host='localhost', 
                        port='5432')
curr = conn.cursor()
curr.execute("CREATE TABLE IF NOT EXISTS Books( ID INTEGER PRIMARY KEY, Acervo VARCHAR(800), Book VARCHAR(800), Author VARCHAR(800), Category VARCHAR(800), Edition VARCHAR(800), PublishYear INTEGER, Publisher VARCHAR(800), Quantity INTEGER)")

booksSpreadsheet = pd.read_excel(r"Excel-Reader\ACERVO BIBLIOGRÁFICO - CATALOGADO EM 2023.xlsx", sheet_name= 'Ricardo', header = 0 )
titlesCollumn    = booksSpreadsheet['TITULO DO LIVRO'].tolist()
authorsCollumn   = booksSpreadsheet['AUTOR'].tolist()
categoryCollumn  = booksSpreadsheet['CATEGORIA'].tolist()
editionCollumn   = booksSpreadsheet['EDIÇÃO'].tolist()
yearCollumn      = booksSpreadsheet['ANO DE PUBLICAÇÃO'].tolist()
publisherCollumn = booksSpreadsheet['EDITORA'].tolist()
quantitCollumn   = booksSpreadsheet['QUANT.'].tolist()

curr.execute("SELECT MAX(ID) FROM Books")
IDk = curr.fetchone()
if str(IDk[0]) == 'None':
    IDk = 0
else:
    IDk = (IDk[0])+1
erros = [ ]
acervo = " "
cont = 0
# for i in titlesCollumn:
for i in range(0,50):
    if str(titlesCollumn[cont]) != 'nan' and (str(authorsCollumn[cont]) == 'nan' and str(categoryCollumn[cont]) == 'nan' and str(editionCollumn[cont]) == 'nan' and str(yearCollumn[cont]) == 'nan' and str(publisherCollumn[cont]) == 'nan' and str(quantitCollumn[cont]) == 'nan'):
        acervo = titlesCollumn[cont]
        print(f'Adicionando: {titlesCollumn[cont]}')
    else:
        print(f'Validando: {titlesCollumn[cont]}')
        data = [ str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), str(yearCollumn[cont]), str(publisherCollumn[cont]), str(quantitCollumn[cont]) ]
        vTool = " "
        for i in data:
            match i:
                case 'nan':
                    vTool = "Erro"
                    print('Informações faltando')
                    erros.append(f'Erro em: {titlesCollumn[cont]}')
                    break
                case '-':
                    vTool = "Erro"
                    print('Informações faltando')
                    erros.append(f'Erro em: {titlesCollumn[cont]}')
                    break
        if vTool != 'Erro':
            curr.execute("SELECT Book FROM Books")
            bookVTool = curr.fetchone()
            for i in bookVTool:
                print(i)
#             if str(bookVTool[0]) == str(titlesCollumn[cont]):
#                 curr.execute("SELECT Quantity FROM Books ")
#             print('Ok')
#             curr.execute("INSERT INTO Books(Acervo, Book, Author, Category, Edition, PublishYear, Publisher, Quantity, ID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s, %s)", (str(acervo), str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), int(round(yearCollumn[cont])), str(publisherCollumn[cont]), int(round(quantitCollumn[cont])), IDk, ))
#     time.sleep(0.2)
#     cont += 1
#     IDk += 1

# os.system('cls')
# for i in erros:
#     print(i)
#     time.sleep(0.5)

# curr.close()
# conn.commit()
# conn.close()