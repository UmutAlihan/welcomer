#!/usr/bin/python3

import subprocess
import datetime

#ip_alive = "192.168.1.126"
#ip_dead = "192.168.1.203"


def is_online(ip):
#checking if related ip is connected to local network
	ping = subprocess.run(["/bin/ping", "-c 3", ip], stdout=subprocess.PIPE)
	ping_result = ping.stdout.decode("utf-8").split("\n")
	return not(any("100% packet loss" in result for result in ping_result))

now = datetime.datetime.now().strftime("%H:%M-%d.%m.%y")
filename = "/tmp/ping.log"
ip="192.168.1.203"
log = open(filename, "a+")
print(" 0\n")
print(now,is_online(ip), file=log)
print("1\n")
log.close()
print("2\n")

