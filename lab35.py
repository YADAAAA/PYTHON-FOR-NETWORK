import time
from ping3 import ping 	
import telnetlib 
from netmiko import ConnectHandler
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
    reponse = ping(IP,unit='ms')    #Return float
    print(int(reponse))             #float to int

    with ConnectHandler(**dev) as router_connect:
        router_connect.enable() 
        reponse = ping(IP,unit='ms')
        if reponse < 10:
            print("HOST : " + IP + " Very Slow (delay " + str(round(reponse,2)) + " ms)")
            mess1 = "HOST : " + IP + " Very Slow (delay " + str(round(reponse,2)) + " ms)"
            PLINE.post(message = mess1)      
        time.sleep(2)
        router_connect.disconnect()

    #ใส่โค้ดตรวจสอบถ้า Delay(ไม่เกิน 10ms) มากกว่าที่เรากำหนดให้
    #ส่งข้อความเข้าไลน์
    #เช่น Host : 172.16.212.120 Very Slow(delay xxx ms)