This repository contains several projects, each .py file containing the code for a particular project, for use with a compatible Adafruit Circuit Playground or Circuit Playground Express board. This repository also includes any additional files (and folders) that are necessary to have on the board at the time of running a particular program (some programs require use of additional sound files, etc. for full functionality). Each of these programs were programmed and tested with an Adafruit Circuit Playground Express board. The programs within this repository, as well as what they do, are as follows:

- simon.py: 
    This project runs a simple game of Simon on a compatible circuit board, selecting a random color (out of the 4 available, each assigned a corresponding     tone and section of the board to light up) and waiting for the user to match it, in sequence, progressively adding more and more to the sequence until     the player fails to match it correctly - at which point the game comes to a halt. Theoretically, players should be able to start a new game after the       first one terminates, with use of the board's buttons, but it appears to quit the program entirely - seemingly due to the board's limited memory      
    capacity. I have yet to remedy this.
    
- Fuel Gauge Project.py
    This project is designed to mimic a sort of fuel gauge - such as that of a car. Pressing button A will increase the "gas" that the imagined tank holds,     until the tank itself is filled. Pressing button B will decrease this level, until the tank reaches zero. When the imagined tank is empty, the board       shines all LEDs in red. When the tank is full, the LEDs turn green. When the tank is partially filled, the rough percentage/ratio of the tank filled is     displayed in blue with the LEDs. When the switch is in the "on" position, the program will run as expected. Moving the slide switch into the "off"         position removes the LED display (since it is very bright).

- Pedometer.py
    This project is a genuine pedometer. It holds a default value for the step goal (which is equal to the step goal increment used in the "settings"           mode), a step goal, and a step count. When the slide switch is in the "on" position, the program runs as expected (in "tracking/display mode), tracking     the user's steps and utilizing the 10 NeoPixel LEDs to display the rough percentage of their step goal that has been met with blue light. When the         switch is in the "off" position, the program is in what I call "settings" mode, where steps are not being tracked and the display is removed               temporarily (it will update once put back in tracking/display mode). In "settings" mode, the user may triple press the capacitive touch pad A2 to hear     their currently set step goal, and then current step count read out to them. If the user triple pressed the capacitive touch pad A5, the board will         read out just their current step count aloud. Pressing button A will increment the user's step goal by whatever the "default" value is set to in the       code (in this case, 500), and pressing button B will decrement by the same, with a minimum step goal of the default value.

- Clock (Version 1)
    This project is my first attempt at making use of the Adafruit Circuit Playground Express as a clock (in particular, for use as a watch). While the         lack of display and meager 10 NeoPixel LEDs make this something of a challenge, this rendition makes use of the buttons, switch, and one of the             capacitive touch pads (A6) on the board to set and read out the time aloud (similar to the pedometer project). The NeoPixel LED display is also used,       as follows:
    When the switch is in the "on" position, the board displays the hour (1-12), with hours 1-10 being displayed quite normally (shining in white) slowly       filling up the board with light as the hours progress. When the board reaches 11 o'clock, however, only the left half of the LEDs (0-4) shine, and when     it is 12 o'clock, the whole board is lit.
    When the switch is in the "off" position, the board displays the minutes (0-59), quite similarly, based on the following color key:
    0-9: blue
    10-19: green
    20-29: yellow
    30-39: orange
    40-49: red
    50-59: pink
    And even once the program is running, pressing touch pad A6 will read out the currently displayed time.
    
- Clock (Version 2)
    This project utilizes much of the same code as its predecessor, and maintains the same color code for the minutes:
    0-9: blue
    10-19: green
    20-29: yellow
    30-39: orange
    40-49: red
    50-59: pink
    That being said, there is one key difference between Clock Version 1 and Clock Version 2: the display.
    The display for this one makes use of individual LEDs (rather than the group of them, as before) to indicate the current hour and minute on the same       LED display without need for the slide switch. Whichever LED the minute reaches will be lit up according to the previously mentioned color key,             whereas the hour will always be displayed in white, making the two easy to differentiate. If the two happen to overlap, then the overlapping LED will       display in purple. As this makes determining the minute somewhat more difficult to gauge, it is encouraged to use touchpad A6 to read out the time if       this occurs, or simply wait a minute for the display to update with more clarity.
    If the hour is 12, there is no LED for the hour on the board. Whereas if the hour is 11, both the 1st (index 0) and 10th (index 9) LEDs will be lit up     in white to indicate such.
