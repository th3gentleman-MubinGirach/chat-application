import socket 
import os 
import threading

selection=input('Please enter the O.S you are using windows/linux: ')
if (selection == 'linux'):
	os.system('clear')
	os.system('ifconfig')



	os.system('tput setaf 4')
	print("Hey welcome to the chat application by th3gentleman..Mubin Girach")
	print('\n')
	os.system('tput setaf 7')

	


	selfip=input("Enter the IP address of your NIC CARD (enp0s3): ")
	selfport=input("Enter your desired port in range of 0-65353: ")
	selfport=int(selfport)

	a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	a.bind((selfip,selfport))



	connectip=input("Enter the IP you want to connect: ")
	connectport=input("I am a bit techie pls give port no also (; : ")
	connectport=int(connectport)
	os.system('tput setaf 2')
	print("Note 1: Please press enter after you receive a message & you want to send another message")
	print("Note 2: If you want exit the application you can simply say pls exit ")


	def send():
		while True:
			os.system('tput setaf 3')
			my_str=input("Enter your message: ")
			if (my_str == 'pls exit'):
				os.system('tput setaf 7')
				os._exit(1)
			my_str_as_bytes = str.encode(my_str)
			a.sendto(my_str_as_bytes,(connectip,connectport))
		

	def rcv():
		while True:
			bytes=a.recvfrom(1000)
			print('\n')
			os.system('tput setaf 6')
			print("You got a message")
			print(bytes[0].decode())
	
	


	x=threading.Thread(target=send)
	y=threading.Thread(target=rcv)
	y.start()
	x.start()



elif (selection == 'windows'):
	os.system('cls')
	os.system('ipconfig')

	


	print("Hey welcome to the chat application by th3gentleman..Mubin Girach")
	print('\n')
	




	selfip=input("Enter the IP address of your NIC CARD (enp0s3): ")
	selfport=input("Enter your desired port in range of 0-65353: ")
	selfport=int(selfport)
	
	a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	a.bind((selfip,selfport))



	connectip=input("Enter the IP you want to connect: ")
	connectport=input("I am a bit techie pls give port no also (; : ")
	connectport=int(connectport)

	print("Note 1: Please press enter after you receive a message & you want to send another message")
	print("Note 2: If you want exit the application you can simply say pls exit ")


	def send():
		while True:
		
			my_str=input("Enter your message: ")
			if (my_str == 'pls exit'):
				os._exit(1)
			my_str_as_bytes = str.encode(my_str)
			a.sendto(my_str_as_bytes,(connectip,connectport))
		

	def rcv():
		while True:
			bytes=a.recvfrom(1000)
			print('\n')
			print("You got a message")
			print(bytes[0].decode())
		
	


	x=threading.Thread(target=send)
	y=threading.Thread(target=rcv)
	y.start()
	x.start()

	



