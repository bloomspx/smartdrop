from enum import Enum
import gui

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    START_DELIVERY_SEQUENCE = 0,
    WAITING_TO_UNLOCK_BOX = 1,
    TAKING_ORDER_PICTURE = 2,
    KEYING_IN_ORDERS = 3,
    CONFIRMING_MORE_ORDERS = 4,
    CONFIRM_LOCK_SEQUENCE = 5,
    WAITING_TO_LOCK_BOX = 6

class LimitSwitchState(Enum):
    OPEN = "open"
    CLOSED = "closed"

lock_state = LockState.LOCKED
process_state = ProcessState.START_DELIVERY_SEQUENCE
passcode = ["4789", "1234", "2345"]
limit_switch_state = LimitSwitchState.CLOSED

def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED

def lock():
    global lock_state
    lock_state = LockState.LOCKED

def state_machine(ctk):
    global lock_state
    global process_state
    if process_state == ProcessState.START_DELIVERY_SEQUENCE:
        user_input = input("Press # to start delivery sequence: ")
        if user_input == "#":
            process_state = ProcessState.WAITING_TO_UNLOCK_BOX
        else:
            user_input = ""
    elif process_state == ProcessState.WAITING_TO_UNLOCK_BOX:
        ctk.select_frame_by_name("step_2")
        user_input = input("Enter order passcode: ")
        # Insert PUB passcode and receive confirmation from MQTT here
        if user_input in passcode:
            print("Correct passcode")
            unlock()
            process_state = ProcessState.TAKING_ORDER_PICTURE
        else:
            lock()
            print("Incorrect passcode, please key in again")
    elif process_state == ProcessState.TAKING_ORDER_PICTURE:
        ctk.select_frame_by_name("step_3")
        print("Place the item in the box")
        user_input = input("Press # to take picture")
        if user_input == "#":
            # Wait for S3 response that picture has been uploaded
            print("Picture taken")
        else:
            user_input = ""
            print("Please press # to take picture")
        process_state = ProcessState.CONFIRMING_MORE_ORDERS
    elif process_state == ProcessState.CONFIRMING_MORE_ORDERS:
        ctk.select_frame_by_name("step_4")
        user_input = input("Do you have more orders? Press # to key in more orders, * to lock box ")
        if user_input == "#":
            ctk.select_frame_by_name("step_2")
            process_state = ProcessState.KEYING_IN_ORDERS
        elif user_input == "*":
            ctk.select_frame_by_name("step_5")
            print("Thank you, please close the door")
            process_state = ProcessState.WAITING_TO_LOCK_BOX
        else: 
            # Always clear the user input if the user presses any other button
            user_input = ""
    elif process_state == ProcessState.KEYING_IN_ORDERS:
        print("Key in additional order passcodes. To lock the box, empty the input and press *")
        user_input = input("Enter order passcode: ")
        if user_input in passcode:
            print("Correct passcode")
            unlock()
            process_state = ProcessState.TAKING_ORDER_PICTURE
        elif user_input == "*":
            process_state = ProcessState.WAITING_TO_LOCK_BOX
    elif process_state == ProcessState.WAITING_TO_LOCK_BOX:
        # Simulate the limit switch being in contact with the door 
        limit_switch_state = input("Is the door closed? (closed/open)")
        if limit_switch_state == LimitSwitchState.CLOSED.value:
            lock()
            ctk.select_frame_by_name("step_1")
            process_state = ProcessState.START_DELIVERY_SEQUENCE
        else:
            print("Please close the door properly")

if __name__ == "__main__":
    ctk = gui.ctkApp()
    while True:
        state_machine(ctk)