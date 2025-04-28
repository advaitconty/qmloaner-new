# Quarter Master Loaner System
- New GUI-based edition GitHub: [QMLoanerGUI](https://github.com/contyadvait/QMLoanerGUI)
- A QM loaning system for the St. Pat's Guitar Ensemble.
- Created with [Advait Contractor (Coder)](mailto:advait@contractor.net) and [Ryan Lim (Designer)](mailto:ryanlim2009@gmail.com)
## My beliefs of creating for the better
- Code should be used to help communities out
- This was made as a demonstration on how we do that
## Why does this exist?
- Our school guitar co-curricular activity (CCA) loans out guitars to everyone within the CCA
- This app makes loaning guitars easier
- The current system invloves
    - Checking an excel spreadsheet
    - Going to an CCA Leader (known as a Quarter master)
    - Asking them for a loan form
- This system automates this through:
    - Going on here
    - Selecting an available guitar
    - Getting a PDF that you can sign and give on collection of the guitar (with handling directions as a bonus through Google Gemini!)

## Running this locally
**Apple Sillicon Macs:**
```bash
git clone https://github.com/advaitconty/qmloaner-new
cd qmloaner-new/
pip3 install $(grep -v 'reportlab' requirements.txt)
git clone https://github.com/Distrotech/reportlab.git
cd reportlab
pip3 install -r requirements.txt
python3 setup.py build_ext --inplace
pip install .
cd ..
rm -rf reportlab/
```

**Everything else:**
```bash
git clone https://github.com/advaitconty/qmloaner-new
cd qmloaner-new/
pip3 install -r requirements.txt
python3 main.py
```

## Screenshots
![Loan table](https://cloud-7r6fpad9m-hack-club-bot.vercel.app/0loan_table.png)

![Email and form auto-generated](https://cloud-gwda8ooks-hack-club-bot.vercel.app/0generated_email_and_form.png)

_Check [`Loan Form Sample.pdf`](https://github.com/contyadvait/QMLoaner/blob/master/Loan%20Form%20Sample.pdf) for an example of how the loan form looks like_
- Cleaning and storage instructions generated with Google Gemini

---
## Requirements before using for your own club
1. Start by running installing requirements in requirements.txt through `pip install -r requirements.txt`
2. Prepare these variables
    - `GEMINI_API_KEY`: Please create this variable that contains your Gemini API Key from the [Google AI Studio](https://ai.google.dev/aistudio)
    - `ATTENDANCE_EMAILS`: A list of emails that when people use the app to inform others, an email will be sent to these people 
    -  `LOAN_EMAILS`: A list of people that will be informed when a guitar is loaned. Can be left blank
    - `NAMES`: A list of everyone's names in the CCA in FULL CAPS.
    - `EMAIL_ID` and `EMAIL_PASSWORD`: Your club's email ID and Password
        - `SMTP_SERVER` and `SMTP_PORT`: Your club's email's SMTP Server and SMTP Port number. You can easily find this thru searching it up
    - You're almost done at this point, now set-up the MongoDB server

### MongoDB Server set-up
Start by setting up `mongo_host_connection(userid, password, default=True)`: This is for accessing your MongoDB server. Inside it, 2 lines should be there, one that takes the `userID` and `password`, and one with a default userID and password in your MongoDB database.
For example:
```python
def mongo_host_connection(username, password, default=False):
    if default == True:
        return (f"mongodb+srv://defaultUser:somePass@mymongoserver.com")
    else:
        return (f"mongodb+srv://{username}:{password}@mymongoserver.com")
```

Once done, you can use the guitar data as a sample on how it should look. At the very least, it should have a `RENTED` String, which is either T or F. It should also have a `S/N` integer, which is required for it to work. Finally, a `Brand` field for Gemini to generate the correct instructions

To set up the database, a guitar data extractor has already been created. Just replace the `inventory.csv` file with another one and change the parameters accordingly inside the file `mongo_add.py`

Once you are done with all of this, run `secret_creator.py` and you are ready to use it for your school! You will have to change `image.jpg` to your school logo.

### Admin functions
For admin functions, create users within the MongoDB console that are admins for these functions. 
