#!/usr/bin/python3

import sys
import os
import time

import pinger
import sun
import db_ev


def turn_on():
	os.system("k1")
	db_ev.write("k",True)

def turn_off():
	os.system("k0")
	db_ev.write("k",False)


ip = "192.168.1.13"
your_city = "Ankara"

filename = "/tmp/welcomer.log"

while(1):
	log_w = open(filename, "a+")
	#time.sleep(1)
	if(pinger.is_online(ip)):
		if(not(sun.is_shining(your_city))):
			while(db_ev.read("is_at_home") == "0"):
				print("welcome home",file=log_w)
				turn_on()
				db_ev.write("is_at_home",True)
		else:
			print("shining\nno need to turn on",file=log_w)
			#turn_off()
	else:
		print("not at home",file=log_w)
		while(db_ev.read("is_at_home") == "1"):
			print("goodbye",file=log_w)
			turn_off()
			db_ev.write("is_at_home",False)
	log_w.close()
