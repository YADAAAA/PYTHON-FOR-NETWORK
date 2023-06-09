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
    "ip route 202.44.32.0 255.255.255.0 gig0/0",
    "ip route 202.44.33.0 255.255.255.0 gig0/0",
    "ip route 202.44.34.0 255.255.255.0 gig0/0",
    "end",
    "show ip route"
    ]

with ConnectHandler(**dev) as router_connect:
    router_connect.enable()
    config_outputs = router_connect.send_config_set(config_commands)

print(config_outputs)
router_connect.disconnect()