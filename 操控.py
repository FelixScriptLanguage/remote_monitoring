import pygame
from pygame.locals import *
from PIL import Image
import pyautogui
screen_width, screen_height = pyautogui.size()
print("屏幕分辨率为：", screen_width, "x", screen_height)
bh = '0'
file_path = 'file/1.jpg'
img = Image.open(file_path)
w = img.width  # 图片的宽
h = img.height  # 图片的高
def video_image():
    while True:
        pygame.time.delay(100)
        try:
            frame = pygame.image.load('./file/1.jpg')
            frame = pygame.transform.scale(frame, (w//1.5, h//1.5))
            screen.blit(frame, (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标被点击
                if event.button == 1:  # 鼠标左键被点击
                    mouse_pos = pygame.mouse.get_pos()  # 获取鼠标光标位置
                    mouse_pos = (round(mouse_pos[0]*1.5),round(mouse_pos[1]*1.5))
                    print('左键：',mouse_pos)  # 输出yes
                    open('./ml.txt','w',encoding='utf-8').write(bh+':left:'+str(mouse_pos))
                elif event.button == 3:  # 鼠标右键被点击
                    mouse_pos = pygame.mouse.get_pos()  # 获取鼠标光标位置
                    mouse_pos = (round(mouse_pos[0] * 1.5), round(mouse_pos[1] * 1.5))
                    print('右键：',mouse_pos)
                    open('./ml.txt','w',encoding='utf-8').write(bh+':right:'+str(mouse_pos))
            elif event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                key = pygame.key.name(event.key).replace('meta','windows')
                open('./ml.txt', 'w', encoding='utf-8').write(bh + ':key:' + key)
        pygame.display.update()



def window():
    pygame.init()
    global screen
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((w//1.5, h//1.5))
    pygame.display.set_caption('屏幕控制')
    #bg = pygame.image.load('file/1.jpg')
    #screen.blit(bg, (0, 0))
    pygame.display.update()
    video_image()


if __name__ == '__main__':
    window()
    # 3.2 显示pygame窗口

