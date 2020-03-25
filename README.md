# Tiny Time Tracker (t3)

Welcome! This is my attempt to make the lightest/fastest timetracker.

My goal is to make everything about this as simple and compact as possible (including this README!)

## How it works
- Time is inputted via Terminal and stored in a Google Sheet
- Once t3 is started, give it a client name, then optionally a comma and a comment (ex. `Big Brand LLC, new purchase order`) A timer has started. 
- If a new client is entered the previous timer we stop, a record will be made, and a new timer will start. If you need to take a break just type `break`
- When you are done for the day type `output` it will output a csv in this format:

| total tracked time (in minutes) | client | comments (invidual events time) |
| ------------- |:-------------:| -----:|
| 78 | Big Brand LLC | - new purchase order (23) - marketing plan (10) - call with client (23)

- 100% Terminal Based
- Written in Python3
 
### SetUpe
1. Download the Repo locally
2. Set Up Credentials 
	1. Head over to the [Google API Console](https://console.developers.google.com/).
	2. Select '+ ENABLE APIS AND SERVICES'
	3. Search for 'Google Sheets API', enable it.
	4. Go back to Dashboard and select 'Credentials' (sidebar), click 'Create Credentials' -> 'Service Account'
	5. Give the app a name like 'Time Tracker', Skip 'Grant this service account access to project', Click Create Key
	6. Create JSON Key, you will be given a secret file, also, note your Service Accounts email (ex. t3@xxx-000.iam.gserviceaccount.com)
3. Create Google Sheet
4. Grant Google Sheet Access to your service account email
4. Drag this key into the t3 folder called `/creds`. This folder is set up to not be logged to version control. 
5. Rename the file creds.json
6. `pip install pygsheets && pip install pandas`
7. In the t3.py file add in the url Google Sheet.
5. `python3 t3.py`

### Commands
- `<client name>, <comment>` - start new time record
- `stop` - continue to run but do not track time
- `output` - generate timesheet for the day
- `done` - turn off t3


