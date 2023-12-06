from enum import Enum
import customtkinter
import RPi.GPIO as GPIO
from awsHelper import *

########################################## CTINKER GUI ##########################################

class ctkApp(customtkinter.CTk):
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        super().__init__()

        # Set GUI title
        self.title("Smart Delivery System")

        # Set screen width and height
        self.width= 1000
        self.height= 500
        self.geometry("%dx%d" % (self.width, self.height))

        # Set main grid layout 1x2 (navigation frame, content frame)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create initial navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        # Navigation frame content
        # Create title label
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Smart Delivery Box", height=60, text_color=("turquoise4", "turquoise4"), padx=20,
                                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        # Create label for start delivery step
        self.start_delivery_label = self.create_navigation_label(text="Step 1: Start Delivery")
        self.start_delivery_label.grid(row=1, column=0, sticky="ew", padx=20)
        # Create label for enter passcode step
        self.enter_passcode_label = self.create_navigation_label(text="Step 2: Enter Passcode")
        self.enter_passcode_label.grid(row=2, column=0, sticky="ew", padx=20)
        # Create label for photo step
        self.photo_label = self.create_navigation_label(text="Step 3: Place Package in Box")
        self.photo_label.grid(row=3, column=0, sticky="ew", padx=20)
        # Create label for checking more delivery step
        self.check_more_delivery_label = self.create_navigation_label(text="Step 4: Make Another Delivery / \nComplete Delivery")
        self.check_more_delivery_label.grid(row=4, column=0, sticky="ew", padx=20)
        # Create label for close box step
        self.close_box_label = self.create_navigation_label(text="Step 5: Close Box")
        self.close_box_label.grid(row=5, column=0, sticky="ew", padx=20)

        # create initial start delivery frame
        self.start_delivery_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.start_delivery_frame_content1_label = self.create_blue_content_label(self.start_delivery_frame, text="Making a Delivery?")
        self.start_delivery_frame_content2_label = self.create_white_content_label(self.start_delivery_frame, text="Press '#' to start delivery")
        self.start_delivery_frame_content1_label.place(relx=0.5, rely=0.3, anchor="center")       
        self.start_delivery_frame_content2_label.place(relx=0.5, rely=0.6, anchor="center")      
        self.start_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)       

        # create enter passcode frame
        self.enter_passcode_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.enter_passcode_frame_content1_label = self.create_blue_content_label(self.enter_passcode_frame, text="Enter Passcode")
        self.enter_passcode_frame_content2_label = self.create_blue_content_label(self.enter_passcode_frame, text="Press '#' to confirm passcode or '*' to delete character")
        self.enter_passcode_frame_content3_label = self.create_white_content_label(self.enter_passcode_frame, text=user_input)
        self.enter_passcode_frame_content1_label.place(relx=0.5, rely=0.3, anchor="center")  
        self.enter_passcode_frame_content2_label.place(relx=0.5, rely=0.5, anchor="center")  
        self.enter_passcode_frame_content3_label.place(relx=0.5, rely=0.7, anchor="center")
        self.enter_passcode_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)         
        # create photo frame
        self.photo_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.photo_frame_content1_label = self.create_blue_content_label(self.photo_frame, text="Place package in the box")
        self.photo_frame_content2_label =self.create_white_content_label(self.photo_frame, text="Press '#' once item is placed")
        self.photo_frame_content1_label.place(relx=0.5, rely=0.3, anchor="center")       
        self.photo_frame_content2_label.place(relx=0.5, rely=0.6, anchor="center")   
        self.photo_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create check more delivery frame
        self.check_more_delivery_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.check_more_delivery_content1_label = self.create_blue_content_label(self.check_more_delivery_frame, text="Do you have more deliveries?")
        self.check_more_delivery_content2_label = self.create_white_content_label(self.check_more_delivery_frame, text="Press '#' for more deliveries \nor '*' to complete delivery")
        self.check_more_delivery_content1_label.place(relx=0.5, rely=0.3, anchor="center")       
        self.check_more_delivery_content2_label.place(relx=0.5, rely=0.6, anchor="center")   
        self.check_more_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create close box frame
        self.close_box_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.close_box_frame_content1_label = self.create_blue_content_label(self.close_box_frame, text="Close Box")
        self.close_box_frame_content1_label.place(relx=0.5, rely=0.5, anchor="center")  
        self.close_box_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create wait for validation frame
        self.wait_for_validation_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.wait_for_validation_frame_content1_label = self.create_blue_content_label(self.wait_for_validation_frame, text="Validating passcode...")
        self.wait_for_validation_frame_content1_label.place(relx=0.5, rely=0.5, anchor="center")
        self.wait_for_validation_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create wait for validation frame
        self.please_wait_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.please_wait_frame_content1_label = self.create_blue_content_label(self.please_wait_frame, text="Please wait...")
        self.please_wait_frame_content1_label.place(relx=0.5, rely=0.5, anchor="center")
        self.please_wait_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)

        # select default frame
        self.select_frame_by_name(ProcessState.STARTDELIVERYSEQUENCE)

    def create_navigation_label(self, text):
        return customtkinter.CTkLabel(self.navigation_frame,height=(self.height-80)/6, text=text, corner_radius=8,
            fg_color=("gray75", "gray25"), 
            compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 20)

    def create_blue_content_label(self, frame, text):
        return customtkinter.CTkLabel(frame, text=text,
            text_color=("gray10", "CadetBlue1"),
            font=customtkinter.CTkFont(size=25, weight="bold"), padx = 20)

    def create_white_content_label(self, frame, text):
        return customtkinter.CTkLabel(frame, text=text,
            text_color=("gray10", "gray99"),
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True), padx = 20)

    def forget_all_frames(self):
        self.start_delivery_frame.grid_forget()
        self.enter_passcode_frame.grid_forget()
        self.photo_frame.grid_forget()
        self.check_more_delivery_frame.grid_forget()
        self.close_box_frame.grid_forget()
        self.wait_for_validation_frame.grid_forget()
        self.please_wait_frame.grid_forget()

    def select_frame_by_name(self, name, user_input=""):
        # set color for current navigation label
        self.start_delivery_label.configure(fg_color=("gray30", "gray30") if name == ProcessState.STARTDELIVERYSEQUENCE else "transparent")
        self.start_delivery_label.configure(text_color=("gray10", "gray90")if name == ProcessState.STARTDELIVERYSEQUENCE else ("gray10", "gray40"))
        self.enter_passcode_label.configure(fg_color=("gray30", "gray30")  if name == ProcessState.WAITINGTOUNLOCKBOX  or name == ProcessState.KEYINGINORDERS or name == ProcessState.WAITINGFORUNLOCKBOXPAYLOAD or name == ProcessState.WAITINGFORADDITIONALORDERSPAYLOAD else "transparent")
        self.enter_passcode_label.configure(text_color=("gray10", "gray90") if name == ProcessState.WAITINGTOUNLOCKBOX or name == ProcessState.KEYINGINORDERS or name == ProcessState.WAITINGFORUNLOCKBOXPAYLOAD or name == ProcessState.WAITINGFORADDITIONALORDERSPAYLOAD else ("gray10", "gray40"))
        self.photo_label.configure(fg_color=("turquoise4", "turquoise4")  if name == ProcessState.TAKINGORDERPICTURE or  name == ProcessState.WAITINGFORPICTUREPAYLOAD else "transparent")
        self.photo_label.configure(text_color=("gray10", "gray90") if name == ProcessState.TAKINGORDERPICTURE or  name == ProcessState.WAITINGFORPICTUREPAYLOAD else ("gray10", "gray40"))
        self.check_more_delivery_label.configure(fg_color=("turquoise4", "turquoise4")  if name == ProcessState.CONFIRMINGMOREORDERS else "transparent")
        self.check_more_delivery_label.configure(text_color=("gray10", "gray90") if name == ProcessState.CONFIRMINGMOREORDERS else ("gray10", "gray40"))
        self.close_box_label.configure(fg_color=("turquoise4", "turquoise4") if name == ProcessState.WAITINGTOLOCKBOX else "transparent")
        self.close_box_label.configure(text_color=("gray10", "gray90") if name == ProcessState.WAITINGTOLOCKBOX else ("gray10", "gray40"))
        # show selected frame
        if name == ProcessState.STARTDELIVERYSEQUENCE:
            self.forget_all_frames()
            self.start_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.WAITINGTOUNLOCKBOX or name == ProcessState.KEYINGINORDERS:
            self.forget_all_frames()
            self.enter_passcode_frame_content1_label.configure(text="Enter Passcode" if curr_passcode_valid else "Passcode Invalid. Please try again.")
            self.enter_passcode_frame_content3_label.configure(text=user_input)
            self.enter_passcode_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.WAITINGFORUNLOCKBOXPAYLOAD or name == ProcessState.WAITINGFORADDITIONALORDERSPAYLOAD:
            self.forget_all_frames()
            self.wait_for_validation_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.WAITINGFORPICTUREPAYLOAD:
            self.forget_all_frames()
            self.please_wait_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.TAKINGORDERPICTURE:
            self.forget_all_frames()
            self.photo_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.CONFIRMINGMOREORDERS:
            self.forget_all_frames()
            self.check_more_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == ProcessState.WAITINGTOLOCKBOX:
            self.forget_all_frames()
            self.close_box_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)

