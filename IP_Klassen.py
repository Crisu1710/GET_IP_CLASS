######################## by Robin Schneider / Crisu1710####################################################################################
import socket
import os
#######################    OS color    #####################################################################################################
if os.name == 'nt':
	class fg:
		BLACK   = ""
		RED     = ''
		GREEN   = ''
		YELLOW  = ''
		BLUE    = ''
		MAGENTA = ''
		CYAN    = ''
		WHITE   = ''
		RESET   = ''

	class bg:
		BLACK   = ''
		RED     = ''
		GREEN   = ''
		YELLOW  = ''
		BLUE    = ''
		MAGENTA = ''
		CYAN    = ''
		WHITE   = ''
		RESET   = ''

	class style:
		BRIGHT    = ''
		DIM       = ''
		NORMAL    = ''
		UNDERLINE = ''
		RESET_ALL = ""

else:
	class fg:
		BLACK   = '\033[30m'
		RED     = '\033[31m'
		GREEN   = '\033[32m'
		YELLOW  = '\033[33m'
		BLUE    = '\033[34m'
		MAGENTA = '\033[35m'
		CYAN    = '\033[36m'
		WHITE   = '\033[37m'
		RESET   = '\033[39m'

	class bg:
		BLACK   = '\033[40m'
		RED     = '\033[41m'
		GREEN   = '\033[42m'
		YELLOW  = '\033[43m'
		BLUE    = '\033[44m'
		MAGENTA = '\033[45m'
		CYAN    = '\033[46m'
		WHITE   = '\033[47m'
		RESET   = '\033[49m'

	class style:
		BRIGHT    = '\033[1m'
		DIM       = '\033[2m'
		NORMAL    = '\033[22m'
		RESET_ALL = '\033[0m'
		UNDERLINE = '\033[4m'
################ get ip of this pc #########################################################################################################
try:
	PC_IP = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] #get ip from hostname (ping hostname)
	if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), # if ip starts with 127 (localhost) ping Google DNS and lisen to own IP
	s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
except Exception:
	pass
	print (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
	print (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
#########################################################################
print ("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
█▀▀▀▀      █▀▀▀▀▀    ▀▀▀▀█▀▀▀▀         █  █▀▀▀▀█         █▀▀▀▀▀    █       █▀▀▀▀▀█    █▀▀▀▀▀▀▀   █▀▀▀▀▀▀▀
█          █             █             █  █    █         █         █       █     █    █          █
█  ▀▀█     █▀▀▀▀         █             █  █▀▀▀▀▀         █         █       █▀▀▀▀▀█    ▀▀▀▀▀▀▀█   ▀▀▀▀▀▀▀█
█    █     █             █             █  █              █         █       █     █           █          █
▀▀▀▀▀▀     ▀▀▀▀▀▀        █             █  █              ▀▀▀▀▀▀    ▀▀▀▀▀   █     █    ▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀
+++++++++++++++++++++++++++++++++++++++ by Robin Schneider ++++++++++++++++++++++++++++++++++++++++++++++++
""")

YorN = input("Use your own IP? (Y/N/?) : ") #your ip or other ip
if YorN.startswith ("N") or YorN.startswith ("n") or YorN == "":            # no, Type a IP
	ipadd = input("PI : ") # type a ip # ip as string
	print (style.RESET_ALL)
elif YorN.startswith ("Y") or YorN.startswith ("y"):                        # yes, use the IP from this PC
	try:
		ipadd = PC_IP
	except Exception:
		print (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
		ipadd = input("PI : ")
		#exit()
	print (style.RESET_ALL)
	#print (ipadd)
elif YorN == "?" or YorN.startswith ("H") or YorN.startswith ("h"):         # get help use
	print (style.BRIGHT, fg.BLUE)
	print ("Type Y/y or Yes/yes to use the IP of your actual network")
	print ("Type N/n or No/no to type a IP e.g. 1.1.1.1 or 192.168.2.1")
	print ("Type ?/H/h or Help/help to open this help")
	print ("Some functions only working with internet connection!")
	print ("Please make sure your connected with the Internet")
	print (style.RESET_ALL)
	#ipadd = input("PI(1.1.1.1) : ")
	#os.system("IP_Klassen.py")
	exit()
elif YorN:																	# close script will work wen you type exit
	print (fg.RED, style.BRIGHT)
	print ("Use (Y/y) or (N/n) or (?/H/h)")
	print (style.RESET_ALL)
	exit()

############## split at . to get e.g. 192 168 2 3 #########
if ipadd == "":
	print (fg.BLUE + "Type a IP like 1.1.1.1 or 192.168.2.3")
	print ("The IP of your PC is automatically used" + style.RESET_ALL)    #<<<<
	try:
		ipadd = PC_IP
		ip = PC_IP.split(".")
	except Exception:
		print (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
		ip = ipadd.split(".")
else:
	ip = ipadd.split(".")
####### split and Convert Strings into Integers P = part ######
try:
	p1 = int(ip[0]) # >>>>>>>>>>>>> # 192
	p2 = int(ip[1]) # ------------- # 168
	p3 = int(ip[2]) # >>>>>>>>>>>>> # 2
	p4 = int(ip[3]) # ------------- # 3
except Exception:
	print (fg.RED + "Please enter a ip xxx.xxx.xxx.xxx like 192.168.2.3" + style.RESET_ALL)
	exit()
### remove 0b and max/min 8 bit bp = binary part ###
bp1 = str(bin(p1))[2:].zfill(8) # 11000000
bp2 = str(bin(p2))[2:].zfill(8) # 10101000
bp3 = str(bin(p3))[2:].zfill(8) # 00000010
bp4 = str(bin(p4))[2:].zfill(8) # 00000011

################################# print complete IP as binary ###########
print (ipadd,end= " >>> ")
print (style.UNDERLINE + fg.RED + bp1[:3] + style.RESET_ALL + style.UNDERLINE + bp1[3:] + " " + bp2 + " " + bp3 + " " + bp4,end= "")
############## print Klasse .. ##################
if bp1.startswith ("0"):
	IPclass = (" A") # 255.0.0.0/8 comming soon
elif bp1.startswith ("10"):
	IPclass = (" B") # 255.255.0.0/16 comming soon
elif bp1.startswith ("110"):
	IPclass = (" C") # 255.255.255.0/24 comming soon
elif bp1.startswith ("1110"):
	IPclass = (" D")
elif bp1.startswith ("1111"):
	IPclass = (" E")
############### v  + '\033[0m' + '\033[5m' ##################
print (style.RESET_ALL + " >>> " + fg.RED + "CLASS" + IPclass)
print (style.RESET_ALL)
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

clear_all = input("clear terminal? Y/N : ")
if clear_all.startswith ("Y") or clear_all.startswith ("y"):
	if os.name == 'nt':
		clear = lambda: os.system('cls')
		clear()
	else:
		clear = lambda: os.system('clear')
		clear()
else:
	exit()
