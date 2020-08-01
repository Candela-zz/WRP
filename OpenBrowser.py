import pyautogui
import time
import webbrowser
import pyperclip

pyperclip.copy('ลงุวิศวกร สอนคำนวณ')
#####ก็อปปี้ค่าไปไว้ในclipboard เเต่ paste ไม่ได้เอาค่าไปวางในsearch engine เลยpaste ไม่ได้

def search(word):
    webbrowser.open('https://www.google.com/')

    time.sleep(4)

    pyautogui.moveTo(600,510,2)
    pyautogui.doubleClick()
    time.sleep(2)
    #####pyautogui.write(word)
    pyautogui.hotkey('ctrl','v')#####ใช้สำหรับภาษาอื่นๆ
    pyautogui.press('enter')
    
    time.sleep(3)
    pyautogui.screenshot(f'{word}.png')

    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('backspace')
    
'''
country=['Brazil','Argentina','Russia','Italy']
for u in country:
    print(u)

search('Thailand')
search('Russia')
'''



