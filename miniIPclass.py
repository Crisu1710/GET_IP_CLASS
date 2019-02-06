# by Robin Schneider / Crisu1710
import socket
import os
ipadd = input("IP : ")
ip = ipadd.split(".")
p1 = int(ip[0])
bp1 = str(bin(p1))[2:].zfill(8)
if bp1.startswith ("0"):
	IPclass = (" A")
elif bp1.startswith ("10"):
	IPclass = (" B")
elif bp1.startswith ("110"):
	IPclass = (" C")
elif bp1.startswith ("1110"):
	IPclass = (" D")
elif bp1.startswith ("1111"):
	IPclass = (" E")
print ("CLASS" + IPclass)
