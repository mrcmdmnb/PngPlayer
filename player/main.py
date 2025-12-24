import cv2 as cv
import pygame
import regex
import time
val=[0,0,0,0,0,0,0,0,0,0,0]
i=0
with open('settings.txt', 'r', encoding='utf-8') as file:
   lines = file.readlines()
   for line in lines:
       val[i]=line
       i=i+1
       
numofpic=int(regex.findall(r'\d+',val[0])[0])
pic_row=int(regex.findall(r'\d+',val[1])[0])
pic_col=int(regex.findall(r'\d+',val[2])[0])
snd_vol=int(regex.findall(r'\d+',val[3])[0])
wait=int(regex.findall(r'\d+',val[4])[0])
win_x=int(regex.findall(r'\d+',val[5])[0])
win_y=int(regex.findall(r'\d+',val[6])[0])
ismusic=int(regex.findall(r'\d+',val[7])[0])
pygame.init()
pygame.mixer.init()
cv.namedWindow("player",cv.WINDOW_NORMAL)
cv.waitKey(1)
cv.resizeWindow("player", pic_row, pic_col)
cv.moveWindow("player",win_x,win_y)
i=1
last_time = time.time()
cv.namedWindow("player",cv.WINDOW_NORMAL) 
if ismusic==1:
    pygame.mixer.music.load("snd.mp3")
    pygame.mixer.music.set_volume(int(snd_vol)/100)
    pygame.mixer.music.play()
while True:
    img=cv.imread(f"pic/{str(i)}.jpg")
    cv.imshow("player",img)
    key=cv.waitKey(1)&0xFF
    if key==27:
        cv.destroyAllWindows() 
        pygame.mixer.music.stop()
        break
    current_time = time.time()
    if current_time - last_time>=wait/1000.0:
        if i!=numofpic:  
            i+=1
        else:
            i=1
        last_time = current_time
