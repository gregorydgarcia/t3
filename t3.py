GOOGLE_SHEET_URL = 'https://docs.google.com/spreadsheets/d/1LKX_c0fnDTJo9VFYFXkxRHa_W52uarDaUQhjcHJBO7g'

import json
import datetime
import csv
import math
import pygsheets

gc = pygsheets.authorize(service_file='creds/creds.json')
sh = gc.open_by_url(GOOGLE_SHEET_URL)
summary_record = sh[0]
running_records = sh[1]

def input_manager():
	command = input(': ') 
	start_record(command)

	command = input(': ')
	while command != 'done':
		if command == 'pause':
			end_record()
			print('timer stopped. start new record to cont.')	
			command = input(': ')					
		else:
			end_record()
			start_record(command)
			command = input(': ') 

	end_record()
	summarize_day()
	print('closing t3')
	return 
	
def start_record(command): 
	client = command.split(',')[0].strip()
	prod = command.split(',')[1].strip()
	notes = command.split(',')[2].strip()
	start = str(datetime.datetime.now())
	new_record = [start,'','',client,prod,notes]
	running_records.insert_rows(1, number=1, values=new_record, inherit=False)


def end_record():
	row = running_records.get_row(2, returnas='matrix', include_tailing_empty=False)
	start = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
	end = datetime.datetime.now()	
	minutes = math.ceil((end - start).seconds / 60)	
	complete_record = [row[0], str(end), minutes, row[3], row[4], row[5]]
	running_records.update_row(2, complete_record, col_offset=0)


def summarize_day():
	print('summary is currently being reworked')
	# all_reccords = running_records.get_all_records(head=1, majdim='ROWS', numericise_data=True)

	# summary = {}
	# for record in all_reccords:
	# 	today = str(datetime.datetime.now()).split(' ')[0]
	# 	if record['Start Time'].split(' ')[0] ==  today:
	# 		formatter = [record['Length (Minutes)'],record['Description']]
	# 		if record['Client'] in summary.keys(): 
	# 			summary[record['Client']].append(formatter)
	# 		else:
	# 			summary[record['Client']] = [formatter]
	
	# for client in summary.keys():
	# 	time_total = 0
	# 	desc_total = ''
	# 	for record in summary[client]:
	# 		time_total = time_total + record[0]
	# 		desc_total = desc_total + '- ' +record[1] + ' (' + str(record[0]) + ')\n '
		
	# 	record = [today, client, time_total, desc_total.rstrip('\n ')]
	# 	summary_record.insert_rows(1, number=1, values=record, inherit=False)

input_manager()
