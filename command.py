import sys
import os
import time

import pinger
import sun

sys.path.insert(0, "/home/uad/Programming/database-gspreadsheet/")
import db_ev


def turn_on():
	os.system("k1")
	db_ev.write("k",True)

def turn_off():
	os.system("k0")
	db_ev.write("k",False)


ip = "192.168.1.27"
your_city = "Ankara"



if(pinger.is_online(ip)):
	if(not(sun.is_shining(your_city))):
		while(db_ev.read("is_at_home") == "0"):
			print("welcome home")
			turn_on()
			db_ev.write("is_at_home",True)
	else:
		print("shining\nno need to turn on")
		#turn_off()
else:
	print("not at home")
	while(db_ev.read("is_at_home") == "1"):	
		print("goodbye")	
		turn_off()
		db_ev.write("is_at_home",False)

