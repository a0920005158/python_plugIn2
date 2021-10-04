import pyautogui
import PIL
from PIL import Image

# 紀錄滑鼠座標
# pyautogui.displayMousePosition() 
# 單擊畫面
pyautogui.click(x=100,y=150,button='left')
# 雙擊畫面
# pyautogui.doubleClick(x=100,y=150,button="left")
# pyautogui.locateOnScreen('test.png')  #  檔案名稱依自己設置處理
# pyautogui.center((1487, 133, 65, 26))  #  取得該圖像的中間值(1519，146)
# pyautogui.click((1519, 146))  #  點擊