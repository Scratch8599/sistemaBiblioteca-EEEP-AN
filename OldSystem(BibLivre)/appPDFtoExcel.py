import os, time, pyautogui as auto

def swithInfo(scrool):
    auto.keyDown( 'shift' )
    auto.scroll(scrool)
    auto.keyUp( 'shift' )

auto.hotkey( 'alt', 'tab' )
auto.click(288,154)
auto.write('200')
auto.press('enter')
auto.hotkey( 'ctrl', 'tab')
auto.click(957,100)
auto.write('300')
auto.press('enter')
auto.moveTo(1539,375)
auto.dragTo(875,376, 2, button="left")
auto.hotkey( 'ctrl', 'c' )
auto.hotkey( 'ctrl', 'tab')
auto.click(166,306)
auto.hotkey( 'ctrl', 'v' )
auto.press('right')
auto.hotkey( 'ctrl', 'tab')
auto.click(956,324)
swithInfo(-8000)
auto.keyDown('ctrl')
auto.click(1481,376)
auto.keyUp('ctrl')
auto.keyDown('ctrlleft')
auto.press('tab', 3)
auto.keyUp('ctrlleft')
auto.moveTo(460,51)
auto.dragTo(194,51, 5, button="left")
auto.hotkey( 'ctrl', 'c')
auto.hotkey( 'ctrl', 'w' )
auto.hotkey( 'ctrl', 'tab' )
auto.hotkey( 'ctrl', 'v' )
auto.press('right')
auto.hotkey( 'alt', 'tab' )
auto.click(927,844)
gender = input('Digite o gênero:\n')
auto.hotkey( 'alt', 'tab' )
auto.write(gender)
auto.press('right')
auto.hotkey( 'ctrl', 'tab')
swithInfo(8000)


# swithInfo(-8000)
# time.sleep(0.5)
# swithInfo(8000)


auto.mouseInfo()