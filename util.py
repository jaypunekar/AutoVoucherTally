import customtkinter

class UpdateFrame(customtkinter.CTkFrame):
    def __init__(self, resort_name, amount, reason, master, **kwargs):
        super().__init__(master, **kwargs)
        self.resort_name = resort_name
        self.amount = amount
        self.reason = reason

        self.label_heading = customtkinter.CTkLabel(self, text="Entered Details", font=('Monospace', 30), width=10, justify='center')
        self.label_heading.place(relx=0.5, rely=0.1, anchor='n')

        self.label_name = customtkinter.CTkLabel(self, text="Resort Name:")
        self.label_name.place(relx=0.15, rely=.2, anchor='nw')
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text=self.resort_name, width=200)
        self.entry_name.place(relx=.15, rely=.25, anchor='nw')

        self.label_amount = customtkinter.CTkLabel(self, text="Amount (Rs.)")
        self.label_amount.place(relx=0.15, rely=.3, anchor='nw')
        self.entry_amount = customtkinter.CTkEntry(self, placeholder_text=self.amount, width=140)
        self.entry_amount.place(relx=.15, rely=.35, anchor='nw')

        self.label_reason = customtkinter.CTkLabel(self, text="Reason:")
        self.label_reason.place(relx=0.15, rely=.4, anchor='nw')
        self.textbox_reason = customtkinter.CTkTextbox(master=self, width=400, corner_radius=8)
        self.textbox_reason.insert('end', self.reason)
        self.textbox_reason.place(relx=.15, rely=.45, anchor='nw')

        self.button_save = customtkinter.CTkButton(self, text="Save")
        self.button_save.place(relx=0.3, rely=0.90, anchor='s')

        self.button_update = customtkinter.CTkButton(self, text="Update",)
        self.button_update.place(relx=0.7, rely=0.90, anchor='s')
