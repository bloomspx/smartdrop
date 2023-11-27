import customtkinter
import os
from PIL import Image
import time

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
        self.enter_passcode_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)       
        # create enter passcode failed frame
        self.enter_passcode_failed_frame = customtkinter.CTkFrame(self, corner_radius=12, fg_color=("turquoise4", "turquoise4"))
        self.enter_passcodee_failed_frame_content1_label = customtkinter.CTkLabel(self.enter_passcode_failed_frame, text="Enter Passcode",
                                    text_color=("gray10", "CadetBlue1"),
                                    font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.enter_passcodee_failed_frame_content2_label = customtkinter.CTkLabel(self.enter_passcode_failed_frame, text="Wrong Passcode! Try Again.",
                            text_color=("gray10", "CadetBlue1"),
                            font=customtkinter.CTkFont(size=40, weight="bold"), padx = 20)
        self.enter_passcodee_failed_frame_content1_label.place(relx=0.5, rely=0.45, anchor="center")     
        self.enter_passcodee_failed_frame_content2_label.place(relx=0.5, rely=0.55, anchor="center")  
        self.enter_passcode_failed_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)       
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
        self.enter_passcode_failed_frame.grid_forget()
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
        if name == "step_2_failed":
            self.forget_all_frames()
            self.enter_passcode_failed_frame.grid(row=0, column=1, sticky="nsew", padx=60, pady=100)
            self.after(5000, lambda: self.select_frame_by_name("step_2"))
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


# if __name__ == "__main__":
#     app = ctkApp()
#     app.mainloop()
