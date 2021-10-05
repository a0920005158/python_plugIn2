import pyautogui
import keyboard
import time
import PIL
import time
from PIL import Image

def error_msg(img):
    print(img+' no search image!');

def start_game_process(img):
    try:
        picturePos = pyautogui.locateOnScreen('./img/'+img+'.png')  #  檔案名稱依自己設置處理
        if picturePos == None:
            error_msg(img);
            return False;
        print(picturePos);
        pictureMidPos = pyautogui.center((picturePos[0], picturePos[1], picturePos[2], picturePos[3]))  #  取得該圖像的中間值(1519，146)
        print(pictureMidPos);
        pyautogui.click((pictureMidPos[0], pictureMidPos[1]))  #  點擊p
        return True;
    except:
        error_msg(img);
        return False;


def start_process():
    for i in range(1,21):
        if start_game_process('img'+str(i)) == True:
            continue;
        else:
            isSearch = False;
            while isSearch == False:
                time.sleep(1)
                if start_game_process('img'+str(i)) == True:
                    isSearch = True;

while True:
    start_process();

# while True:
#     if keyboard.read_key() == "f6":
#         start_game_process()
#         break
#     if keyboard.read_key() == "f7":
#         print('f777777777777777777!');
#         break

# https://medium.com/pyladies-taiwan/python-%E5%B0%87python%E6%89%93%E5%8C%85%E6%88%90exe%E6%AA%94-32a4bacbe351
# https://martychen920.blogspot.com/2017/06/python-pyautogui_20.html
# 紀錄滑鼠座標
# pyautogui.displayMousePosition() 
# 單擊畫面
# pyautogui.click(x=100,y=150,button='left')
# 雙擊畫面
# pyautogui.doubleClick(x=100,y=150,button="left")