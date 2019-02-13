#!/usr/bin/env python3

##^^shebang used for > ./name.py
######################## by Robin Schneider / Crisu1710 ###################################################################################
import socket
import os

r = open('IPlist.txt', "r")
iplist = r.readlines()

w = open('ips.log', "a")

# letters to check if its a domain
letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#######################    OS color    and errors  ########################################################################################
if os.name == 'nt':
	class fg:
		RED     = ''
		BLUE    = ''
		RESET   = ''

	class bg:
		RED     = ''
		BLUE    = ''
		RESET   = ''

	class style:
		BRIGHT    = ''
		DIM       = ''
		NORMAL    = ''
		UNDERLINE = ''
		RESET_ALL = ""

	class error:
		CONNECTION = (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
		MAXLENGTH  = (fg.RED + "Max is 255.255.255.255" + style.RESET_ALL)
		IP         = (fg.RED + "Please enter a ip xxx.xxx.xxx.xxx like 192.168.2.3" + style.RESET_ALL)
		TLD        = (fg.RED + "type a name with a normal top level domain" + style.RESET_ALL)

else:
	class fg:
		RED     = '\033[31m'
		BLUE    = '\033[34m'
		RESET   = '\033[39m'

	class bg:
		RED     = '\033[41m'
		BLUE    = '\033[44m'
		RESET   = '\033[49m'

	class style:
		BRIGHT    = '\033[1m'
		DIM       = '\033[2m'
		NORMAL    = '\033[22m'
		RESET_ALL = '\033[0m'
		UNDERLINE = '\033[4m'

	class error:
		CONNECTION = (fg.RED + "NO INTERNET CONNECTION" + style.RESET_ALL)
		MAXLENGTH  = (fg.RED + "Max is 255.255.255.255" + style.RESET_ALL)
		IP         = (fg.RED + "Please enter a ip xxx.xxx.xxx.xxx like 192.168.2.3" + style.RESET_ALL)
		TLD        = (fg.RED + "type a name with a normal top level domain" + style.RESET_ALL)
################ get ip of this pc and check if internet is connected ######################################################################
try:
	PC_IP = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] #get ip from hostname (ping hostname)
	if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), # if ip starts with 127 (localhost) ping Google DNS and lisen to own IP
	s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
except Exception:
	pass
	print (error.CONNECTION)
	print (error.CONNECTION)

