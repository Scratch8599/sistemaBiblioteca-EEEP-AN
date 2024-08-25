import os, time, pyautogui as auto

def switchInfo(x):
    auto.keyDown('shift')
    auto.scroll(x)
    auto.keyUp('shift')

def getEmail():
    auto.keyDown('ctrl')
    auto.click(1546,733)
    auto.keyUp('ctrl')

def registerUser(userName,userEmail,userGender,userCPF,userID,userYear):
    auto.hotkey('alt', 'tab')
    auto.scroll(1000)
    auto.click(1316,466)
    auto.click(904,718)
    auto.write(userName)
    auto.click(915,764)
    auto.click(915,797)
    auto.scroll(-1000)
    auto.click(900,472)
    auto.write(userEmail)
    auto.click(900,499)
    if userGender == "m" or 'M':
        auto.click(900,533)
    elif userGender == "f" or 'F':
        auto.click(900,550)
    auto.click(900,650)
    auto.write(userCPF)
    auto.click(900,900)
    if userGender == "m":
        auto.write(f'ALUNO {userYear} MATRICULA: {userID}')
    elif userGender == "M":
        auto.write(f'ALUNO {userYear} MATRICULA: {userID}')
    elif userGender == "f":
        auto.write(f'ALUNA {userYear} MATRICULA: {userID}')
    elif userGender == "F":
        auto.write(f'ALUNA {userYear} MATRICULA: {userID}')
    auto.click(1111,985)
    auto.hotkey('alt', 'tab')

def runApp():
    auto.click(633,770, 2)
    auto.hotkey('ctrl', 'c')
    auto.moveTo(819,736)
    auto.dragTo(1343,736, 2, button='left')
    time.sleep(0.5)
    auto.hotkey('ctrl', 'c')
    time.sleep(0.5)
    auto.click(1526,734, 2)
    auto.hotkey('ctrl', 'c')
    switchInfo(-10000)
    getEmail()
    auto.click(371,15)
    auto.moveTo(634,52)
    auto.dragTo(234,52, 5, button='left')
    auto.hotkey('ctrl', 'c')
    auto.click(459,14)
    auto.click(633,770)
    switchInfo(10000)
    auto.scroll(-155)

auto.hotkey('alt', 'tab')
for i in range(0,9):
    runApp()
    userName = input('Digite o nome do Aluno(a):\n')
    userEmail = input('Digite o E-mail do Aluno(a)\n')
    userGender = input("Digite o sexo do Aluno(a)\nUse 'M' para MASCULINO e 'F' para FEMININO\n")
    userCPF = input('Digite o CPF do Aluno(a)\n')
    userID = input('Digite a matrícula do Aluno(a)\n')
    userYear = input('Digite o ano de ingresso do Aluno(a)\n')
    registerUser(userName,userEmail,userGender,userCPF,userID,userYear)

# auto.mouseInfo()
