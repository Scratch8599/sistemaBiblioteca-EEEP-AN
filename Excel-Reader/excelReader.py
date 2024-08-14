import pandas as pd

planilhaLivros = pd.read_excel(r"sistemaBiblioteca-EEEP-AN\Excel-Reader\test.xlsx", header = 0)
gabrielsRow = planilhaLivros['Gabriel'].tolist()
emiliasRow = planilhaLivros['Emilia'].tolist()

cont = 0

if len(gabrielsRow) > len(emiliasRow):
    for i in gabrielsRow:
        print(gabrielsRow[cont], emiliasRow[cont])
        cont += 1
else:
    for i in emiliasRow:
        print(emiliasRow[cont], gabrielsRow[cont])
        cont += 1