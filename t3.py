GOOGLE_SHEET_URL = 'https://docs.google.com/spreadsheets/d/1LKX_c0fnDTJo9VFYFXkxRHa_W52uarDaUQhjcHJBO7g'

import json
import datetime
import csv
import pygsheets

gc = pygsheets.authorize(service_file='creds/creds.json')
sh = gc.open_by_url(GOOGLE_SHEET_URL)
summary_record = sh[0]
full_records = sh[1]

full_records.update_values('A1', [['hello', 'hi', 'yay']])




def start_up():	
	with open('records.json', 'r') as json_file:
		data = json.load(json_file)
		data["today"] = str(datetime.date.today())	
		if data["today"] not in data['records'].keys():
			data['records'][data["today"]] = []
		
	with open('records.json', 'w') as json_file:		
		json.dump(data, json_file)


	input_manager(data)	




def input_manager(data):
	command = input(': ') 
	while command != 'done':
		if command == 'stop':
			save_record(data)
			print('time is not being tracked')	
		elif command == 'output':
			save_record(data)
			package_results()
			print('time is not being tracked')
			input_manager(data)
		else:
			save_record(data)
			start_record(command, data)
		command = input(': ') 

	save_record(data)
	print('closing t3')
	return 

def save_record(data):
	r = data['active_record']
	
	if len(r) != 0: 
		start = datetime.datetime.strptime(r[2], "%Y-%m-%d %H:%M:%S.%f")
		end = datetime.datetime.now()	
		minutes = round((end - start).seconds / 60)		

		data['records'][data['today']].append([r[0], r[1], minutes])
		data['active_record'] = []
	
		with open('records.json', 'w') as json_file:		
			json.dump(data, json_file)

def start_record(command, data): 
	command_arr = command.split(',')		
	client = command_arr[0]
	comment = ''
	if len(command_arr) == 2:		
		comment = command_arr[1]		
	start_time = str(datetime.datetime.now())

	data['active_record'] = [client, comment, start_time]

	with open('records.json', 'w') as json_file:		
			json.dump(data, json_file)

def package_results():
	with open('records.json', 'r') as json_file:
		data = json.load(json_file)
		today = data['today']
		todays_records = data['records'][today]
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
		print('timesheet saved at timesheets/' + filename)

start_up()
