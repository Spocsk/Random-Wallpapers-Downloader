
import urllib.request
import os
import time
import ctypes
import random

print('Program start...')


dir_content = os.listdir('C:/Users/Dylan/Desktop/Scripts/Python/random_wallpapers')

def set_wallpapers():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:/Users/Dylan/Desktop/scripts/Python/random_wallpapers/' + str(dir_content[random_num]) , 0)
    print('Wallpapers : {} set !'.format(dir_content[random_num]))

def dl_wallpapers():
    img_url = "https://source.unsplash.com/random/2560x1080"
    img_name = os.path.basename(img_url)
    urllib.request.urlretrieve(img_url,img_name + '_' + str(milli) +'.jpg')#save pic into folder
    print('Wallpapers downloaded as {}'.format(img_name + '_' + str(milli) +'.jpg'))

x = 0

#1 min timer
while True:
    milli = int(round(time.time() * 1000))
    x += 1
    time.sleep(0.5)
    dl_wallpapers()
"""
    if x == 1:
        #dl_wallpapers()
        #time.sleep(10)
        #random_num =  random.randint(0,len(dir_content)-1)
        #set_wallpapers()
        x = 0


"""




