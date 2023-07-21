
# AutoVoucherTally (TallyMain)

The AutoVoucherTally (also known as TallyMain) is a comprehensive solution designed to streamline and automate the voucher creation, approval, and payment process for businesses. It comprises three interconnected applications: TallyClient, TallyMain, and TallyAccounts, each serving a specific role in the end-to-end workflow. Ideally, three different computers are required with their respective app installed.

## Contents

- [Overview](#overview)
- [MongoDB Atlas Setup](#mongodb-atlas-setup)
- [AutoVoucherTally Setup](#autovouchertally-setup)
- [Tally ERP 9 Setup](#tally-erp-9-setup)
- [Installation](#installation)
- [Packaging](#packaging-the-application)
- [Screenshots](#screenshots)

## Overview
Let's take a brief look at the overall functionality of the entire software:

AutoVoucherTally:

1. TallyClient:
- TallyClient is the front-end application that allows users to create a voucher, which includes Client name, Amount, Department and Reason for payment. The app provides an intuitive interface where users can input all the necessary details of the vouchers. Once the voucher data is filled in, TallyClient securely stores it in MongoDB, a NoSQL database, ensuring centralized and easily accessible storage for all vouchers.

2. TallyMain:
- TallyMain acts as the central processing hub of the software. It retrieves the voucher data stored in MongoDB and performs an approval process by selecting the payment method from the company's side. This approval process ensures that only valid and correctly filled vouchers proceed further for processing. TallyMain then add the entries to Tally using Tally's Server using XML. Users need not import the XML file manually to Tally. 

3. TallyAccounts:
- TallyAccounts is responsible for processing the vouchers that have been approved by TallyMain. It retrieves the approved voucher data from MongoDB and initiates the payment process based on the payment details provided in those vouchers. This may include online fund transfers, generating checks, or recording cash payments in Tally ERP 9. TallyAccounts updates the voucher status in MongoDB after successful payment execution, marking it as "paid".

Points to remember before use (These points a elaborated more in Setup sections):

- Make sure you are connected to the Internet

- Tally EPR 9 should be running in the background

-  MongoDB Atlas servers should be up (This is not a concern but just in case)



Overall, the integrated functionality of TallyClient, TallyMain, and TallyAccounts in your Voucher Automation Software streamlines the voucher creation, approval, and payment process, reducing manual efforts, eliminating errors, and ensuring accurate accounting in Tally ERP 9.


## MongoDB Atlas Setup

#### *Note: Follow this section if you are completely to MongoDB or Databases in general. I have given detailed instructions with screenshots.

This Application uses MongoDB Atlas. If you are new to MongoDB Atlas follow the steps given below:

Step 1: Make an account on [MongoDB Atlas](https://www.mongodb.com/atlas/database)

Step 2: After creating an account you will be redirected to a page where you have to select a server. I would recommed choosing free for starters.

[![mongo-1.png](https://i.postimg.cc/8sQJWYjd/mongo-1.png)](https://postimg.cc/Wq81cXmt)

Step 3: You will then be asked to choose a username and password as a Security Check. Remember them as you will need them later.

[![mongo-2.png](https://i.postimg.cc/7YkQqZL6/mongo-2.png)](https://postimg.cc/9zLBpVZ5)

Step 4: This part is important. You will now have to give you IP Address to MongoDB. Access to your database will only be authorized from this IP Address. This can be edited later.

[![mongo-3.png](https://i.postimg.cc/dVDRYbG3/mongo-3.png)](https://postimg.cc/fVnS7g2Q)


Step 5: Congratulation you Databases is up and working. Now click on "Connect" button and go to Drivers.

[![mongo-4.png](https://i.postimg.cc/1XkSzhfS/mongo-4.png)](https://postimg.cc/y3ytfGmp)

[![mongo-5.png](https://i.postimg.cc/jSdwfmcT/mongo-5.png)](https://postimg.cc/ykt84f2p)

Step 6: Select Python as driver. And you get the url that connects to you database.

[![mongo-6.png](https://i.postimg.cc/023RGJdN/mongo-6.png)](https://postimg.cc/4mzSsy0C)

[![mongo-7.png](https://i.postimg.cc/mZ56KWcX/mongo-7.png)](https://postimg.cc/Thn9WSJg)

Step 7: In the link replace <paassword> with the paassword you gave earlier. Your username will already be there, if not, then add it too. (Remove the angle brackets aswell in <password>).

[![mongo-8.png](https://i.postimg.cc/wvPZXCLG/mongo-8.png)](https://postimg.cc/mzYmR6dY)

Step 8: Go to Browse Collections and you will see it is emply. There you can create a Database and Collection(remember their names as we will require it later).

[![mongo-9.png](https://i.postimg.cc/3xb3fxML/mongo-9.png)](https://postimg.cc/hXTFfgtx)

Congratulation! You have you MongoDB url. Now follow the next section for further integrating it to AutoVoucherTally.

## AutoVoucherTally Setup

You can get all the files for the project by cloning the project repository.

```bash
  git clone https://github.com/jaypunekar/AutoVoucherTally.git
```
Go to the project directory
```bash
  cd AutoVoucherTally
```

You will get all the files in AutoVoucherTally directory.

Step 1: There are two files that contains the code we are concerned with. i.e. main.py and util.py. In both the files you will find a section right after imports where the code to connect to MongoDB database is there.

[![mongoinside.png](https://i.postimg.cc/G2yVQcrs/mongoinside.png)](https://postimg.cc/S2mgQbny)

Setep 2: Change the mongo_url to the url you got earlier while setting up MongoDB Atlas. And change the database name and collection name as well (You should have all of it if you have followed the MongoDB Atlas Setup section). Change the code in both (main.py & util.py) the files.

*NOTE:- Keep localhost as it is.
## Tally ERP 9 Setup

Setting up Tally ERP 9 is reletively simple. We just have to make Tally ERP 9 as a Server. By Default it acts as a Client.

To do so. Open Tally EPR 9 and press F12 it will take you to configure page. Then go to Advance configuration make Tally as a Server.

[![tally-1.png](https://i.postimg.cc/KjD11kqG/tally-1.png)](https://postimg.cc/BPtSy6fk)

[![tally-2.png](https://i.postimg.cc/fWfyjdCZ/tally-2.png)](https://postimg.cc/Dmm778RY)

[![Tally-3.png](https://i.postimg.cc/RVP02z2D/Tally-3.png)](https://postimg.cc/fJ9Z01zc)


There is also a helpful youtube video on the same by Software Codecs [Here](https://www.youtube.com/watch?v=x_PhPlVL2mY).



## Installation
### Software Requirement.

1. [TallyClient](https://github.com/jaypunekar/TallyClient)
2. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)
3. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)

You should have already run first two command if you followed [AutoVoucherTally Setup](#autovouchertally-setup)

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
conda create -p venv python==3.7 -y
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
#### Complete MongoDB Atlas and AutoVoucherTally Setup first else the following command won't work.

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
