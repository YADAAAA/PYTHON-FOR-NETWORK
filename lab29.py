from netmiko import ConnectHandler
from getpass import getpass

dev = {
    'device_type' : 'cisco_ios',
    'host' : '172.16.212.127',
    'username' : 'admin',
    'password' : 'Cisco@123',
    'secret' : 'Cisco@123'
    }

config_commands = [
    "int gig0/1",
    "ip address 192.168.10.1 255.255.255.0",
    "no shutdown",
    "no switchport",
    "end",
    "show ip int bri"
    ]

with ConnectHandler(**dev) as router_connect:
    router_connect.enable()
    config_outputs = router_connect.send_config_set(config_commands)
print(config_outputs)
router_connect.disconnect()