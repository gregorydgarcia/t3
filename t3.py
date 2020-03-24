''' ToDos
[ ] Add in storage
[ ] Move router to switch case format
[ ] Add check in router if command not in correct format
[ ] Move input array into single line
[ ] handle records over the next date
[ ] Add storage option (.json)
[ ] store active record as it's made
'''

import json
import datetime

def start_up():
	records = {}
	today = str(datetime.date.today())		
	if today not in records.values():
		records[today] = []		
	record_manager(records)

def record_manager(records): 
	command = ''
	active_record = ''
	while command != 'stop':
		if active_record == '':
			command = input(': ')
			active_record = make_record(command)

		else:
			command = input(': ')
			save_record(active_record, records)					
			active_record = make_record(command)			
		
	print(records)
		

def make_record(command):
	results_array = command.split(',')
	client = results_array[0]
	comment = ''
	if len(results_array) == 2:		
		comment = results_array[1]				
	start_time = datetime.datetime.now()
	return [client, comment, start_time]

def save_record(record, records):
	start = record[2]
	end = datetime.datetime.now()	
	length = end - start
	minutes = length.seconds / 60
	today = str(datetime.date.today())	
	records[today].append([record[0], record[1], minutes])


start_up()
