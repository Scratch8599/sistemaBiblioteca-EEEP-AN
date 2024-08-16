import os, time, pandas as pd, psycopg2
# Integração à planilha
booksSpreadsheet = pd.read_excel(r"ACERVO BIBLIOGRÁFICO - CATALOGADO EM 2023.xlsx", header = 0)
titlesCollumn    = booksSpreadsheet['TITULO DO LIVRO'].tolist()
authorsCollumn   = booksSpreadsheet['AUTOR'].tolist()
categoryCollumn  = booksSpreadsheet['CATEGORIA'].tolist()
editionCollumn   = booksSpreadsheet['EDIÇÃO'].tolist()
yearCollumn      = booksSpreadsheet['ANO DE PUBLICAÇÃO'].tolist()
publisherCollumn = booksSpreadsheet['EDITORA'].tolist()
quantitCollumn   = booksSpreadsheet['QUANT.'].tolist()

# O "x".tolist() retorna uma lista float (???)

conn = psycopg2.connect(database="    ", 
                        user="    ", 
                        password="    ")
curr = conn.cursor()

dbErrors = [ ]

nameTable = str(input("Digite o nome da tabela a ser inserido"))



cont = 0
for i in titlesCollumn:
    if str(authorsCollumn[cont]) != 'nan' or str(categoryCollumn[cont]) != 'nan' or str(editionCollumn[cont]) != 'nan' or str(yearCollumn[cont]) != 'nan' or str(publisherCollumn[cont]) != 'nan' or str(quantitCollumn[cont]) != 'nan':
        curr.execute('''
        INSERT INTO %s (Book, Author, Category, Edition, PublishYear, Publisher, Quantity) VALUES(%s, %s, %s, %s, %s, %s, %s)
        ''', (nameTable, str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), int(yearCollumn[cont]), str(publisherCollumn[cont]), int(quantitCollumn[cont])))
        curr.execute('''
        SELECT * FROM %s WHERE Book = '%s' 
        ''', (nameTable, str(titlesCollumn[cont])))
        validation = curr.fetchall()
        if str(titlesCollumn[cont]) == str(validation[1]):
            print(f"Erro em {titlesCollumn[cont]}")
            dbErrors.append(f"Erro em {titlesCollumn[cont]}")
            pass
        elif str(authorsCollumn[cont]) == str(validation[2]):
            print(f"Erro em {authorsCollumn[cont]}")
            dbErrors.append(f"Erro em {authorsCollumn[cont]}")
            pass
        elif str(categoryCollumn[cont]) == str(validation[3]):
            print(f"Erro em {categoryCollumn[cont]}")
            dbErrors.append(f"Erro em {categoryCollumn[cont]}")
            pass
        elif str(editionCollumn[cont]) == str(validation[4]):
            print(f"Erro em {editionCollumn[cont]}")
            dbErrors.append(f"Erro em {editionCollumn[cont]}")
            pass
        elif str(yearCollumn[cont]) == str(validation[5]):
            print(f"Erro em {yearCollumn[cont]}")
            dbErrors.append(f"Erro em {yearCollumn[cont]}")
            pass
        elif str(publisherCollumn[cont]) == str(validation[6]):
            print(f"Erro em {publisherCollumn[cont]}")
            dbErrors.append(f"Erro em {publisherCollumn[cont]}")
            pass
        elif str(quantitCollumn[cont]) == str(validation[7]):
            print(f"Erro em {quantitCollumn[cont]}")
            dbErrors.append(f"Erro em {quantitCollumn[cont]}")
            pass
        pass
    else 







# Old code, just backup
cont = 0
for i in titlesCollumn:
    # Condicional feita para dividir as seções: "PNLD LITERÁRIO 2021/2023 - ACERVO x"
    if str(quantitCollumn[cont]) == "nan":
        # Tive que converter em string pra poder fazer a comparação como NaN
        os.system('cls')
        print(f"{titlesCollumn[cont]}\n")
        time.sleep(1)
    else: 
        # Condicional feita para verificar se há informações faltando
        if str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
            # Tive que converter em string pra poder fazer a comparação como NaN
            print(f'ERRO EM {titlesCollumn[cont]}\n')
            break
        else:
            print(f"Livro: {cont} \nTítulo: {titlesCollumn[cont]} \nAutor: {authorsCollumn[cont]} \nCategoria: {categoryCollumn[cont]} \nEdição: {editionCollumn[cont]} \nAno de publicação: {yearCollumn[cont]} \nEditora: {publisherCollumn[cont]} \nQuantidade: {quantitCollumn[cont]} \n")
    cont += 1
    time.sleep(0.25)