########################################## HARDWARE ##########################################

class LockState(Enum):
    LOCKED = 1
    UNLOCKED = 2

class ProcessState(Enum):
    STARTDELIVERYSEQUENCE = 0,
    WAITINGTOUNLOCKBOX = 1,
    WAITINGFORUNLOCKBOXPAYLOAD = 2
    TAKINGORDERPICTURE = 3,
    WAITINGFORPICTUREPAYLOAD = 4,
    KEYINGINORDERS = 5,
    WAITINGFORADDITIONALORDERSPAYLOAD = 6,
    CONFIRMINGMOREORDERS = 7,
    CONFIRMLOCKSEQUENCE = 8,
    WAITINGTOLOCKBOX = 9

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
process_state = ProcessState.STARTDELIVERYSEQUENCE
limit_switch_state = LimitSwitchState.CLOSED
keypadPressed = -1
switch_state = 1
prev_switch_state = -1
device_id = "simple_id"
most_recent_keyed_in_passcode = ""
mqtt_connection = None
prev_process_state = ProcessState.STARTDELIVERYSEQUENCE
curr_process_state = ProcessState.STARTDELIVERYSEQUENCE
prev_user_input = user_input
curr_user_input = user_input
prev_passcode_valid = True
curr_passcode_valid = True

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
    lock()
    return

