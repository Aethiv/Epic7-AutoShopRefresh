import cv2 as cv
from time import sleep
from windowcapture import WindowCapture
from detection import Detection
from shop import Shop


# initialize the WindowCapture class
wincap = WindowCapture('LDPlayer')
cwindow = Shop(wincap.get_screen_position((0,0)), wincap.get_width(), wincap.get_height())

# initialize detection classes
detection_cov = Detection('resources/cov.jpg')
detection_myst = Detection('resources/myst.jpg')
detection_refresh = Detection('resources/refresh.jpg')
detection_confirm = Detection('resources/confirm.jpg')
detection_buy1 = Detection('resources/buy.jpg')
detection_buy_cov = Detection('resources/buy_cov.jpg')
detection_buy_myst = Detection('resources/buy_myst.jpg')

x = '1'
cov_bought = False
myst_bought = False

cov_count = 0
myst_count = 0

skystones_count = 2000

while(skystones_count > 0):
    
    #Time for the animation to finish before locking the frame of the emulator
    sleep(1)
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # Look for the bookmarks
    if cov_bought == False:
        cov_points = detection_cov.find(screenshot, 0.80)
    else:
        cov_points = []

    if myst_bought == False:
        myst_points = detection_myst.find(screenshot, 0.80)
    else:
        myst_points = []

    points = cov_points + myst_points
    
   
    
    if any(points) and x != 'xd1':        
        x = 'xd'
    
    match x:
        case '1':
            cwindow.scroll()
            x = '2'
        case '2':
            ref_point = detection_refresh.find(screenshot, 0.95)
            cwindow.click_here(ref_point)
            x = '3'
        case '3':
            conf_point = detection_confirm.find(screenshot, 0.90)
            cwindow.click_here(conf_point)
            cov_bought = False
            myst_bought = False
            skystones_count -= 3
            x = '1'
        case 'xd':
            buy1_points = detection_buy1.find(screenshot, 0.95)
            cwindow.click_here(cwindow.find_closest(points[0], buy1_points))
            x = 'xd1'
        case 'xd1':
            buy_cov_point = detection_buy_cov.find(screenshot, 0.95)
            buy_myst_point = detection_buy_myst.find(screenshot, 0.95)
            if any(buy_cov_point):
                cwindow.click_here(buy_cov_point)
                cov_bought = True
                cov_count += 1
            elif any(buy_myst_point):
                cwindow.click_here(buy_myst_point)
                myst_bought = True
                myst_count += 1
            x = '1'
    
    print('myst bought: ', myst_count)
    print('cov bought: ', cov_count)
    print('skystones left: ', skystones_count)   
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')

