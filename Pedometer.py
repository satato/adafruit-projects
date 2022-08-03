#necessary import statements
from adafruit_circuitplayground import cp
import time
import math

#sets the default step goal
default = 500
stepGoal = default
stepCount = 0
displayed = False
touch_tracker = []

#lowers brightness of LEDs bc good lord
cp.pixels.brightness = 0.2

#defines a function which reads out the current step goal (and subsequently, step count as well)
def read_goal(goal, count):
    cp.pixels.fill((0,255,0))

    cp.play_file('step goal.wav')
    step_goal = str(goal)
    time.sleep(0.2)
    for digit in step_goal:
        cp.play_file('mobile banking/{}.wav'.format(int(digit)))

    cp.pixels.fill(0)
    time.sleep(0.2)
    read_count(count)


#defines a function which reads out the current step count
def read_count(count):
    cp.pixels.fill((0,255,0))

    cp.play_file('current steps.wav')
    steps = str(count)
    time.sleep(0.2)
    for digit in steps:
        cp.play_file('mobile banking/{}.wav'.format(int(digit)))

    cp.pixels.fill(0)


#defines a function which flashes all LEDs red twice
def red_flasher():
    cp.pixels.fill((255,0,0))
    time.sleep(0.5)
    cp.pixels.fill(0)
    time.sleep(0.5)
    cp.pixels.fill((255,0,0))
    time.sleep(0.5)
    cp.pixels.fill(0)


#defines a function for scaling down a ratio for display with the 10 NeoPixel LEDs
def scale_value(value,maxValue):
    chunk = maxValue / 10
    #scales ratio of a value to the maxValue for display with the 10 LEDs
    return math.floor(value/chunk)


#defines a function to set/reset the display
def display(value,maxValue):
    for index in range(len(cp.pixels)):
        if index < scale_value(value,maxValue):
            cp.pixels[index] = (0,0,255)
        else:
            cp.pixels[index] = 0


while True:
    #switch on = tracking/display mode
    if cp.switch:
        #if the display has not yet been set/updated, do so
        if not(displayed):
            display(stepCount,stepGoal)
            displayed = True

        #if the board detects a step (using shake), increase count
        #TBI - need to adjust shake sensitivity to sense steps
        if cp.shake(shake_threshold = 11):
            stepCount += 1
            #indicates display is not updated
            displayed = False
            print("step:",stepCount)

    #switch off = settings mode
    else:
        displayed = False
        #button A increases step goal by default number of steps
        if cp.button_a:
            stepGoal += default
            time.sleep(0.2)
            print(stepGoal)

        #button B decreases step goal by default number of steps, with a minimum goal of default
        if cp.button_b:
            stepGoal -= default
            if stepGoal < default:
                stepGoal = default
            time.sleep(0.2)
            print(stepGoal)

        #triple press of A3 reads out current step goal and current step count
        if cp.touch_A2:
            touch_tracker.append('3')
            if len(touch_tracker) == 3:
                if touch_tracker[0] == '3' and touch_tracker[1] == '3' and touch_tracker[2] == '3':
                    cp.pixels.fill((0,255,0))
                    read_goal(stepGoal,stepCount)
                    cp.pixels.fill(0)
                else:
                    #flashes red to indicate invalid input
                    red_flasher()
                touch_tracker = []
            time.sleep(0.2)

        #triple press of A4 reads out ONLY current step count
        if cp.touch_A5:
            touch_tracker.append('4')
            if len(touch_tracker) == 3:
                if touch_tracker[0] == '4' and touch_tracker[1] == '4' and touch_tracker[2] == '4':
                    cp.pixels.fill((0,255,0))
                    read_count(stepCount)
                    cp.pixels.fill(0)
                else:
                    #flashes red to indicate invalid input
                    red_flasher()
                touch_tracker = []
            time.sleep(0.2)
