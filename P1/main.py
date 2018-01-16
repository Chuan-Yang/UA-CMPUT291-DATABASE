
#selling a car which doesn't owned by the seller
#i.e. all data need to be verified before commit to the database

import cx_Oracle
import sys
import os
import getpass
import DLR, VR, NVR, AT
import time
global cursor

def get_pass():
	user = input("Username [%s]: " % getpass.getuser())
	pw = getpass.getpass()
	return user,pw

def exit(signed_in=0): # Check for write/commit right(if error raised..)
	if signed_in == 1:
		cursor.close()
		con.close()
		sys.exit()
	else:
		sys.exit()
	return 

def main_menu():
	os.system('clear')
	print('Welcome to Auto Reistration System')
	print('Input the following number for features')
	print('1.New Vehicle Registration')
	print('2.Auto Transaction')
	print('3.Driver License Registration')
	print('4.Violation Record')
	print('5.Search Engine')
	print('0.Exit Program')
	cmd = input('Please enter your choice: ')
	if cmd not in {'0','1','2','3','4','5'}:
		print('Invalid input, please try again!')
		cmd = input('Please enter your choice: ')
	if cmd == '0':
		exit()
	elif cmd == '1':
		NVR.NVR_main()
		main_menu()
	elif cmd == '2':
		AT.AT_main()
		main_menu()
	elif cmd == '3':
		DLR.DLR_main()	
		main_menu()
	elif cmd == '4':
		VR.VR_main()
		main_menu()
	elif cmd == '5':
		SE.SE_main()
		main_menu()
	else:
		main_menu()
	

#selling a car which doesn't owned by the seller
#i.e. all data need to be verified before commit to the database

	

while True:
	try:
		user, pw = get_pass()
		con_string = user + '/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
		con = cx_Oracle.connect(con_string)
		print('111')
		break
	except cx_Oracle.Error:
		os.system('clear')
		print('Unable to connect to SQL Server.')
		print('Check Internet connection.')
		print('Check username & password.')
		while True:
			cmd = input('Press Enter to Re-attempt or Q to exit: ')
			if cmd == 'Q' or cmd == 'q':
				exit()
			elif cmd == '':
				print('222')
				user, pw = get_pass()
				break
			else:
				print ("Invalid input! Please try again!")
				continue

#user, pw = get_pass()
#user=input('1')
#pw=input('2')


con.autocommit = 1
cursor = con.cursor()

if __name__ == '__main__':
	main_menu()