# Reads the columns and appends the value, that corresponds to the button, to a variable
def read_line(line, characters):
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
## START DELIVERY SEQUENCE ##
def start_delivery_sequence():
    global process_state
    process_state = ProcessState.WAITINGTOUNLOCKBOX

def invalid_asterisk_at_start_state():
    global process_state
    print("Please press # to start delivery sequence")
    process_state = ProcessState.STARTDELIVERYSEQUENCE

## WAITINGTOUNLCOCKBOX ##
# Backspace func 
def backspace():
    global user_input
    if len(user_input)!=0:
        user_input = user_input[:-1]
    return

# Confirm user input func
def confirm_passcode():
    global most_recent_keyed_in_passcode
    global user_input
    global process_state
    global most_recent_keyed_in_passcode
    global mqtt_connection
    global curr_passcode_valid
    if len(user_input) == 6:
        validate_payload = format_validate_payload(device_id, user_input)
        publish_to_validate_topic(mqtt_connection, validate_payload)
        process_state = ProcessState.WAITINGFORUNLOCKBOXPAYLOAD
    else:
        curr_passcode_valid = False
    return

## WAITINGFORUNLOCKBOXPAYLOAD ##
def check_unlock_box_payload():
    global process_state
    global mqtt_connection
    global device_id
    global user_input
    global most_recent_keyed_in_passcode
    global lock_state
    global limit_switch_state
    global curr_passcode_valid
    received_payload = wait_for_received_payload()
    if received_payload:
        if validate_passcode_payload(decode_payload(received_payload)):
            curr_passcode_valid = True
            print("Correct passcode")
            unlock()
            most_recent_keyed_in_passcode = user_input
            process_state = ProcessState.TAKINGORDERPICTURE
        else:
            curr_passcode_valid = False
            lock()
            print("Incorrect passcode, please key in again")
            process_state = ProcessState.WAITINGTOUNLOCKBOX
        invalidate_payload()
    user_input = ""
    return

