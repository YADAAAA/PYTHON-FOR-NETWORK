import datetime
import time
from netmiko import ConnectHandler
import sys
from linenotipy import Line

PLINE = Line(token ='UnCvXF6Q9zYVwac0FK49xLGTXK19QTwuLB66HNHg0oV')

count = 0
DeviceFile = open("ip.txt",'r')
Lines = DeviceFile.read().splitlines()
DeviceFile.close()

for IP in Lines:
    count += 1
    dev = {
        'device_type' : 'cisco_ios',
        'host' : IP,
        'username' : 'admin',
        'password' : 'Cisco@123',
        'secret' : 'Cisco@123'
            }

    with ConnectHandler(**dev) as router_connect:
        router_connect.enable()
        OuputConfig = router_connect.send_command("show run\n")
        PMessage = "Backup " + IP + " Processing.."
        print(PMessage)
        PLINE.post(message= PMessage)
        Date = str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))
        FileName = IP + "-" + Date +".txt"

        with open(FileName,'w') as CFGFile:
            CFGFile.write(OuputConfig)
            CFGFile.close()
            PLINE.post(message = "Success!")
            print("Success!")
    router_connect.disconnect()