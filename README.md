# AutoVoucherTally (TallyMain)

The AutoVoucherTally (also known as TallyMain) is a comprehensive solution designed to streamline and automate the voucher creation, approval, and payment process for businesses. It comprises three interconnected applications: TallyClient, TallyMain, and TallyAccounts, each serving a specific role in the end-to-end workflow. Ideally, three different computers are required with their respective app installed. Let's take a brief look at the overall functionality of the entire software:

AutoVoucherTally:

1. TallyClient:
- TallyClient is the front-end application that allows users to create a voucher, which includes Client name, Amount, Department and Reason for payment. The app provides an intuitive interface where users can input all the necessary details of the vouchers. Once the voucher data is filled in, TallyClient securely stores it in MongoDB, a NoSQL database, ensuring centralized and easily accessible storage for all vouchers.

2. TallyMain:
- TallyMain acts as the central processing hub of the software. It retrieves the voucher data stored in MongoDB and performs an approval process by selecting the payment method from the company's side. This approval process ensures that only valid and correctly filled vouchers proceed further for processing. TallyMain then add the entries to Tally using Tally's Server using XML. Users need not import the XML file manually to Tally. 

3. TallyAccounts:
- TallyAccounts is responsible for processing the vouchers that have been approved by TallyMain. It retrieves the approved voucher data from MongoDB and initiates the payment process based on the payment details provided in those vouchers. This may include online fund transfers, generating checks, or recording cash payments in Tally ERP 9. TallyAccounts updates the voucher status in MongoDB after successful payment execution, marking it as "paid".

Points to remember before use (These points a elaborated more in Setup sections):

- Make sure you are connected to the Internet.

- Tally EPR 9 should be running in the background.

-  MongoDB Atlas servers should be up (This is not a concern but just in case).



Overall, the integrated functionality of TallyClient, TallyMain, and TallyAccounts in your Voucher Automation Software streamlines the voucher creation, approval, and payment process, reducing manual efforts, eliminating errors, and ensuring accurate accounting in Tally ERP 9.



## AutoVoucherTally Setup
Coming shortly
## Tally Setup
Coming shortly
## Installation
### Software Requirement.

1. [TallyClient](https://github.com/jaypunekar/TallyClient)
2. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)
3. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)


Clone the project:

```bash
git clone https://github.com/jaypunekar/AutoVoucherTally.git
```
Go to the project directory
```bash
cd AutoVoucherTally
```

Create conda virtual enviornment (This step in not necessory):
```bash
conda create -p venv python==3.8 -y
```
```bash
conda activate venv/
```

OR 
```bash
conda activate venv
```
Install dependencies:
```bash
pip install -r requirements.txt
```

To run the program using Terminal:
```bash
python main.py
```
OR
```bash
python3 main.py
```


## Packaging the Application

In the Terminal (In AutoVoucherTally dir) run:
```bash
pyinstaller --onefile main.py  
```

Then run:

```bash
pyinstaller --name TallyMain --onefile --windowed --main.py
```

If you want to add an icon run (icon.ico should be in AutoVoucherTally dir):
```bash
pyinstaller --name TallyMain --onefile --windowed --icon=icon.ico --main.py
```
#### You will see a "dist" folder in AutoVoucherTally directory. Inside the "dist" folder you will get the executable file.

## Screenshots

[![img.png](https://i.postimg.cc/yY2bcnyN/img.png)](https://postimg.cc/dLm6K2XM)

[![img2.png](https://i.postimg.cc/BZVYfNyC/img2.png)](https://postimg.cc/ThnqrjTy)
