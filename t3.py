''' ToDos
[ ] Add in storage
[ ] Move router to switch case format
[ ] Add check in router if command not in correct format
[ ] Move input array into single line
[ ] handle records over the next date
[ ] Add storage option (.json)
[ ] store active record as it's made
[ ] hook up fixtures
'''

import json
import datetime
import csv

def start_up():
	records = {}
	today = str(datetime.date.today())		
	if today not in records.keys():
		records[today] = []		
	record_manager(records)

def record_manager(records): 
	command = ''
	active_record = ''
	while command != 'done':
		if active_record == '':
			command = input(': ')
			active_record = make_record(command)

		else:
			command = input(': ')
			save_record(active_record, records)					
			active_record = make_record(command)			
		
	package_results(records)
		

def make_record(command):
	results_array = command.split(',')
	client = results_array[0]
	comment = ''
	if len(results_array) == 2:		
		comment = results_array[1].strip()				
	start_time = datetime.datetime.now()
	return [client, comment, start_time]

def save_record(record, records):
	start = record[2]
	end = datetime.datetime.now()	
	length = end - start
	minutes = round(length.seconds / 60)
	today = str(datetime.date.today())	
	records[today].append([record[0], record[1], minutes])

def package_results(records):
	today = str(datetime.date.today())	
	todays_records = records[today]
	record_grouping = {}
	for record in todays_records:
		client = record[0]
		length = record[2]
		comment_row = record[1] + ' (' + str(length) + ')'
		if client in record_grouping.keys():
			total_length = record_grouping[client][0]
			total_comments = record_grouping[client][1]			
			total_length = total_length + length
			total_comments = total_comments + ' ' + comment_row
			record_grouping[client] = [total_length, total_comments]
		else:
			record_grouping[client] = [length, comment_row]	

	time = str(datetime.datetime.now())
	filename = 'timesheets/timesheet_' + time + '.csv'
	with open(filename, 'w') as f:
		headers = 'total tracked time (in minutes),client,comments (invidual events time)\n'
		f.write(headers)
		for key in record_grouping.keys():
			f.write(str(record_grouping[key][0]) + ',' + key + "," + record_grouping[key][1] + '\n')
	print('Timesheet Saved at timesheets/' + filename)
start_up()
