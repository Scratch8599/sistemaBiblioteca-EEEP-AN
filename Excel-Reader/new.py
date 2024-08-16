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
conn = psycopg2.connect(database="    ", 
                        user="    ", 
                        password="    ")
curr = conn.cursor()

#Inicializando a lista que vai armazenar os erros
dbErrors = [ ]
rdErros  = [ ]

# Seletor caso a gente precise fazer isso em mais de uma tabela
nameTable = str(input("Digite o nome da tabela a ser inserido"))

# Iniciando as variáveis que vão ser manipuladas no looping
cont = 0
acervo = ""
for i in titlesCollumn:
    if str(quantitCollumn[cont]) == 'nan':
        # Checando se a linha lida é de "Acervo", se é, está armazenando para adicionar no banco de dados
        acervo = str(titlesCollumn[cont])
        cont = 0

        # Inicia um looping de console para printar o acervo atual e indicar que está carregando
        for i in range(0,50):
            print(f"{acervo}{"."*cont}")
            time.sleep(0.3)
            os.system('cls')
            if cont == 4:
                cont = 0 
            cont += 1
        pass
    else:
        if str(authorsCollumn[cont]) != 'nan' or str(categoryCollumn[cont]) != 'nan' or str(editionCollumn[cont]) != 'nan' or str(yearCollumn[cont]) != 'nan' or str(publisherCollumn[cont]) != 'nan' or str(quantitCollumn[cont]) != 'nan':
            #Checando se há todas as informações, se há, está adicionando e validando no banco de dados
            curr.execute('''
            INSERT INTO %s (Acervo, Book, Author, Category, Edition, PublishYear, Publisher, Quantity) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (nameTable, acervo, str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), int(yearCollumn[cont]), str(publisherCollumn[cont]), int(quantitCollumn[cont])))
            curr.execute('''
            SELECT * FROM %s WHERE Book = '%s' 
            ''', (nameTable, str(titlesCollumn[cont])))
            validation = curr.fetchall()

            # Validação e armazenamento de erros 
            if acervo != str(validation[1]):
                print(f"Erro em {acervo}")
                dbErrors.append(f"Erro em {acervo}")
                pass
            if str(titlesCollumn[cont]) != str(validation[2]):
                print(f"Erro em {titlesCollumn[cont]}")
                dbErrors.append(f"Erro em {titlesCollumn[cont]}")
                pass
            elif str(authorsCollumn[cont]) != str(validation[3]):
                print(f"Erro em {authorsCollumn[cont]}")
                dbErrors.append(f"Erro em {authorsCollumn[cont]}")
                pass
            elif str(categoryCollumn[cont]) != str(validation[4]):
                print(f"Erro em {categoryCollumn[cont]}")
                dbErrors.append(f"Erro em {categoryCollumn[cont]}")
                pass
            elif str(editionCollumn[cont]) != str(validation[5]):
                print(f"Erro em {editionCollumn[cont]}")
                dbErrors.append(f"Erro em {editionCollumn[cont]}")
                pass
            elif str(yearCollumn[cont]) != str(validation[6]):
                print(f"Erro em {yearCollumn[cont]}")
                dbErrors.append(f"Erro em {yearCollumn[cont]}")
                pass
            elif str(publisherCollumn[cont]) != str(validation[7]):
                print(f"Erro em {publisherCollumn[cont]}")
                dbErrors.append(f"Erro em {publisherCollumn[cont]}")
                pass
            elif str(quantitCollumn[cont]) != str(validation[8]):
                print(f"Erro em {quantitCollumn[cont]}")
                dbErrors.append(f"Erro em {quantitCollumn[cont]}")
                pass
            pass
        elif str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
            print(f'Ocorreu um erro em {titlesCollumn[cont]}')
            rdErros.append(f"Erro em {titlesCollumn[cont]}")
            pass
    cont += 1
    time.sleep(0.5)
