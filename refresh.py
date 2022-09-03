import pyautogui
from time import sleep

class Refresh:

    base_x = 0
    base_y = 0
    pos_x = 0
    pos_y = 0

    def __init__(self, base):

        self.base_x = base[0]
        self.base_y = base[1]


    def scroll(self):
        pyautogui.moveTo(self.base_x+1000,self.base_y+500)
        pyautogui.click()
        pyautogui.scroll(-10)
        sleep(2)

    def ref(self):
        pyautogui.moveTo(self.base_x+260,self.base_y+800)
        pyautogui.click()
        sleep(1)
        pyautogui.moveTo(self.base_x+890,self.base_y+550)
        pyautogui.click()
        sleep(2)

    def buy(self,point):

        self.pos_x = point[0]
        self.pos_y = point[1]
        pyautogui.moveTo(self.pos_x+650,self.pos_y+50)
        pyautogui.click()
        sleep(1)
        pyautogui.moveTo(self.base_x+850,self.base_y +610)
        pyautogui.click()
        sleep(3)