from adafruit_circuitplayground import cp
import time
import rtc
import functions_lib

cp.pixels.brightness = 0.2
switch_pos = cp.switch
display_color = "white"

color_defs = functions_lib.colors_dict

r = rtc.RTC()

def read_time(hour,minute):
    cp.play_file('wavs/hour.wav')
    for digit in str(hour):
        cp.play_file('wavs/{}.wav'.format(int(digit)))

    cp.play_file('wavs/minute.wav')
    for digit in str(minute):
        cp.play_file('wavs/{}.wav'.format(int(digit)))


def set_time():
    done = False
    #default time is 00:00 - perfect midnight
    hour = 0
    minute = 0

    #default mode = set hour
    mode = True
    modeChanged = True

    while not(done):
        #switches mode if touchpad A6 is pressed
        if cp.touch_A6:
            if mode:
                mode = False
            else:
                mode = True

            modeChanged = True

            #reads out the currently set time for reference
            read_time(hour,minute)

            time.sleep(0.2)

        #requests input
        if mode and modeChanged:
            #prompts user to set hour
            cp.play_file('wavs/set_hour.wav')
            modeChanged = False
        elif modeChanged:
            #prompts user to set minute
            cp.play_file('wavs/set_minute.wav')
            modeChanged = False

        #button A increases by 1
        if cp.button_a:
            if mode:
                hour += 1
                if hour == 12:
                    hour = 0
            else:
                minute += 1
                if minute == 60:
                    minute = 0

            time.sleep(0.2)

        #button B decreases by 1
        if cp.button_b:
            if mode:
                hour -= 1
                if hour == -1:
                    hour = 11
            else:
                minute -= 1
                if minute == -1:
                    minute = 59

            time.sleep(0.2)

        #if the switch position is changed, save time
        if cp.switch != switch_pos:
            r.datetime = time.struct_time((2022, 8, 6, hour, minute, 0, 0, -1, -1))
            done = True

set_time()
print("current time:",r.datetime[3],":",r.datetime[4])

while True:
    #if touchpad A6 is pressed, reads out the time
    if cp.touch_A6:
        read_time(r.datetime[3],r.datetime[4])

    #if switch is in "on" position, displays the hour
    if cp.switch:
        display_color = "white"
        #updates display
        if r.datetime[3] < 11:
            functions_lib.display(r.datetime[3],10,color_defs[display_color])
        elif r.datetime[3] == 11:
            functions_lib.display(5,10,color_defs[display_color])
        else:
            cp.pixels.fill(color_defs[display_color])

    #otherwise, displays the minutes
    else:
        #adjusts display color to determine minutes more easily with the 10 LEDs available
        if r.datetime[4] < 10:
            display_color = "blue"
        elif r.datetime[4] < 20:
            display_color = "green"
        elif r.datetime[4] < 30:
            display_color = "yellow"
        elif r.datetime[4] < 40:
            display_color = "orange"
        elif r.datetime[4] < 50:
            display_color = "red"
        elif r.datetime[4] < 60:
            display_color = "pink"

        #adjusts for display
        display_min = r.datetime[4] % 10
        #updates display
        functions_lib.display(display_min,10,color_defs[display_color])
