import os, time, pandas as pd, excelToDB as eDB

# Integração à planilha
booksSpreadsheet = pd.read_excel(r"sistemaBiblioteca-EEEP-AN\Excel-Reader\ACERVO BIBLIOGRÁFICO - CATALOGADO EM 2023.xlsx", header = 0)
titlesCollumn    = booksSpreadsheet['TITULO DO LIVRO'].tolist()
authorsCollumn   = booksSpreadsheet['AUTOR'].tolist()
categoryCollumn  = booksSpreadsheet['CATEGORIA'].tolist()
editionCollumn   = booksSpreadsheet['EDIÇÃO'].tolist()
yearCollumn      = booksSpreadsheet['ANO DE PUBLICAÇÃO'].tolist()
publisherCollumn = booksSpreadsheet['EDITORA'].tolist()
quantitCollumn   = booksSpreadsheet['QUANT.'].tolist()
# O "x".tolist() retorna uma lista float (???)

def searchingForUndefinedData():
    cont = 0
    for i in titlesCollumn:
        if str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
                return "Undefined Data"     
        cont += 1

def readingExcelFile():
    cont = 0
    for i in titlesCollumn:
        # Condicional feita para dividir as seções: "PNLD LITERÁRIO 2021/2023 - ACERVO x"
        if str(quantitCollumn[cont]) == "nan":
            # Tive que converter em string pra poder fazer a comparação como NaN
            os.system('cls')
            print(f"{"="*10} \n{titlesCollumn[cont]} \n{"="*10}\n")
            time.sleep(1)
        else: 
            # Condicional feita para verificar se há informações faltando
            if str(authorsCollumn[cont]) == 'nan' or str(categoryCollumn[cont]) == 'nan' or str(editionCollumn[cont]) == 'nan' or str(yearCollumn[cont]) == 'nan' or str(publisherCollumn[cont]) == 'nan' or str(quantitCollumn[cont]) == 'nan':
                # Tive que converter em string pra poder fazer a comparação como NaN
                print(f'{'='*100}\n{'='*100}\n{'='*100} \n{' '*20}ERRO EM {titlesCollumn[cont]} \n{'='*100}\n{'='*100}\n{'='*100} \n')
                break
            else:
                print(f"Livro: {cont} \nTítulo: {titlesCollumn[cont]} \nAutor: {authorsCollumn[cont]} \nCategoria: {categoryCollumn[cont]} \nEdição: {editionCollumn[cont]} \nAno de publicação: {yearCollumn[cont]} \nEditora: {publisherCollumn[cont]} \nQuantidade: {quantitCollumn[cont]} {"\n"*2}")
        cont += 1
        time.sleep(0.25)

def addingInfoOnDataBase(nameTable):
    cont = 0
    for i in titlesCollumn:
        if str(quantitCollumn[cont]) == "nan":
            pass
        else:
            eDB.insertingInfoOnTable(nameTable, str(titlesCollumn[cont]), str(authorsCollumn[cont]), str(categoryCollumn[cont]), str(editionCollumn[cont]), yearCollumn[cont], str(publisherCollumn[cont]), quantitCollumn[cont])
        cont += 1
        time.sleep(0.25)