from enum import Enum
import RPi.GPIO as GPIO
import time


class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    WAITINGTOUNLOCKBOX = 1,
    TAKINGORDERPICTURE = 2,
    KEYINGINORDERS = 3,
    CONFIRMINGMOREORDERS = 4,
    CONFIRMLOCKSEQUENCE = 5,
    WAITINGTOLOCKBOX = 6

class LimitSwitchState(Enum):
    OPEN = "open"
    CLOSED = "closed"


######## CONSTANTS ########

# These are the GPIO pin numbers where the
# lines of the keypad matrix are connected
L1 = 5
L2 = 6
L3 = 13
L4 = 19
# These are the 3 columns
C1 = 12
C2 = 16
C3 = 20
# Output pin for the lock
LockPin = 18
# Input pin for the limit switch
LimitSwitchPin = 23

user_input = ""
lock_state = LockState.LOCKED
process_state = ProcessState.WAITINGTOUNLOCKBOX
passcodes = ["4789", "1234", "2345"]
limit_switch_state = LimitSwitchState.CLOSED
keypadPressed = -1
switch_state = 1
prev_switch_state = -1

########################################## HELPER FUNCTIONS ##########################################
# Unlock command
def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED
    GPIO.output(18, 1)

# Lock command
def lock():
    global lock_state
    lock_state = LockState.LOCKED
    GPIO.output(18, 0)

# Setup GPIO
def setup():
    global switch_state
    global prev_switch_state
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LimitSwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)

    # Use the internal pull-down resistors
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LockPin, GPIO.OUT)
    lock()
    return

# Reads the columns and appends the value, that corresponds to the button, to a variable
def readLine(line, characters):
    global user_input
    # Sends a pulse on each line to detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        user_input = user_input + characters[0]
    if(GPIO.input(C2) == 1):
        user_input = user_input + characters[1]
    if(GPIO.input(C3) == 1):
        user_input = user_input + characters[2]
    GPIO.output(line, GPIO.LOW)

########################################## STATE SPECIFIC FUNCTIONS ##########################################
## WAITINGTOUNLCOCKBOX ##
# Backspace func
def backspace():
    global user_input
    if len(user_input)!=0:
        user_input = user_input[:-1]
    return

# Confirm user input func
def confirm_passcode():
    global user_input
    global process_state
    print(user_input)
    if user_input in passcodes:
        print("Code correct!")
        unlock()
        process_state = ProcessState.TAKINGORDERPICTURE
    else:
        lock()
    user_input = ""
    return

## TAKINGORDERPICTURES ##
def taking_order_picture():
    global process_state
    # Wait for S3 response that picture has been uploaded
    print("Picture taken")
    process_state = ProcessState.CONFIRMINGMOREORDERS

def invalidate_asterisk_at_photo_state():
    global process_state
    print("Please press # to take picture")
    process_state = ProcessState.TAKINGORDERPICTURE

## CONFIRMINGMOREORDERS ##
def confirm_more_orders():
    global process_state
    process_state = ProcessState.KEYINGINORDERS

def confirm_no_more_orders():
    global process_state
    print("Thank you, please close the door")
    process_state = ProcessState.WAITINGTOLOCKBOX

## KEYINGINORDERS ##
def key_in_additional_orders():
    global user_input
    global process_state
    if user_input in passcodes:
        print("Code correct!")
        unlock()
        process_state = ProcessState.TAKINGORDERPICTURE
    else:
        print("Incorrect passcode, please key in again or press * to begin locking sequence")
        process_state = ProcessState.KEYINGINORDERS
    user_input = ""
    return

def start_locking_sequence():
    global process_state
    global user_input
    if len(user_input) == 0:
        process_state = ProcessState.CONFIRMLOCKSEQUENCE
    else:
        user_input = user_input[:-1]
    return


## CONFIRMLOCKSEQUENCE ##
def confirm_lock_sequence():
    global process_state
    process_state = ProcessState.WAITINGTOLOCKBOX

def return_to_keying_in_orders():
    global process_state
    process_state = ProcessState.KEYINGINORDERS

## WAITINGTOLOCKBOX ##
def lock_box():
    global process_state
    if limit_switch_state == LimitSwitchState.CLOSED:
        lock()
        process_state = ProcessState.WAITINGTOUNLOCKBOX
    else:
        print("Please close the door properly")
    return

def invalid_asterisk_at_locking_state():
    global process_state
    print("Please press # to lock the door")
    process_state = ProcessState.WAITINGTOLOCKBOX

########################################## GENERAL KEYPAD FUNCTIONS ##########################################
def checkSpecialKeys(hash_func, asterisk_func):
    global passcodes
    global process_state
    global user_input
    pressed = False
    GPIO.output(L4, GPIO.HIGH)

    if (GPIO.input(C1) == 1):
        asterisk_func()
        pressed = True

    if (not pressed and GPIO.input(C3) == 1):
        hash_func()
        pressed = True
    GPIO.output(L4, GPIO.LOW)
    return pressed

def keypad_input(hash_func, asterisk_func):
    if not checkSpecialKeys(hash_func, asterisk_func):
        readLine(L1, ["1","2","3"])
        readLine(L2, ["4","5","6"])
        readLine(L3, ["7","8","9"])
        readLine(L4, ["*","0","#"])
        time.sleep(0.1)
    else:
        time.sleep(0.1)

########################################## MAIN STATE MACHINE ##########################################
def state_machine():
    global lock_state
    global process_state
    global keypadPressed
    if keypadPressed != -1:
        setAllLines(GPIO.HIGH)
        if GPIO.input(keypadPressed) == 0:
            keypadPressed = -1
        else:
            time.sleep(0.1)
    else:
        if process_state == ProcessState.WAITINGTOUNLOCKBOX and lock_state == LockState.LOCKED:
            keypad_input(hash_func=confirm_passcode, asterisk_func=backspace)
            # Insert PUB passcode and receive confirmation from MQTT here
        elif process_state == ProcessState.TAKINGORDERPICTURE:
            keypad_input(hash_func=taking_order_picture, asterisk_func=invalidate_asterisk_at_photo_state)
        elif process_state == ProcessState.CONFIRMINGMOREORDERS:
            keypad_input(hash_func=confirm_more_orders, asterisk_func=confirm_no_more_orders)
        elif process_state == ProcessState.KEYINGINORDERS:
            keypad_input(hash_func=key_in_additional_orders, asterisk_func=start_locking_sequence)
        elif process_state == ProcessState.CONFIRMLOCKSEQUENCE:
            print("Please press # to confirm locking sequence. Press * to return to keying in orders")
            keypad_input(hash_func=confirm_lock_sequence, asterisk_func=return_to_keying_in_orders)
        elif process_state == ProcessState.WAITINGTOLOCKBOX:
            keypad_input(hash_func=lock_box, asterisk_func=invalid_asterisk_at_locking_state)

########################################## MAIN DRIVER FUNCTIOn ##########################################
if __name__ == "__main__":
    try:
        setup()
        while True:
            switch_state = GPIO.input(LimitSwitchPin)
            if switch_state != prev_switch_state:
                if switch_state == 0:
                    limit_switch_state = LimitSwitchState.CLOSED
                else:
                    limit_switch_state = LimitSwitchState.OPEN
                prev_switch_state = switch_state
            state_machine()
            print("-------------------------------------------------")
            print("User input: " + user_input)
            print("Lock state: " + str(lock_state))
            print("Process state: " + str(process_state))
            print("Limit switch state: " + str(limit_switch_state))
            print("-------------------------------------------------")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program ended")
