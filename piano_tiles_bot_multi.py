import pyautogui 
import time
import multiprocessing


def click_on_black(x,y,stri="tag"):
   while True:
      if( pyautogui.pixelMatchesColor(x, y, (0, 0, 0))):
         pyautogui.click(x=x,y=y)
      


if __name__ == "__main__":
   t1=multiprocessing.Process(target=click_on_black,args=(714,565,"t1"))
   t2=multiprocessing.Process(target=click_on_black,args=(868,575,"t2"))
   
   t3=multiprocessing.Process(target=click_on_black,args=(1004,575,"t3"))
   t4=multiprocessing.Process(target=click_on_black,args=(1210,575,"t4"))

   t1.start()
   t2.start()
   t3.start()
   t4.start()