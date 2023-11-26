
from enum import Enum
from aws_helper import *
import config

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

lock_state = LockState.LOCKED
process_state = ProcessState.START_DELIVERY_SEQUENCE
passcode = ["589494", "213355", "252845"]
limit_switch_state = LimitSwitchState.CLOSED
deviceID = "simple_id"
most_recent_keyed_in_passcode = ""

def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED

def lock():
    global lock_state
    lock_state = LockState.LOCKED


def state_machine(mqtt_connection):
    global lock_state
    global process_state
    global most_recent_keyed_in_passcode
    # -------- START DELIVERY SEQUENCE --------
    if process_state == ProcessState.START_DELIVERY_SEQUENCE:
        user_input = input("Press # to start delivery sequence: ")
        if user_input == "#":
            process_state = ProcessState.WAITINGTOUNLOCKBOX
        else:
            user_input = ""
    # -------- WAITING TO UNLOCK BOX --------
    elif process_state == ProcessState.WAITINGTOUNLOCKBOX:
        user_input = input("Enter order passcode: ")
        # AWS PUB passcode and receive confirmation from MQTT here     
        validate_payload = format_validate_payload(deviceID, user_input)
        publish_to_validate_topic(mqtt_connection, validate_payload)
        received_payload = wait_for_received_payload()
        if received_payload:
            if validate_passcode_payload(decode_payload(received_payload)):
            # if user_input in passcode:
                print("Correct passcode")
                unlock()
                most_recent_keyed_in_passcode = user_input
                process_state = ProcessState.TAKINGORDERPICTURE
            else:
                lock()
                print("Incorrect passcode, please key in again")
            invalidate_payload()
    # -------- TAKING ORDER PICTURE --------
    elif process_state == ProcessState.TAKINGORDERPICTURE:
        print("Place the item in the box")
        user_input = input("Press # to take picture")
        if user_input == "#":
            # AWS PUB take photo and receive confirmation from MQTT here
            take_photo_payload = format_take_photo_payload(deviceID, most_recent_keyed_in_passcode)
            publish_to_take_photo_topic(mqtt_connection, take_photo_payload)
            received_payload = wait_for_received_payload()
            if received_payload:
                if validate_take_photo_payload(decode_payload(received_payload)):
                    print("Picture taken")
                    process_state = ProcessState.CONFIRMINGMOREORDERS
                else:
                    print("Picture not taken")
                    user_input = ""
                    print("Please press # to take picture")
            invalidate_payload()
    # -------- CONFIRMING MORE ORDERS --------
    elif process_state == ProcessState.CONFIRMINGMOREORDERS:
        user_input = input("Do you have more orders? Press # to key in more orders, * to lock box ")
        if user_input == "#":
            process_state = ProcessState.KEYINGINORDERS
        elif user_input == "*":
            print("Thank you, please close the door")
            process_state = ProcessState.CONFIRMLOCKSEQUENCE
        user_input = ""
    # -------- KEYING IN ORDERS --------
    elif process_state == ProcessState.KEYINGINORDERS:
        print("Key in additional order passcodes. To lock the box, empty the input and press *")
        user_input = input("Enter order passcode: ")
        if user_input == "*":
            process_state = ProcessState.CONFIRMLOCKSEQUENCE
        else:
            # AWS PUB passcode and receive confirmation from MQTT here
            validate_payload = format_validate_payload(deviceID, user_input)
            publish_to_validate_topic(mqtt_connection, validate_payload)
            received_payload = wait_for_received_payload()
            if received_payload:
                if validate_passcode_payload(decode_payload(received_payload)):
                    print("Correct passcode")
                    most_recent_keyed_in_passcode = user_input
                    process_state = ProcessState.TAKINGORDERPICTURE
                else:
                    print("Incorrect passcode, please key in again")
            invalidate_payload()
        user_input = ""
    # -------- CONFIRM LOCK SEQUENCE --------
    elif process_state == ProcessState.CONFIRMLOCKSEQUENCE:
        user_input = input("Press * to confirm locking the box, # to return to keying in orders")
        if user_input == "*":
            lock()
            process_state = ProcessState.WAITINGTOLOCKBOX
        elif user_input == "#":
            process_state = ProcessState.KEYINGINORDERS
        user_input = ""
    # -------- WAITING TO LOCK BOX --------
    elif process_state == ProcessState.WAITINGTOLOCKBOX:
        # Simulate the limit switch being in contact with the door 
        limit_switch_state = input("Is the door closed? (closed/open)")
        if limit_switch_state == LimitSwitchState.CLOSED.value:
            lock()
            process_state = ProcessState.START_DELIVERY_SEQUENCE
        else:
            print("Please close the door properly")


if __name__ == "__main__":
    mqtt_connection = aws_setup()
    if mqtt_connection:
        while True:
            state_machine(mqtt_connection)

