from netmiko import ConnectHandler
from getpass import getpass

dev = {
    'device_type' : 'cisco_ios',
    'host' : '172.16.212.127',
    'username' : 'admin',
    'password' : 'Cisco@123',
    'secret' : 'Cisco@123'
    } #Parameters-Dictionary

with ConnectHandler(**dev) as router_connect:
    router_connect.enable()
    output = router_connect.send_command("show running-config")
    router_connect.disconnect()

with open("R1.txt",'w') as file:
    file.write(output)
    file.close()