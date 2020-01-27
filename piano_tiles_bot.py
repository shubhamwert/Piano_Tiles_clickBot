import pyautogui 
import time
import multiprocessing
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

print(pyautogui.size())
width, height =pyautogui.size()

def getInitialData():
   x1=0
   y1=0
   while True:
      x, y = pyautogui.position()
      if x1 != x and y1 !=y:  
         print(x,y)
         x1=x
         y1=y

def click_on_black(x,y,stri="tag"):
   while True:
      # print(stri)
      if( pyautogui.pixelMatchesColor(x, y, (0, 0, 0))):
         pyautogui.click(x=x,y=y)
      # else:
      #    return 



if __name__ == "__main__":
   getInitialData()
   time.sleep(2)
   x=[714,868,1004,1210]

   #loop initialize
   while True:
      for x1 in x:
         click_on_black(x1,580)
   

#714 565 868 578 1004 583 1210 589