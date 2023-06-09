import datetime
import time
from ping3 import ping 	
import telnetlib 
from netmiko import ConnectHandler
import sys
from linenotipy import Line

PLINE = Line(token ='UnCvXF6Q9zYVwac0FK49xLGTXK19QTwuLB66HNHg0oV')

DeviceFile = open("ip.txt",'r')
#DeviceFile = open("IPRouterLab.txt",'r')
TXTIPs = DeviceFile.read().splitlines()
DeviceFile.close()

count = 0
user = "admin"
password = "Cisco@123"

for IP in TXTIPs:
    count += 1
    dev = {
        'device_type' : 'cisco_ios',
        'host' : IP,
        'username' : 'admin',
        'password' : 'Cisco@123',
        'secret' : 'Cisco@123'
            }
#---------------- Check Host Up/Down ----------------------  
with ConnectHandler(**dev) as router_connect:
    router_connect.enable() 
    reponse = ping(IP,unit='ms')
    if reponse != None:
        print("Hey : " + IP + " is UP. Delay : " + str(round(reponse,2)) + " ms")
        mess1 = "Hey : " + IP + " is UP. Delay : " + str(round(reponse,2)) + " ms"
        PLINE.post(message = mess1)      
    else:
         print(IP+" is Down !!")
         mess1_2 = IP+" is Down !!"
         PLINE.post(message = mess1_2)  
    time.sleep(2)

#-----------------Check Telnet Enable --------------------- 
    tn = telnetlib.Telnet(IP)   
    if tn.read_until(b'Username: '):			
        tn.write(user.encode('ascii') + b'\n')
        tn.read_until(b'Password: ') 		
        tn.write(password.encode('ascii') + b'\n')
        print("Hey : " + IP + " Telnet is OK.")
        mess2 = "Hey : " + IP + " Telnet is OK."
        PLINE.post(message = mess2) 
        tn.close()
    else:
        print("Hey : " + IP + " Telnet isn't work!!.")
        mess2_2 = "Hey : " + IP + " Telnet isn't work!!."
        PLINE.post(message = mess2_2) 
    time.sleep(2)

#----------------- Check SSH Enable ------------------------
    dev = {
    'device_type' : 'cisco_ios',
    'host' : IP,
    'username' : user,
    'password' : password
        }
    with ConnectHandler(**dev) as router_connect:
        print("Host : " + IP + " SSH is OK.")
        mess3 = "Host : " + IP + " SSH is OK."
        PLINE.post(message = mess3) 
        router_connect.disconnect()
    print("")
    time.sleep(3)

#pip install ping3  # install ping3
#pip install --upgrade ping3 # upgrade ping3
#pip uninstall ping3  # uninstall ping3