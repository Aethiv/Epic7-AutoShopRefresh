import cv2 as cv
from time import time
from windowcapture import WindowCapture
from detection import Detection
from time import time
from refresh import Refresh


# initialize the WindowCapture class
wincap = WindowCapture('BlueStacks App Player')
cwindow = Refresh(wincap.get_screen_position((0,0)))
# initialize the Vision class
detection_cov = Detection('resources/cov.jpg')
detection_myst = Detection('resources/myst.jpg')

loop_time = time()
scrolled = False
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    cov_points = detection_cov.find(screenshot, 0.95, 'rectangles')
    myst_points = detection_myst.find(screenshot, 0.95, 'rectangles')

    points = cov_points + myst_points

    if not any(points):
        if not scrolled:
            cwindow.scroll()
            scrolled = True
            print('test1')
        else:
            cwindow.ref()
            scrolled = False
            print('test2')
    else:
        for point in points:
            cwindow.buy(wincap.get_screen_position(point))
        
        

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')

