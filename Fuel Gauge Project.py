from adafruit_circuitplayground import cp
import time

cp.pixels.auto_write = False

gasQuantity = 0
tankCapacity = 16
step = 2

#scales the ratio between a given value and maxValue for display with the 10 NeoPixel LEDs
def scale_value(value,maxValue):
    return round(value/maxValue * 9)


while True:
    if cp.switch:
        cp.red_led = False
        if cp.button_a:
            print(gasQuantity)
            if gasQuantity < tankCapacity:
                gasQuantity += step
            if gasQuantity > tankCapacity:
                gasQuantity = tankCapacity
            time.sleep(0.2)
        if cp.button_b:
            print(gasQuantity)
            if gasQuantity > 0:
                gasQuantity -= step
            if gasQuantity < 0:
                gasQuantity = 0
            time.sleep(0.2)

        if gasQuantity == tankCapacity:
            cp.pixels.fill((0,200,0))
        elif gasQuantity == 0:
            cp.pixels.fill((200,0,0))
        else:
            for i in range(10):
                if (i <= scale_value(gasQuantity,tankCapacity) and gasQuantity != 0):
                    cp.pixels[i] = (0,0,150)
                else:
                    cp.pixels[i] = (0,0,0)

        cp.pixels.show()
    else:
        cp.red_led = True
        cp.pixels.fill(0)
        cp.pixels.show()
