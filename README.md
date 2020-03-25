# Tiny Time Tracker (t3)

Welcome! This is my attempt to make the lightest/fastest timetracker.

My goal is to make everything about this as simple and compact as possible (including this README!)

## How it works
- Once t3 is started, give it a client name, then optionally a comma and a comment (ex. `Big Brand LLC, new purchase order`) A timer has started. 
- If a new client is entered the previous timer we stop, a record will be made, and a new timer will start. If you need to take a break just type `break`
- When you are done for the day type `output` it will output a csv in this format:

| total tracked time (in minutes) | client | comments (invidual events time) |
| ------------- |:-------------:| -----:|
| 78 | Big Brand LLC | - new purchase order (23) - marketing plan (10) - call with client (23)

- 100% Terminal Based
- Written in Python3
 
### SetUp
1. Download Repo
2. `python3 t3.py`

### Commands
- `<client name>, <comment>` - start new time record
- `pause` - continue to run but do not track time
- `output` - generate timesheet for the day
- `done` - turn off t3


