import time, pyautogui as auto

userName = ""
userEmail = ""
# userGender = input("Digite o sexo do Aluno(a)\nUse 'M' para MASCULINO e 'F' para FEMININO\n")
# userCPF = input('')
# userID = input('')
# userYear = input('')

def switchWindow():
    auto.keyDown('alt')
    auto.press('tab')
    auto.keyUp('alt')

def switchTab():
    auto.keyDown('ctrlleft')
    auto.press('tab')
    auto.keyUp('ctrlleft')

def closeTab():
    auto.keyDown('ctrlleft')
    auto.press('w')
    auto.keyUp('ctrlleft')

def copyInfo():
    auto.keyDown('ctrlleft')
    auto.press('c')
    auto.keyUp('ctrlleft')

def pasteInfo():
    auto.keyDown('ctrlleft')
    auto.press('v')
    auto.keyUp('ctrlleft')

def getEmail():
    auto.keyDown('ctrlleft')
    auto.click(1843,514)
    auto.keyUp('ctrlleft')
    auto.keyDown('ctrlleft')
    auto.press('tab', 3)
    auto.keyUp('ctrlleft')
    auto.moveTo(460,51)
    auto.dragTo(194,51, 5, button="left")
    copyInfo()

def getUserInfo():
    zoom = "160"
    page = 1
    switchWindow()
    auto.click(953,97)
    auto.write(zoom)
    auto.click(833,97)
    auto.write(str(page))
    auto.moveTo(957,514)
    auto.dragTo(602,514, 1.05, button="left")
    copyInfo()
    switchWindow()
    auto.click(368,996)
    userName = input()
    pasteInfo()
    switchTab()
    getEmail()
    switchTab()
    userEmail = input()
    time.sleep(0.3)
    auto.click(368,996, 2)
    auto.keyDown('ctrlleft')
    auto.keyDown('shiftleft')
    auto.press('v')
    auto.keyUp('ctrlleft')
    auto.keyUp('ctrlshift')
    auto.press('enter')


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
    # time.sleep(4)
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

getUserInfo()

auto.mouseInfo()
# def registerUser():