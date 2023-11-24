# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

from enum import Enum
import RPi.GPIO as GPIO
import time

######## CONSTANTS ########

# These are the GPIO pin numbers where the
# lines of the keypad matrix are connected
L1 = 5
L2 = 6
L3 = 13
L4 = 19
# These are the four columns
C1 = 12
C2 = 16
C3 = 20

LockPin = 18
LimitSwitchPin = 23

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    WAITINGTOUNLOCKBOX = 1,
    KEYINGINORDERS = 2,
    CONFIRMINGMOREORDERS = 3,
    LOCKBOX = 4
    
    
# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed = -1

secretCode = "4789"
input = ""
lock_state = LockState.LOCKED
process_state = ProcessState.WAITINGTOUNLOCKBOX

# Sets all lines to a specific state. This is a helper
# for detecting when the user releases a button
def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)

def checkSpecialKeys():
    global input
    pressed = False

    GPIO.output(L4, GPIO.HIGH)

    if (GPIO.input(C1) == 1):
        if len(input)!=0:
          input = input[:-1]
        print("Backspace")
        pressed = True

    if (not pressed and GPIO.input(C3) == 1):
        print(input)
        if input == secretCode:
            print("Code correct!")
            unlock()
        else:
            print("Incorrect code!")
            # TODO: Sound an alarm, send an email, etc.
        pressed = True
        input = ""

    GPIO.output(L4, GPIO.LOW)
    return pressed

def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED
    GPIO.output(18, 1)

def lock():
    global lock_state
    lock_state = LockState.LOCKED
    GPIO.output(18, 0)
    
# reads the columns and appends the value, that corresponds
# to the button, to a variable
def readLine(line, characters):
    global input
    # We have to send a pulse on each line to
    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        input = input + characters[0]
    if(GPIO.input(C2) == 1):
        input = input + characters[1]
    if(GPIO.input(C3) == 1):
        input = input + characters[2]
    GPIO.output(line, GPIO.LOW)
# State Machine
def state_machine():
    global process_state
    if process_state == ProcessState.WAITINGTOUNLOCKBOX:
        if not checkSpecialKeys():
            readLine(L1, ["1","2","3"])
            readLine(L2, ["4","5","6"])
            readLine(L3, ["7","8","9"])
            readLine(L4, ["*","0","#"])
            time.sleep(0.1)
        else:
            time.sleep(0.1)
        lock()
    else:
        unlock()

# Main Function
if __name__ == "__main__":
    # Setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LimitSwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    switch_state = GPIO.input(LimitSwitchPin)
    prev_switch_state = switch_state
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)

    # Use the internal pull-down resistors
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LockPin, GPIO.OUT)

    try:
        while True:
            switch_state = GPIO.input(LimitSwitchPin)
            # Check if the button state has changed
            if switch_state != prev_switch_state:
                if switch_state == GPIO.HIGH:
                    print("The limit switch: TOUCHED -> UNTOUCHED")
                else:
                    print("The limit switch: UNTOUCHED -> TOUCHED")
                prev_switch_state = switch_state


            if switch_state == GPIO.HIGH:
                print("The limit switch: UNTOUCHED")
            else:
                print("The limit switch: TOUCHED")
            if lock_state == LockState.LOCKED:
                lock()
            else:
                unlock()
            print(input)
            # If a button was previously pressed,
            # check, whether the user has released it yet
            if keypadPressed != -1:
                setAllLines(GPIO.HIGH)
                if GPIO.input(keypadPressed) == 0:
                    keypadPressed = -1
                else:
                    time.sleep(0.1)
            # Otherwise, just read the input
            else:
                if not checkSpecialKeys():
                    readLine(L1, ["1","2","3"])
                    readLine(L2, ["4","5","6"])
                    readLine(L3, ["7","8","9"])
                    readLine(L4, ["*","0","#"])
                    time.sleep(0.1)
                else:
                    time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nApplication stopped!")
    finally:
        GPIO.cleanup()
