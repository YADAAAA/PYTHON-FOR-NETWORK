from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import json

dev = {
    'device_type' : 'cisco_ios',
    'host' : '172.16.212.127',
    'username' : 'admin',
    'password' : 'Cisco@123'
    }

command = "show ip int brief"
with ConnectHandler(**dev) as router_connect:
    output = router_connect.send_command(command,use_textfsm=True)

'''
router_connect.disconnect()
noip_connect = [item['intf'] for item in output if item['ipaddr'] == 'unassigned']
print(noip_connect)
'''

router_connect.disconnect()
noip_connect = [item['intf'] for item in output if item['ipaddr'] == '172.16.212.127']
print(noip_connect)