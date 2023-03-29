import pyautogui
import math
from time import sleep
import random

class Shop:

    base_x = 0
    base_y = 0
    window_w = 0
    window_h = 0
    

    def __init__(self, base, w, h):

        self.base_x = base[0]
        self.base_y = base[1]
        self.window_w = w
        self.window_h = h
        
        
    def scroll(self):
        pyautogui.moveTo(self.base_x + (self.window_w/2),self.base_y + (self.window_h/2))
        #pyautogui.click()
        pyautogui.scroll(-5000)

    def click_here(self, point):
        
        x,y = point[0]
        
        x += random.randrange(-7, 7)
        y += random.randrange(-15, 15)
        
        pyautogui.moveTo(self.base_x + x,self.base_y + y)
        pyautogui.click()

    def find_closest(self, main_point, other_points):
        
        the_point = []
        closest_point = None
        closest_distance = float('inf')
        for point in other_points:
            distance = math.sqrt((point[0]-main_point[0])**2 + (point[1]-main_point[1])**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_point = point
        the_point.append(closest_point)
         
        return the_point