import time, os, pyautogui as auto

userName   = input()
userEmail  = input()
userGender = input()
userCPF    = input()
userYear   = input()
userID     = input()

auto.hotkey('alt', 'tab')
auto.scroll(1000)
auto.click(1275,469)
auto.click(840,718)
auto.write(userName)
auto.click(874,764)
auto.click(871,803)
auto.scroll(-1000)
auto.click(868,471)
auto.write(userEmail)
auto.click(898,494)
if userGender == "M" or 'm':
    auto.click(895,532)
elif userGender == "F" or "f":
    auto.click(891,549)
auto.click(881,646)
auto.write(userCPF)
auto.click(856,851)
if userGender == "M" or 'm':
    auto.write(f'Aluno do ano: {userYear}; Matrícula: ')
elif userGender == "F" or "f":
    auto.write(f'Aluna do ano: {userYear}; Matrícula: ')

auto.mouseInfo()