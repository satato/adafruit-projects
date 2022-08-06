from adafruit_circuitplayground import cp
import time
import rtc
import functions_lib

r = rtc.RTC()
switch_pos = cp.switch
cp.pixels.brightness = 0.2

def read_time(hour,minute):
    if hour == 0:
        hour = 12

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


#updates the time display accordingly
def update_time(minute,hour):
    cp.pixels.auto_write = False

    cp.pixels.fill(0)
    if hour == 11:
        if minute % 10 == 1:
            cp.pixels[0] = functions_lib.colors_dict["purple"]
            cp.pixels[9] = (255,255,255)
    elif minute % 10 == hour:
        display_color = "purple"
        cp.pixels[hour - 1] = functions_lib.colors_dict[display_color]
    else:
        #updates hour in white
        if hour != 0:
            cp.pixels[hour - 1] = (255,255,255)
        #updates minute in corresponding color
        display_min = minute % 10

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

        if display_min != 0:
            cp.pixels[display_min - 1] = functions_lib.colors_dict[display_color]

    cp.pixels.show()


set_time()
print("current time:",r.datetime[3],":",r.datetime[4])
update_time(r.datetime[4],r.datetime[3])

last_hour = r.datetime[3]
last_min = r.datetime[4]

while True:
    #if touchpad A6 is pressed, reads out the time
    if cp.touch_A6:
        read_time(r.datetime[3],r.datetime[4])

    if r.datetime[3] != last_hour or r.datetime[4] != last_min:
        update_time(r.datetime[4],r.datetime[3])

