import pyautogui as auto

def switchWindow():
    auto.keyDown('alt')
    auto.press('tab')
    auto.keyUp('alt')

def getUserInfo():
    zoom = "125"
    page = 1
    switchWindow()
    auto.click(953,97)
    auto.write(zoom)
    auto.click(833,97)
    auto.write(str(page))
    auto.moveTo(945,369)
    
getUserInfo()
auto.mouseInfo()
# def registerUser():