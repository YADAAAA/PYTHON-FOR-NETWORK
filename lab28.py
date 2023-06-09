from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

dev = {
    'device_type' : 'cisco_ios',
    'host' : '172.16.212.127',
    'username' : 'admin',
    'password' : 'Cisco@123'
    }

command = "show ip int brief"
with ConnectHandler(**dev) as router_connect:
    output = router_connect.send_command(command,use_textfsm=True)

print()
pprint(output)
print()