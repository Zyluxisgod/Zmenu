#!/usr/bin/python

'''
This is me just messing around,so
edit it if you want,as I do not care.
Have fun and enjoy!Thank you.
'''

import os #=====> For command line stuff
from colors import * #My list of colors
from termcolor import colored #More colors
import sys #Just cuz
from geoip import open_database #For geoip
import subprocess #To background stuff
import random #For random password
import string #Password stuff



while True:
	
	
#Main menu
	os.system("clear") #=====> Clear
	file = open("Banner/banner", "r") #=====> Open banner in read mode
	sys.stdout.write(BLUE)  #=====> Print banner in blue
	print file.read()
	print colored("   1:","white")+colored("IP and scanning","white")
	print colored("   2:", "white")+colored("Stress Testing", "white")
	print colored("   3:", "white")+colored("Passwords and Cracking")
	print colored("   00:", "white")+colored("Exit", "white")
	print("\n \n")
	menu_choice1 = input(colored("<Zyluxisgod>", "blue"))
	
	
#Main menu option 1
	if menu_choice1==1:
		os.system("clear")
		while True:
			file = open("Banner/networktools")
			sys.stdout.write(GREEN)
			print file.read()
			print colored("   1:", "white")+colored("Ping", "white")
			print colored("   2:", "white")+colored("Nmap", "white")
			print colored("   3:", "white")+colored("GeoIp", "white")
			print colored("   4:", "white")+colored("WhoIs", "white")
			print colored("   00:", "white")+colored("Main Menu", "white")
			print("\n \n")
			menu_choice = input(colored("<Zyluxisgod>", "blue")) #=====> Choice for menu1


#Possible options for Menu option 1
#Ping:
			if menu_choice==1:
				os.system("clear")
				while True:
					file = open("Banner/ping")
					sys.stdout.write(YELLOW)
					print file.read()
					x = raw_input(colored("Ip:", "white"))
					def ping(x):
						os.system("ping "+x)
					try:
						ping(x)
					except KeyboardInterrupt:
						break
						
#Nmap
			elif menu_choice==2:
				os.system("clear")
				while True:
					file = open("Banner/nmap")
					sys.stdout.write(YELLOW)
					print file.read()
					cmd = raw_input(colored("<nmap>", "blue"))
					os.system("nmap "+ cmd)
					
#GeoIP
			elif menu_choice==3:
				os.system("clear")
				file = open("Banner/geoip")
				sys.stdout.write(YELLOW)
				print file.read()
				ip = raw_input(colored("IP:", "white"))
				with open_database('/data/data/com.termux/files/usr/lib/python2.7/site-packages/_geoip_geolite2/GeoLite2-City.mmdb') as db:
				    match = db.lookup(ip)
				    print('IP info:', match)
				    db.close()
				
#Whois
			elif menu_choice==4:
				os.system("clear")
				while True:
					file = open("Banner/whois")
					sys.stdout.write(YELLOW)
					print file.read()
					ip = raw_input(colored("Domain:", "white"))
					os.system("whois "+ip)
#Back button
			elif menu_choice==00:
				break
#In case the user can't read
			else:
				print colored("Pick an option from the list please.", "red")
				
				
#Main menu option 2
	elif menu_choice1==2:
		os.system("clear")
		while True:
			file = open("Banner/stresstesting")
			sys.stdout.write(GREEN)
			print file.read()
			print colored("   1:", "white")+colored("DDOS IP", "white")
			print colored("   2:", "white")+colored("DOS Website", "white")
			print colored("   00:", "white")+colored("Main Menu", "white")
			print("\n \n")
			menu_choice = input(colored("<Zyluxisgod>", "blue"))
			
#DDOS IP menu option
			if menu_choice==1:
				os.system("clear")
				file = open("Banner/ddosip")
				sys.stdout.write(RED)
				print file.read()
				ip = raw_input(colored("IP:", "white"))
				subprocess.call(["core/ip",ip])
				
#DOS Website option
			elif menu_choice==2:
				os.system("clear")
				file = open("Banner/ddoswebsite")
				sys.stdout.write(RED)
				print file.read()
				website = raw_input(colored("Domain:", "white"))
				subprocess.call(["core/http",website])
				
#Back button
			elif menu_choice==00:
				break

#Just in case
			else:
				print("One of the options please")

				
#Main menu option 3
	elif menu_choice1==3:
		os.system("clear")
		file = open("Banner/passandcracking")
		sys.stdout.write(YELLOW)
		print file.read()
		print colored("   1:", "white")+colored("Generate Dictionary for bruteforce", "white")
		print colored("   2:", "white")+colored("Random Password", "white")
		print colored("   00:", "white")+colored("Main Menu", "white")
		print("\n \n")
		menu_choice = input(colored("<Zyluxisgod>", "blue"))
		
#Possible options for menu 3
		if menu_choice==1:
			while True:
				os.system("clear")
				file = open("Banner/dictionary")
				sys.stdout.write(GREEN)
				print file.read()
				print colored("   1:", "white")+colored("Small list", "white")
				print colored("   2:", "white")+colored("Medium list", "white")
				print colored("   3:", "white")+colored("Large list", "white")
				print colored("   00:", "white")+colored("Main Menu", "white")
				print("\n \n")
				menu_choice = input(colored("<Zyluxisgod>", "blue"))
				
#Small list
				if menu_choice==1:
					os.system("clear")
					os.system("wordlist -m 8 -M 8 -o list.txt 1234567890")
					break
		
#Medium list
				elif menu_choice==2:
					os.system("clear")
					os.system("wordlist -m 8 -M 12 -o medlist.txt 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
					break
					
#Large list
				elif menu_choice==3:
					os.system("clear")
					os.system("wordlist -m 8 -M 24 -o medlist.txt 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
					break
					
		
#Random password
		elif menu_choice==2:
			os.system("clear")
			while True:
				length = int(input(("Length:")))
				chars =(string.ascii_letters+string.digits)
				ems = ""
				for i in range(length):
					ems= ems+(random.choice(chars))
				print(ems)
		
#Just in case
		else:
			print("One of the options please")

				
				
#Big break
	elif menu_choice1==00:
		os.system("clear")
		break
		
#Just in case
	else:
		print("One ofe the optiones please")