print ("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
█▀▀▀▀      █▀▀▀▀▀    ▀▀▀▀█▀▀▀▀         █  █▀▀▀▀█         █▀▀▀▀▀    █       █▀▀▀▀▀█    █▀▀▀▀▀▀▀   █▀▀▀▀▀▀▀
█          █             █             █  █    █         █         █       █     █    █          █
█  ▀▀█     █▀▀▀▀         █             █  █▀▀▀▀▀         █         █       █▀▀▀▀▀█    ▀▀▀▀▀▀▀█   ▀▀▀▀▀▀▀█
█    █     █             █             █  █              █         █       █     █           █          █
▀▀▀▀▀▀     ▀▀▀▀▀▀        █             █  █              ▀▀▀▀▀▀    ▀▀▀▀▀   █     █    ▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀
+++++++++++++++++++++++++++++++++++ by Robin Schneider (Crisu1710) +++++++++++++++++++++++++++++++++++++++++
""")

YorN = input("Use your own IP? (L/Y/N/?) : ") 								#your ip or other ip
if YorN.startswith ("N") or YorN.startswith ("n") or YorN == "":            # no, Type a IP
	ipadd = input("PI (xxx.xxx.xxx.xxx) or DOMAIN (name.com) : ") 			# type a ip # ip as string
	print (style.RESET_ALL)
elif YorN == "l" or YorN == "L":
	for ipadd in iplist:
		pass
elif YorN.startswith ("Y") or YorN.startswith ("y"):                        # yes, use the IP from this PC
	try:
		ipadd = PC_IP
	except Exception:
		print (error.CONNECTION)
		ipadd = input("PI : ")
		#exit()
	print (style.RESET_ALL)
	#print (ipadd)
elif YorN == "?" or YorN.startswith ("H") or YorN.startswith ("h"):         # get help use
	print (style.BRIGHT, fg.BLUE)
	print ("Type Y/y or Yes/yes to use the IP of your actual network")
	print ("Type L/l to use a list of IPs from IPlist.txt")
	print ("Type N/n or No/no to type a IP e.g. 1.1.1.1 or 192.168.2.1")
	print ("Type ?/H/h or Help/help to open this help")
	print ("Some functions only working with internet connection!")
	print ("Please make sure your connected with the Internet")
	print (style.RESET_ALL)
	#ipadd = input("PI(1.1.1.1) : ")
	#os.system("IP_Klassen.py")
	exit()
elif YorN:																	# close script
	print (fg.RED, style.BRIGHT)
	print ("Use (Y/y) or (N/n) or (?/H/h)")
	print (style.RESET_ALL)
	exit()


############## split at . to get e.g. 192 168 2 3 #########
if ipadd == "":
	print (error.IP)
	print ("The IP of your PC is automatically used" + style.RESET_ALL)
	try:
		ipadd = PC_IP
		ip = PC_IP.split(".")
	except Exception:
		print (error.CONNECTION)
		ip = ipadd.split(".")
else:
	try:
		#if ipadd.endswith (".com") or ipadd.endswith (".de") or ipadd.endswith (".org") or ipadd.endswith (".uk") or ipadd.endswith (".net"):
		if ipadd.endswith (letters):
		#if any((ipadd in letters) for ipadd in letters): # <<<<<<<<<<<<<<< is it a domain wit letters a - z
			Host = socket.gethostbyname(ipadd)
			print (Host)
			ip = Host.split(".")
		else: # its a ip (with numbers)
			try: # get the host name of the ip
				Host = socket.gethostbyaddr(ipadd)
				print (Host[0])
				ip = ipadd.split(".")
			except Exception:	# if ip can't be pinged
				ip = ipadd.split(".")
	except Exception:   # <<<<<<<<<<<<<<<< if ther isn no ping to the domain
		print (error.TLD)
		print (error.CONNECTION)
		exit()
####### split and Convert Strings into Integers P = part ######
try:
	p1 = int(ip[0]) # >>>>>>>>>>>>> # 192
	p2 = int(ip[1]) # ------------- # 168
	p3 = int(ip[2]) # >>>>>>>>>>>>> # 2
	p4 = int(ip[3]) # ------------- # 3
except Exception:
	print (error.IP)
	exit()

################ max ip ######################################
if p1 > 255 or p2 > 255 or p3 > 255 or p4 > 255:
	print (error.MAXLENGTH)
	exit()
else:
	pass

try:
	if int(ip[4]) >= 0:
		print (error.MAXLENGTH)
		exit()
	else:
		pass
except Exception:
	pass
### remove 0b and max/min 8 bit bp = binary part ###
bp1 = str(bin(p1))[2:].zfill(8) # 11000000
bp2 = str(bin(p2))[2:].zfill(8) # 10101000
bp3 = str(bin(p3))[2:].zfill(8) # 00000010
bp4 = str(bin(p4))[2:].zfill(8) # 00000011
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
############### privat or puplic ################################
if IPclass == (" A"):
	if p1 == 0:
		pp = ("Routing ")
	elif p1 == 127:
		pp = ("Localhost ")
	elif p1 != 10:
		pp = ("PUBLIC ")
	else:
		pp = ("PRIVATE ")
elif IPclass == (" B"):
	if p1 == 169 and p2 == 254:
		pp = ("APIPA ")
	elif p2 < 16 or p2 > 31 or p1 != 172:
		pp = ("PUBLIC ")
	else:
		pp = ("PRIVATE ")
elif IPclass == (" C"):
	if p1 != 192 or p2 != 168:
		pp = ("PUBLIC ")
	else:
		pp = ("PRIVATE ")
elif IPclass == (" D"):
	pp = ("MULTICAST ")
elif IPclass == (" E"):
	if p1 == 255:
		mask = str(bp1 + bp2 + bp3 + bp4)
		print ("ID :", mask.count("1"))
		pp = ("SUBNET MASK ")
	else:
		pp = ("RESEARCH ")

print (ipadd,end= " >>> ")
print (style.UNDERLINE + fg.RED + bp1[:3] + style.RESET_ALL + style.UNDERLINE + bp1[3:] + " " + bp2 + " " + bp3 + " " + bp4,end= "")
print (style.RESET_ALL + " >>> " + fg.RED + pp + "CLASS" + IPclass)
print (style.RESET_ALL)
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
##################################################################

w.write(ipadd + "\n")
w.close()

clear_all = input("clear terminal? Y/N : ")
if clear_all.startswith ("Y") or clear_all.startswith ("y"):
	if os.name == 'nt':
		clear = lambda: os.system('cls') #windows
		clear()
	else:
		clear = lambda: os.system('clear') #linux
		clear()
else:
	exit()
