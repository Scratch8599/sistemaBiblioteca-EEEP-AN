import pyautogui as auto, time

screenWidth, screenHeight = auto.size()
print(screenWidth, screenHeight)

mouseX, mouseY = auto.position()
print(mouseX, mouseY)

def switchWindow():
    auto.keyDown('alt')
    auto.press('tab')
    auto.keyUp('alt')

def registerUser(userName,userEmail,userGender,userCPF,userID,userYear):
    switchWindow()
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
    time.sleep(4)
    switchWindow()
    validating = input("As informações estão corretas?\nUse 's' para SIM e 'n' para NÃO\n")
    switchWindow()
    if validating == "s":
        auto.click(1111,985)
    elif validating == "S":
        auto.click(1111,985)
    elif validating == "n":
        auto.click(1300,985)
        auto.click(1064,612)
    elif validating == "N":
        auto.click(1300,985)
        auto.click(1064,612)
    switchWindow()
    


userName = input('Digite o nome do Aluno(a):\n')
userEmail = input('Digite o E-mail do Aluno(a)\n')
userGender = input("Digite o sexo do Aluno(a)\nUse 'M' para MASCULINO e 'F' para FEMININO\n")
userCPF = input('Digite o CPF do Aluno(a)\n')
userID = input('Digite a matrícula do Aluno(a)\n')
userYear = input('Digite o ano de ingresso do Aluno(a)\n')
registerUser(userName,userEmail,userGender,userCPF,userID,userYear)
