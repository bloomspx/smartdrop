
from enum import Enum

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    WAITINGTOUNLOCKBOX = 1,
    TAKINGORDERPICTURE = 2,
    KEYINGINORDERS = 3,
    CONFIRMINGMOREORDERS = 4,
    WAITINGTOLOCKBOX = 5

class LimitSwitchState(Enum):
    OPEN = "open"
    CLOSED = "closed"

lock_state = LockState.LOCKED
process_state = ProcessState.WAITINGTOUNLOCKBOX
passcode = "4789"
limit_switch_state = LimitSwitchState.CLOSED

def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED

def lock():
    global lock_state
    lock_state = LockState.LOCKED

def state_machine():
    global lock_state
    global process_state
    if process_state == ProcessState.WAITINGTOUNLOCKBOX and lock_state == LockState.LOCKED:
        user_input = input("Enter order passcode: ")
        # Insert PUB passcode and receive confirmation from MQTT here
        if user_input == passcode:
            print("Correct passcode")
            unlock()
            process_state = ProcessState.TAKINGORDERPICTURE
        else:
            lock()
            print("Incorrect passcode, please key in again")
    elif process_state == ProcessState.TAKINGORDERPICTURE:
        print("Hold up your order to the camera")
        user_input = input("Press # to take picture")
        if user_input == "#":
            # Wait for S3 response that picture has been uploaded
            print("Picture taken")
            process_state = ProcessState.KEYINGINORDERS
        else:
            print("Please press # to take picture")
        process_state = ProcessState.CONFIRMINGMOREORDERS
    elif process_state == ProcessState.CONFIRMINGMOREORDERS:
        user_input = input("Do you have more orders? (y/n) ")
        if user_input == "y":
            process_state = ProcessState.KEYINGINORDERS
        else:
            print("Thank you, please close the door")
            process_state = ProcessState.WAITINGTOLOCKBOX
    elif process_state == ProcessState.KEYINGINORDERS:
        user_input = input("Enter order passcode: ")
        if user_input == passcode:
            print("Correct passcode")
            unlock()
            process_state = ProcessState.TAKINGORDERPICTURE
        else:
            # User may want to break out of keying in sequence and just lock the door. This is the difference between the initial WAITINGTOUNLOCKBOX State
            print("Incorrect passcode, please key in again or press # to begin locking sequence")
            if user_input == "#":
                process_state = ProcessState.WAITINGTOLOCKBOX
            else:
                process_state = ProcessState.KEYINGINORDERS
    elif process_state == ProcessState.WAITINGTOLOCKBOX:
        # Simulate the limit switch being in contact with the door 
        limit_switch_state = input("Is the door closed? (closed/open)")
        if limit_switch_state == LimitSwitchState.CLOSED.value:
            user_input = input("Press # to lock")
            if user_input == "#":
                lock()
                process_state = ProcessState.WAITINGTOUNLOCKBOX
        else:
            print("Please close the door properly")

while True:
    state_machine()

