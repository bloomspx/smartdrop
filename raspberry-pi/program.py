from enum import Enum
import time
import customtkinter
import os
from PIL import Image

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
def unlock():
    global lock_state
    lock_state = LockState.UNLOCKED

def lock():
    global lock_state
    lock_state = LockState.LOCKED

class ctkApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set GUI title
        self.title("Smart Delivery System")

        # Get screen width and height
        width= self.winfo_screenwidth() 
        height= self.winfo_screenheight()
        # Set tkinter window size to full screen
        self.geometry("%dx%d" % (width, height))

        self.lock_state = LockState.LOCKED
        self.process_state = ProcessState.START_DELIVERY_SEQUENCE
        self.passcode = ["4789", "1234", "2345"]
        self.limit_switch_state = LimitSwitchState.CLOSED

        # Load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "delivery-man.png")), size=(50, 50))
        self.package_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "package.png")), size=(75, 75))

        # Set main grid layout 1x2
        # 1st column is for navigation frame
        # 2nd column is for content frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create initial navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        # Create title label
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Smart Delivery Box", height=60, text_color=("turquoise4", "turquoise4"), padx=20,
                                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Create label for start delivery step
        self.start_delivery_label = customtkinter.CTkLabel(self.navigation_frame,height=(height-80)/6, text="Step 1: Start Delivery", corner_radius=8,
                                                   fg_color=("gray75", "gray25"), 
                                                    compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 20)
        self.start_delivery_label.grid(row=1, column=0, sticky="ew", padx=20)
        # Create label for enter passcode step
        self.enter_passcode_label = customtkinter.CTkLabel(self.navigation_frame,height=(height-60)/6, text="Step 2: Enter Passcode", corner_radius=8,
                                                   fg_color=("gray75", "gray25"), 
                                                    compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 20)
        self.enter_passcode_label.grid(row=2, column=0, sticky="ew", padx=20)
        # Create label for photo step
        self.photo_label = customtkinter.CTkLabel(self.navigation_frame,  height=(height-60)/6, text="Step 3: Place Package in Box", corner_radius=8,
                                                   fg_color=("gray75", "gray25"), 
                                                    compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 20)
        self.photo_label.grid(row=3, column=0, sticky="ew", padx=20)
        # Create label for checking more delivery step
        self.check_more_delivery_label = customtkinter.CTkLabel(self.navigation_frame,height=(height-60)/6, text="Step 4: Make Another Delivery / \nComplete Delivery", corner_radius=8,
                                                   fg_color=("gray75", "gray25"),
                                                    compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 20)
        self.check_more_delivery_label.grid(row=4, column=0, sticky="ew", padx=20)
        # Create label for close box step
        self.close_box_label = customtkinter.CTkLabel(self.navigation_frame, height=(height-60)/6, text="Step 5: Close Box", corner_radius=8,
                                                   fg_color=("gray75", "gray25"), 
                                                    compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), padx = 40)
        self.close_box_label.grid(row=5, column=0, sticky="ew", padx=20)

        self.textbox = customtkinter.CTkTextbox(self, width=0, height=0)
        self.textbox.bind("<KeyPress>", self.runEvent)
        self.textbox.grid(row=6, column=0, sticky="nsew")
        self.textbox.focus()

        # create initial start delivery frame
        self.start_delivery_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.start_delivery_frame_content1_label = customtkinter.CTkLabel(self.start_delivery_frame, text="Making a Delivery?",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.start_delivery_frame_content2_label = customtkinter.CTkLabel(self.start_delivery_frame, text="Press '#' to start delivery",
                                            text_color=("gray10", "gray99"),
                                            font=customtkinter.CTkFont(size=40, weight="bold", underline=True), padx = 20)
        self.start_delivery_frame_content1_label.place(relx=0.5, rely=0.45, anchor="center")       
        self.start_delivery_frame_content2_label.place(relx=0.5, rely=0.55, anchor="center")      
        self.start_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)       

        # create enter passcode frame
        self.enter_passcode_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.enter_passcode_frame_content_label = customtkinter.CTkLabel(self.enter_passcode_frame, text="Enter Passcode",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.enter_passcode_frame_content_label.place(relx=0.5, rely=0.45, anchor="center")  
        self.passcode_textbox = customtkinter.CTkTextbox(self.enter_passcode_frame, width=100, height=0)
        self.passcode_textbox.bind("<KeyPress>", self.runEvent)
        self.passcode_textbox.place(relx=0.5, rely=0.55, anchor="center")
        self.enter_passcode_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)         
        # create photo frame
        self.photo_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.photo_frame_frame_content1_label = customtkinter.CTkLabel(self.photo_frame, text="Place package in the box",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.photo_frame_content2_label = customtkinter.CTkLabel(self.photo_frame, text="Press '#' once item is placed",
                                            text_color=("gray10", "gray99"),
                                            font=customtkinter.CTkFont(size=40, weight="bold", underline=True), padx = 20)
        self.photo_frame_frame_content1_label.place(relx=0.5, rely=0.45, anchor="center")       
        self.photo_frame_content2_label.place(relx=0.5, rely=0.55, anchor="center")   
        self.photo_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create check more delivery frame
        self.check_more_delivery_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.check_more_delivery_content1_label = customtkinter.CTkLabel(self.check_more_delivery_frame, text="Do you have more deliveries?",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.check_more_delivery_content2_label = customtkinter.CTkLabel(self.check_more_delivery_frame, text="Press '#' for more deliveries \nor '*' to complete delivery",
                                            text_color=("gray10", "gray99"),
                                            font=customtkinter.CTkFont(size=40, weight="bold", underline=True), padx = 20)
        self.check_more_delivery_content1_label.place(relx=0.5, rely=0.3, anchor="center")       
        self.check_more_delivery_content2_label.place(relx=0.5, rely=0.55, anchor="center")   
        self.check_more_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        # create close box frame
        self.close_box_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.close_box_frame_content1_label = customtkinter.CTkLabel(self.close_box_frame, text="Close Box",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.close_box_frame_content1_label.place(relx=0.5, rely=0.5, anchor="center")  
        self.close_box_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)

        # select default frame
        self.select_frame_by_name("step_1")

    def forget_all_frames(self):
        self.start_delivery_frame.grid_forget()
        self.enter_passcode_frame.grid_forget()
        self.photo_frame.grid_forget()
        self.check_more_delivery_frame.grid_forget()
        self.close_box_frame.grid_forget()

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.start_delivery_label.configure(fg_color=("gray30", "gray30") if name == "step_1" else "transparent")
        self.start_delivery_label.configure(text_color=("gray10", "gray90")if name == "step_1" else ("gray10", "gray40"))
        self.enter_passcode_label.configure(fg_color=("gray30", "gray30")  if name == "step_2"  or name == "step_2_failed" else "transparent")
        self.enter_passcode_label.configure(text_color=("gray10", "gray90") if name == "step_2" or name == "step_2_failed" else ("gray10", "gray40"))
        self.photo_label.configure(fg_color=("turquoise4", "turquoise4")  if name == "step_3" else "transparent")
        self.photo_label.configure(text_color=("gray10", "gray90") if name == "step_3"else ("gray10", "gray40"))
        self.check_more_delivery_label.configure(fg_color=("turquoise4", "turquoise4")  if name == "step_4" else "transparent")
        self.check_more_delivery_label.configure(text_color=("gray10", "gray90") if name == "step_4" else ("gray10", "gray40"))
        self.close_box_label.configure(fg_color=("turquoise4", "turquoise4") if name == "step_5" else "transparent")
        self.close_box_label.configure(text_color=("gray10", "gray90") if name == "step_5" else ("gray10", "gray40"))

        # show selected frame
        if name == "step_1":
            self.forget_all_frames()
            self.start_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == "step_2":
            self.forget_all_frames()
            self.enter_passcode_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == "step_3":
            self.forget_all_frames()
            self.photo_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == "step_4":
            self.forget_all_frames()
            self.check_more_delivery_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
        if name == "step_5":
            self.forget_all_frames()
            self.close_box_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)

    def runEvent(self, event):
        print(event)
        print(self.process_state)
        print(self.textbox.get('1.0',"end"))
        if self.process_state == ProcessState.START_DELIVERY_SEQUENCE:
            if event.char == "#":
                self.textbox.delete('1.0', customtkinter.END)
                self.process_state = ProcessState.WAITING_TO_UNLOCK_BOX
                self.select_frame_by_name("step_2")
                self.textbox.delete('1.0', customtkinter.END)
                self.passcode_textbox.focus()
                self.mainloop()
            else:
                self.textbox.delete('1.0', customtkinter.END)
                self.mainloop()
                self.select_frame_by_name("step_1")
        elif self.process_state == ProcessState.WAITING_TO_UNLOCK_BOX:
            # Insert PUB passcode and receive confirmation from MQTT here
            if event.char == "#":
                if self.passcode_textbox.get('1.0',"end")[:-1] in self.passcode:
                    print("Correct passcode")
                    unlock()
                    self.enter_passcode_frame_content_label.configure(text="Enter passcode")
                    self.process_state = ProcessState.TAKING_ORDER_PICTURE
                    self.select_frame_by_name("step_3")
                    self.passcode_textbox.delete('1.0', customtkinter.END)
                    self.textbox.delete('1.0', customtkinter.END)
                    self.textbox.focus()
                    self.mainloop()
                else:
                    self.enter_passcode_frame_content_label.configure(text="Incorrect passcode, please key in again")
                    lock()
                    print("Incorrect passcode, please key in again")
                    self.passcode_textbox.delete('1.0', customtkinter.END)
                    self.mainloop()
        elif self.process_state == ProcessState.TAKING_ORDER_PICTURE:
            self.textbox.delete('1.0', customtkinter.END)
            print("Place the item in the box")
            if event.char == "#":
                # Wait for S3 response that picture has been uploaded
                print("Picture taken")
                self.process_state = ProcessState.CONFIRMING_MORE_ORDERS
                self.select_frame_by_name("step_4")
                self.textbox.delete('1.0', customtkinter.END)
                self.mainloop()
            else:
                self.textbox.delete('1.0', customtkinter.END)
                self.mainloop()
                print("Please press # to take picture")
        elif self.process_state == ProcessState.CONFIRMING_MORE_ORDERS:
            if event.char == "#":
                self.process_state = ProcessState.KEYING_IN_ORDERS
                self.select_frame_by_name("step_2")
                self.passcode_textbox.focus()
                self.textbox.delete('1.0', customtkinter.END)
                self.mainloop()
            elif event.char == "*":
                print("Thank you, please close the door")
                self.process_state = ProcessState.WAITING_TO_LOCK_BOX
                self.select_frame_by_name("step_5")
                self.textbox.delete('1.0', customtkinter.END)
                limit_switch_state = LimitSwitchState.CLOSED.value
                if limit_switch_state == LimitSwitchState.CLOSED.value:
                    lock()
                    self.process_state = ProcessState.START_DELIVERY_SEQUENCE
                    self.select_frame_by_name("step_1")
                else:
                    print("Please close the door properly")
                self.mainloop()
        elif self.process_state == ProcessState.KEYING_IN_ORDERS:
            print("Key in additional order passcodes. To lock the box, empty the input and press *")
            if event.char == "#":            
                if self.passcode_textbox.get('1.0',"end")[:-1] in self.passcode:
                    print("Correct passcode")
                    unlock()
                    self.process_state = ProcessState.TAKING_ORDER_PICTURE
                    self.select_frame_by_name("step_3")
                    self.passcode_textbox.delete('1.0', customtkinter.END)
                    self.textbox.delete('1.0', customtkinter.END)
                    self.textbox.focus()
                    self.mainloop()
                else:
                    self.select_frame_by_name("step_2_failed")
                    lock()
                    print("Incorrect passcode, please key in again")
                    self.passcode_textbox.delete('1.0', customtkinter.END)
                    self.mainloop()
            if event.char == "*":
                self.process_state = ProcessState.WAITING_TO_LOCK_BOX
        # elif self.process_state == ProcessState.WAITING_TO_LOCK_BOX:
        #     # Simulate the limit switch being in contact with the door 
        #     # while limit switch is not closed, keep checking
        #     limit_switch_state = LimitSwitchState.CLOSED.value
        #     if limit_switch_state == LimitSwitchState.CLOSED.value:
        #         lock()
        #         self.select_frame_by_name("step_1")
        #         self.process_state = ProcessState.START_DELIVERY_SEQUENCE
        #     else:
        #         print("Please close the door properly")



app = ctkApp()
app.mainloop()