## TAKINGORDERPICTURES ##
def taking_order_picture():
    global process_state
    global most_recent_keyed_in_passcode
    global mqtt_connection
    # AWS PUB take photo and receive confirmation from MQTT here
    take_photo_payload = format_take_photo_payload(device_id, most_recent_keyed_in_passcode)
    publish_to_take_photo_topic(mqtt_connection, take_photo_payload)
    process_state = ProcessState.WAITINGFORPICTUREPAYLOAD

def invalidate_asterisk_at_photo_state():
    global process_state
    print("Please press # to take picture")
    process_state = ProcessState.TAKINGORDERPICTURE

## WAITINGFORPICTUREPAYLOAD ##
def check_picture_payload():
    global process_state
    global mqtt_connection
    global device_id
    global user_input
    global most_recent_keyed_in_passcode
    global lock_state
    global limit_switch_state
    received_payload = wait_for_received_payload()
    if received_payload:
        if validate_take_photo_payload(decode_payload(received_payload)):
            print("Picture taken")
            process_state = ProcessState.CONFIRMINGMOREORDERS
        else:
            print("Picture not taken")
            print("Please press # to take picture")
        invalidate_payload()
    user_input = ""
    return

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
    global most_recent_keyed_in_passcode
    global mqtt_connection
    global curr_passcode_valid
    # AWS PUB passcode and receive confirmation from MQTT here
    if len(user_input) == 6:
        validate_payload = format_validate_payload(device_id, user_input)
        publish_to_validate_topic(mqtt_connection, validate_payload)
        process_state = ProcessState.WAITINGFORADDITIONALORDERSPAYLOAD
    else:
        curr_passcode_valid = False
    return

## WAITINGFORADDITIONALORDERSPAYLOAD ##
def check_additional_orders_payload():
    global process_state
    global mqtt_connection
    global device_id
    global user_input
    global most_recent_keyed_in_passcode
    global lock_state
    global limit_switch_state
    global curr_passcode_valid
    received_payload = wait_for_received_payload()
    if received_payload:
        if validate_passcode_payload(decode_payload(received_payload)):
            curr_passcode_valid = True
            print("Correct passcode")
            most_recent_keyed_in_passcode = user_input
            process_state = ProcessState.TAKINGORDERPICTURE
        else:
            curr_passcode_valid = False
            print("Incorrect passcode, please key in again")
            process_state = ProcessState.KEYINGINORDERS
        invalidate_payload()
    user_input = ""
    return

def start_locking_sequence():
    global process_state
    global user_input
    if len(user_input) == 0:
        process_state = ProcessState.WAITINGTOLOCKBOX
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
        process_state = ProcessState.STARTDELIVERYSEQUENCE
    else:
        print("Please close the door properly")
    return

def invalid_asterisk_at_locking_state():
    global process_state
    print("Please press # to lock the door")
    process_state = ProcessState.WAITINGTOLOCKBOX

########################################## GENERAL KEYPAD FUNCTIONS ##########################################
def check_special_keys(hash_func, asterisk_func):
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
    if not check_special_keys(hash_func, asterisk_func):
        read_line(L1, ["1","2","3"])
        read_line(L2, ["4","5","6"])
        read_line(L3, ["7","8","9"])
        read_line(L4, ["*","0","#"])


