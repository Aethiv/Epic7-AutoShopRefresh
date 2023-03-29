# Epic7-AutoShopRefresh
Auto shop refresh tool for epic7

# How it works
Currrently set up for LD Player, to change the emulator edit the line "wincap = WindowCapture('LDPlayer')" to an emulator of your choice.
It uses image detection for every action it performs, including buttons.
Randomises each click by few pixels.
Tested for 720p resolution.

It needs the emulator to be the active window

Using openCV detects both Covenant and Mystic Bookmakmarks and proceeds to buy them
When doesnt find any, scrolls the shop page and refreshes it using skystones

# TODO

* different resolutions
* work in an inactive window
* GPU acceleration or CPU multithread
