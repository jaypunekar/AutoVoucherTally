import customtkinter
from CTkMessagebox import CTkMessagebox
from pymongo.mongo_client import MongoClient
from tkinter import ttk
from datetime import datetime
import pandas as pd
from PIL import Image
import requests
import xml.etree.ElementTree as Et

# Tally URL
tally_url = "https://localhost:9000"

# MongoDB Atlas URL
mongo_url = "mongodb+srv://mongodb:mongodb@tally.i6wfrlt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_url)

# Database Name and Collection Name
db = client['Punekar']
collec = db['Tally']


class UpdateFrame(customtkinter.CTkFrame):
    def __init__(self, client_name, amount, reason, master, **kwargs):
        super().__init__(master, **kwargs)
        self.client_name = client_name
        self.amount = amount
        self.reason = reason

        self.label_heading = customtkinter.CTkLabel(self, text="Entered Details", font=('Monospace', 30), width=10, justify='center')
        self.label_heading.place(relx=0.5, rely=0.1, anchor='n')

        self.label_name = customtkinter.CTkLabel(self, text="Resort Name:")
        self.label_name.place(relx=0.15, rely=.2, anchor='nw')
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text=self.client_name, width=200)
        self.entry_name.place(relx=.15, rely=.25, anchor='nw')

        # Dropdown menu for Types of Payment
        self.payment_type = customtkinter.CTkLabel(self, text="Payment Type")
        self.payment_type.place(relx=0.15, rely=.2, anchor='nw')
        self.optionmenu = customtkinter.CTkOptionMenu(self ,values=['', 'Cash', 'Bank 1', 'Bank 2', 'Bank 3', 'Bank 4'])

        # This code finds the currently selected
        self.currently_selected = collec.find_one({"Client Name": str(client_name), "Amount": str(amount), "Reason": str(reason)})
        if self.currently_selected['Payment_from']:   #if there is a payment type selected that preset the menu to that type or else show blank
            self.optionmenu.set(self.currently_selected['Payment_from'])
        else:
            self.optionmenu.set('')
        self.optionmenu.place(relx=.55, rely=.25, anchor='nw')

        self.label_amount = customtkinter.CTkLabel(self, text="Amount (Rs.)")
        self.label_amount.place(relx=0.15, rely=.3, anchor='nw')
        self.entry_amount = customtkinter.CTkEntry(self, placeholder_text=self.amount, width=140)
        self.entry_amount.place(relx=.15, rely=.35, anchor='nw')

        self.label_reason = customtkinter.CTkLabel(self, text="Reason:")
        self.label_reason.place(relx=0.15, rely=.4, anchor='nw')
        self.textbox_reason = customtkinter.CTkTextbox(master=self, width=400, corner_radius=8)
        self.textbox_reason.insert('end', self.reason)
        self.textbox_reason.place(relx=.15, rely=.45, anchor='nw')

        self.button_save = customtkinter.CTkButton(self, text="Delete", command=lambda:self.delete_the_voucher(self.optionmenu.get(), self.client_name, self.amount, self.reason))
        self.button_save.place(relx=0.3, rely=0.90, anchor='s')

        self.button_update = customtkinter.CTkButton(self, text="Approve",command=lambda:self.update_bank_details(self.optionmenu.get(), self.client_name, self.amount, self.reason))
        self.button_update.place(relx=0.7, rely=0.90, anchor='s')

    def delete_the_voucher(self, payment_type, client_name, amount, reason):
        try:
            selected_voucher = collec.find_one({"Client Name": str(client_name), "Amount": str(amount), "Reason": str(reason)})
            collec.delete_one({"Client Name": str(client_name), "Amount": str(amount), "Reason": str(reason)})
            CTkMessagebox(title='Updated', message="The voucher is Succussfully Deleated! (Restart the Program to See the Changes)")
        except Exception:
            CTkMessagebox(title='Error', message="There was an error while deleating the voucher")


    def update_bank_details(self, payment_type, client_name, amount, reason):
        try:
            # Convert all the parameter to string so that 'find_one' function will understand
            # print(collec.find_one({"Client Name": str(client_name), "Amount": str(amount), "Reason": str(reason)}))
            if payment_type is not '':
                collec.update_one({"Client Name": str(client_name), "Amount": str(amount), "Reason": str(reason)}, {"$set": {"Payment_from": str(payment_type), "Approved": 1}})
                CTkMessagebox(title='Updated', message="Payment Type has been Succussfully Updated and the Voucher has been Approved (Restart the program to see the changes)")
            else:
                CTkMessagebox(title='Error', message="Please select a proper bank")


        except Exception:
            CTkMessagebox(title='Error', message="There was an Error while updating")
        

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.update_button = customtkinter.CTkButton(self, text="View", command=self.view_selected)
        self.update_button.pack(pady=10)
        self.update_button = customtkinter.CTkButton(self, text="Add Resort")
        self.update_button.pack(pady=10)
        self.update_button = customtkinter.CTkButton(self, text="Check Resort")
        self.update_button.pack(pady=10)
        self.update_button = customtkinter.CTkButton(self, text="Add to Tally", fg_color='red', command=self.integrate_in_tally)
        self.update_button.pack(pady=100)

        self.update_window = None

    # This function will integrate all the "Approved" & "Paid" Voucher to Tally
    def integrate_in_tally(self):
        self.client_name = "Name"
        self.paymant_from = "Bank Name"
        self.date_time = "Date & Time"
        
        #Tally server Runs on localhost:9000 by default
        self.url = "http://localhost:9000/"

        self.xmlBody = f"""<ENVELOPE>
            <HEADER>
                <VERSION>1</VERSION>
                <TALLYREQUEST>Import</TALLYREQUEST>
                <TYPE>Data</TYPE>
                <ID>Vouchers</ID>
            </HEADER>
            <BODY>
                <DESC>
                    <STATICVARIABLES>
                        <IMPORTDUPS>@@DUPCOMBINE</IMPORTDUPS>
                        </STATICVARIABLES>
                </DESC>
                <DATA>
                    <TALLYMESSAGE>
                        <VOUCHER>
                            <DATE>20230701</DATE>
                            <NARRATION>Ch. No. Tested</NARRATION>
                            <VOUCHERTYPENAME>Payment</VOUCHERTYPENAME>
                            <VOUCHERNUMBER>1</VOUCHERNUMBER>
                            <ALLLEDGERENTRIES.LIST>
                                <LEDGERNAME>{self.client_name}</LEDGERNAME>
                                <ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>
                                <AMOUNT>10000.00</AMOUNT>
                            </ALLLEDGERENTRIES.LIST>
                            <ALLLEDGERENTRIES.LIST>
                                <LEDGERNAME>{self.payment_from}</LEDGERNAME>
                                <ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>
                                <AMOUNT>-10000.00</AMOUNT>
                            </ALLLEDGERENTRIES.LIST>
                        </VOUCHER>
                    </TALLYMESSAGE>
                </DATA>
            </BODY>
        </ENVELOPE>"""

        self.req = requests.post(url=self.url, data=self.xmlBody)

        self.res = self.req.text.strip()
        responseXML = Et.fromstring(self.res)

    def view_selected(self):
        try:
            x = trv.selection()
            self.update_window = customtkinter.CTkToplevel(self)
            self.update_window.geometry("637x637")
            self.update_window.focus()
            self.update_window.resizable(False, False)

            #Finding the data from MongoDB
            selected_item = collec.find_one({'Department': trv.item(x)["values"][0], 'Date_time': trv.item(x)["values"][1], 'Client Name': trv.item(x)["values"][2]})



            # Initializing class UpdateFrame
            # UpdateFrame class opens a toplevel frame with all the details in it
            self.my_frame = UpdateFrame(master=self.update_window, client_name=trv.item(x)["values"][2], amount=trv.item(x)["values"][4], reason=selected_item['Reason'], height=600, width=600)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        except Exception:
            print(Exception.__cause__)
            CTkMessagebox(title='Error', message="You haven't selected a row or there was an error in Database")


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.df = pd.DataFrame(columns=["Department", "Date_time", "Client Name", "Person Name", "Amount", "Payment_to", "Approved", "Paid"])
        self.order = True

        try:
            for one_collec in collec.find():
                self.df.loc[len(self.df.index)] = [one_collec["Department"], one_collec["Date_time"], one_collec["Client Name"], one_collec["Person Name"], one_collec["Amount"], one_collec["Payment_to"], one_collec["Approved"], one_collec["Paid"]]
        except Exception:
            CTkMessagebox(title="Error", message="There is a error in MyFrame")

        self.display_data(self.df)
        # self.my_tree.pack(pady=10)

        self.style = ttk.Style()
            
        self.style.theme_use("default")

        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        self.style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        self.style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        
        self.style.configure("Treeview", height=700)

        self.update_window = None

    # Function for sorting column 
    def sort_column(self, column):
        if self.order:
            self.order = False
        else:
            self.order = True
        
        self.df = self.df.sort_values(by=[column], ascending=self.order)
        self.display_data(self.df)

    def display_data(self, dataframe):
        l1 = list(self.df)
        r_set = self.df.to_numpy().tolist()
        global trv
        trv = ttk.Treeview(self, selectmode ='browse', show='headings', height=33, columns=l1)
        trv.grid(row=1,column=1,padx=30,pady=20)
        for col in l1:
            trv.column(col, width = 100, anchor ='c')
            trv.heading(col, text = col,command=lambda col=col :self.sort_column(col))

        for dt in r_set:  
            v = [r for r in dt] # creating a list from each row 
            trv.insert("", 'end' ,values=v) # adding row
        