def state_machine(ctk):
    global lock_state
    global process_state
    global keypadPressed
    global curr_process_state
    global curr_user_input
    if keypadPressed != -1:
        setAllLines(GPIO.HIGH)
        if GPIO.input(keypadPressed) == 0:
            keypadPressed = -1
    else:
        if process_state == ProcessState.STARTDELIVERYSEQUENCE:
            print("Press # to start delivery sequence")
            keypad_input(hash_func=start_delivery_sequence, asterisk_func=invalid_asterisk_at_start_state)
        elif process_state == ProcessState.WAITINGTOUNLOCKBOX and lock_state == LockState.LOCKED:
            keypad_input(hash_func=confirm_passcode, asterisk_func=backspace)
        elif process_state == ProcessState.WAITINGFORUNLOCKBOXPAYLOAD:
            check_unlock_box_payload()
        elif process_state == ProcessState.TAKINGORDERPICTURE:
            keypad_input(hash_func=taking_order_picture, asterisk_func=invalidate_asterisk_at_photo_state)
        elif process_state == ProcessState.WAITINGFORPICTUREPAYLOAD:
            check_picture_payload()
        elif process_state == ProcessState.CONFIRMINGMOREORDERS:
            keypad_input(hash_func=confirm_more_orders, asterisk_func=confirm_no_more_orders)
        elif process_state == ProcessState.KEYINGINORDERS:
            keypad_input(hash_func=key_in_additional_orders, asterisk_func=start_locking_sequence)
        elif process_state == ProcessState.WAITINGFORADDITIONALORDERSPAYLOAD:
            check_additional_orders_payload()
        elif process_state == ProcessState.WAITINGTOLOCKBOX:
            app.after(1000,lock_box())
        curr_process_state = process_state
        curr_user_input = user_input
        

def check_change_of_state():
    global prev_process_state
    global curr_process_state
    if prev_process_state != curr_process_state:
        prev_process_state = curr_process_state
        return True
    return False

def check_change_of_input():
    global prev_user_input
    global curr_user_input
    if prev_user_input != curr_user_input:
        prev_user_input = curr_user_input
        return True
    return False
    
def check_change_of_passcode_valid():
    global prev_passcode_valid
    global curr_passcode_valid
    if prev_passcode_valid != curr_passcode_valid:
        prev_passcode_valid = curr_passcode_valid
        return True
    return False

########################################## DRIVER FUNCTION ##########################################
app = ctkApp()
mqtt_connection = aws_setup()
hardware_setup()

def my_main_loop():
    global switch_state
    global prev_switch_state
    global mqtt_connection
    global device_id
    global process_state
    global lock_state
    global user_input
    global limit_switch_state
    global app
    if mqtt_connection and device_id:
        switch_state = GPIO.input(LimitSwitchPin)
        if switch_state != prev_switch_state:
            if switch_state == 0:
                limit_switch_state = LimitSwitchState.CLOSED
            else:
                limit_switch_state = LimitSwitchState.OPEN
            prev_switch_state = switch_state
        state_machine(app)
        print("-------------------------------------------------")
        print("User input: " + user_input)
        print("Most recent user input: " + str(most_recent_keyed_in_passcode))
        print("Lock state: " + str(lock_state))
        print("Process state: " + str(process_state))
        print("Limit switch state: " + str(limit_switch_state))
        print("-------------------------------------------------")
    if check_change_of_state():
        print("Changing state to: " + str(curr_process_state))
        app.select_frame_by_name(curr_process_state)
    else:
        print("ELSE")
        if process_state == ProcessState.WAITINGTOUNLOCKBOX or process_state == ProcessState.KEYINGINORDERS:
            print("keying states")
            print(prev_user_input)
            print(curr_user_input)
            if check_change_of_input():
                print("Changing input to: " + str(curr_user_input))
                app.select_frame_by_name(curr_process_state, curr_user_input)
            if check_change_of_passcode_valid():
                app.select_frame_by_name(curr_process_state, curr_user_input)
    app.after(100, my_main_loop)

app.after(100, my_main_loop)
app.mainloop()


