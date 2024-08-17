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
for i in titlesCollumn:
    if str(quantitCollumn[cont]) == 'nan':
        # Checando se a linha lida é de "Acervo", se é, está armazenando para adicionar no banco de dados
        acervo = str(titlesCollumn[cont])
        
    else:
        if str(authorsCollumn[cont]) != 'nan' or str(categoryCollumn[cont]) != 'nan' or str(editionCollumn[cont]) != 'nan' or str(yearCollumn[cont]) != 'nan' or str(publisherCollumn[cont]) != 'nan' or str(quantitCollumn[cont]) != 'nan':
            print(f"Tentando adicionar {titlesCollumn[cont]} ao Bando de dados")
            #Checando se há todas as informações, se há, está adicionando e validando no banco de dados
            curr.execute('''
            INSERT INTO Livros (ID, Acervo, Book, Author, Category, Edition, PublishYear, Publisher, Quantity) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (cont, acervo, str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), int(yearCollumn[cont]), str(publisherCollumn[cont]), int(quantitCollumn[cont]),))
            
            # Validação e armazenamento de erros 
            curr.execute('''
            SELECT * FROM Livros WHERE Book = %s
            ''', (str(titlesCollumn[cont]),))
            validation = curr.fetchone()
            checkValidation = [ None, acervo, titlesCollumn[cont], authorsCollumn[cont], categoryCollumn[cont], editionCollumn[cont], yearCollumn[cont], publisherCollumn[cont], quantitCollumn[cont] ]
            for i in range(1,8):
                if str(checkValidation[i]) != str(validation[i]):
                    print(f"Erro em {titlesCollumn[cont]}")
                    dbErrors.append(f"Erro em {titlesCollumn[cont]}")
            pass
        elif str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
            print(f'Ocorreu um erro em {titlesCollumn[cont]}')
            rdErros.append(f"Erro em {titlesCollumn[cont]}")
            pass
    cont += 1
    if cont%50 == 0:
        os.system('cls')
    time.sleep(0.25)

print(f'{dbErrors}\n{rdErros}')
if len(dbErrors) > len(rdErros):
    time.sleep(len(dbErrors))
else:
    time.sleep(len(rdErros))

curr.close()
conn.commit()
conn.close()