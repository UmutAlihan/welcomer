import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

#sheet = db_access()
#lamp_states = sheet.get_all_records()

#sheet.cell(2,1).value # cell(row, col)
#sheet.update_cell(2,2,"1")  # changing to new value "1"ets
#sheet.range("A1:B3")  #returns all data in range as list
#.input_value -> gives you the values of returned data

def db_access():
	os.chdir("/home/uad/Programming/welcomer/")
	scope = ["https://spreadsheets.google.com/feeds"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("./client_secret.json",scope)
	client = gspread.authorize(creds)
	return client.open("db-ev").sheet1


def read(item):
	db = db_access()
	if(item == "k"):
		state = db.cell(2,2).value
		return state 
	if(item == "s"): 
		state = db.cell(3,2).value 
		return state
	if(item == "is_at_home"):
		state = db.cell(4,2).value
		return state


def write(item, state):
	db = db_access()
	if(item == "k"):
		if(state == True):
			db.update_cell(2,2,"1")
		else:
			db.update_cell(2,2,"0")
	if(item == "s"):
		if(state == True):
			db.update_cell(3,2,"1")
		else:
			db.update_cell(3,2,"0")
	if(item == "is_at_home"):
		if(state == True):
			db.update_cell(4,2,"1")
		else:
			db.update_cell(4,2,"0")

