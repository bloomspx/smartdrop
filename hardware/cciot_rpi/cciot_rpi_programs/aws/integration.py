from enum import Enum
import RPi.GPIO as GPIO
import gui

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    START_DELIVERY_SEQUENCE = 0,
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
device_id = "simple_id"
most_recent_keyed_in_passcode = ""
mqtt_connection = None


# Setup GPIO
def hardware_setup():
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
    # lock()
    return

if __name__ == "__main__":
    try:
        # mqtt_connection = aws_setup()
        hardware_setup()
        # device_id = getSerial()
        print(device_id)
        ctk = gui.ctkApp()

    except KeyboardInterrupt:
        GPIO.cleanup()