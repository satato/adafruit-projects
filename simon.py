from adafruit_circuitplayground import cp
import time
import random
#A1 = red 5,6,7
#A2 = green 7,8,9
#A5 = yellow 0,1,2
#A6 = blue 2,3,4

#uses the red LED as an "on and running" indicator
cp.red_led = True

#by default, no game is being played
playing = False

#defines the RGB values of the colors being used
colors = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "yellow": (255,255,0)
}

#defines the color options for simon to choose from
simonColors = ["red","green","blue","yellow"]

#defines a function for the red option displaying
def playRed():
    cp.pixels[5] = colors["red"]
    cp.pixels[6] = colors["red"]
    cp.pixels[7] = colors["red"]
    cp.start_tone(329.63)


#defines a function for the green option displaying
def playGreen():
    cp.pixels[7] = colors["green"]
    cp.pixels[8] = colors["green"]
    cp.pixels[9] = colors["green"]
    cp.start_tone(196.00)


#defines a function for the blue option displaying
def playBlue():
    cp.pixels[0] = colors["blue"]
    cp.pixels[1] = colors["blue"]
    cp.pixels[2] = colors["blue"]
    cp.start_tone(293.66)


#defines a function for the yellow option displaying
def playYellow():
    cp.pixels[2] = colors["yellow"]
    cp.pixels[3] = colors["yellow"]
    cp.pixels[4] = colors["yellow"]
    cp.start_tone(261.63)


#defines a function for defining and continuing the Simon pattern
def simonSays(lastSimon, playing):
    #randomly decides the next color addition to the pattern
    lastSimon.append(simonColors[random.randrange(0,4)])

    #causes the lights to flash in the correct color and order based on the pattern so far
    for item in lastSimon:
        if item == "red":
            playRed()
        elif item == "green":
            playGreen()
        elif item == "blue":
            playBlue()
        else:
            playYellow()
        time.sleep(1)
        cp.stop_tone()
        cp.pixels.fill((0,0,0))
        time.sleep(0.25)

    #after the colors have flashed, guessing begins!
    guessTime(lastSimon, playing)


#defines a function for allowing the player to guess along with the pattern after Simon says
def guessTime(lastSimon, playing):
    guessing = True
    guessIndex = 0
    guess = ""

    #loops guessing until the player successfully finishes the round or the game ends
    while guessing:
        #if the player has guessed successfully and reached the end of the simon round, end guessing
        if guessIndex == len(lastSimon):
            guessing = False
        #otherwise, continue guessing until end of round or guess is wrong
        else:
            touched = False
            #takes a guess and lights up accordingly
            while not(touched):
                if cp.touch_A1:
                    touched = True
                    guess = "red"
                    playRed()
                    time.sleep(1)
                if cp.touch_A2:
                    touched = True
                    guess = "green"
                    playGreen()
                    time.sleep(1)
                if cp.touch_A5:
                    touched = True
                    guess = "blue"
                    playBlue()
                    time.sleep(1)
                if cp.touch_A6:
                    touched = True
                    guess = "yellow"
                    playYellow()
                    time.sleep(1)
                cp.stop_tone()

            cp.pixels.fill((0,0,0))

            #checks whether the guess is correct. if it is, continue the loop
            if guess == lastSimon[guessIndex]:
                guessIndex += 1
            #if guess is incorrect, loop ends and game ends after the whole board flashes red twice
            else:
                guessing = False
                playing = False
                cp.pixels.fill(colors["red"])
                time.sleep(0.5)
                cp.pixels.fill((0,0,0))
                time.sleep(0.5)
                cp.pixels.fill(colors["red"])
                time.sleep(0.5)
                cp.pixels.fill((0,0,0))

        print("GUESS: " + guess)
    #once the guessing loop ends, checks whether the round ends or the game ends and acts accordingly
    if playing:
        time.sleep(1)
        simonSays(lastSimon, playing)
    #if the game is over, simply returns to close out the method
    else:
        return


#for the entirety of the program running, if a game is not in progress and button A is pressed, a game will start
while True:
    if not(playing) and cp.button_a:
        playing = True
        simonSays([], playing)
