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

# Conexão ao PostGreeSQL
conn = psycopg2.connect(dbname   = "Teste", 
                        user     = "postgres", 
                        password = "1969",
                        host     = "localhost",
                        port     = "5432")
curr = conn.cursor()

# Criando tabela caso não exista uma
curr.execute('''
    CREATE TABLE if not exists Livros (ID integer PRIMARY KEY,
                Acervo    varchar(80),
                Book      varchar(80), 
                Author    varchar(80), 
                Category  varchar(80),
                Edition   varchar(80),
                PublishYear   integer,
                Publisher varchar(80),
                Quantity      integer)
    ''')

#Inicializando a lista que vai armazenar os erros
dbErrors = [ ]
rdErros  = [ ]

# Iniciando as variáveis que vão ser manipuladas no looping
cont   = 0
acervo = ""
for i in range(0,100):
    if str(quantitCollumn[cont]) == 'nan':
        # Checando se a linha lida é de "Acervo", se é, está armazenando para adicionar no banco de dados
        acervo = str(titlesCollumn[cont])
        
    else:
        if str(authorsCollumn[cont]) != 'nan' or str(categoryCollumn[cont]) != 'nan' or str(editionCollumn[cont]) != 'nan' or str(yearCollumn[cont]) != 'nan' or str(publisherCollumn[cont]) != 'nan' or str(quantitCollumn[cont]) != 'nan':
            print(f"Livro: {cont}")
            #Checando se há todas as informações, se há, está adicionando e validando no banco de dados
            curr.execute('''
            INSERT INTO Livros (ID, Acervo, Book, Author, Category, Edition, PublishYear, Publisher, Quantity) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (cont, acervo, str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), int(yearCollumn[cont]), str(publisherCollumn[cont]), int(quantitCollumn[cont]),))
            
            # Validação e armazenamento de erros 
            curr.execute('''
            SELECT * FROM Livros WHERE Book = %s
            ''', (str(titlesCollumn[cont]),))
            validation = curr.fetchone()
            if acervo != str(validation[1]):
                print(f"Erro em {acervo}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            if str(titlesCollumn[cont]) != str(validation[2]):
                print(f"Erro em {titlesCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(authorsCollumn[cont]) != str(validation[3]):
                print(f"Erro em {authorsCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(categoryCollumn[cont]) != str(validation[4]):
                print(f"Erro em {categoryCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(editionCollumn[cont]) != str(validation[5]):
                print(f"Erro em {editionCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(yearCollumn[cont]) != str(validation[6]):
                print(f"Erro em {yearCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(publisherCollumn[cont]) != str(validation[7]):
                print(f"Erro em {publisherCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif quantitCollumn[cont] != validation[8]:
                print(f"Erro em {quantitCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            pass
        elif str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
            print(f'Ocorreu um erro em {titlesCollumn[cont]}')
            rdErros.append(f"Erro em {titlesCollumn[cont]}")
            pass
    cont += 1
    time.sleep(0.25)

print(f'{dbErrors}\n{rdErros}')
time.sleep(len(dbErrors))


curr.close()
conn.commit()
conn.close()