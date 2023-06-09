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
    "int gig0/2",
    "int switchport",
    "int gig0/2.20",
    "encapsulation dot1Q 20",
    "ip address 192.168.20.1 255.255.255.0",
    "no shutdown",
    "vlan 250", #สร้าง vlan 250
    "name Netmiko-VLAN", #ตั้งชื่อ name Netmiko-VLAN
    "end",
    "show vlan bri", #แสดง vlan
    "show ip int bri"
    ]

with ConnectHandler(**dev) as router_connect:
    router_connect.enable()
    config_outputs = router_connect.send_config_set(config_commands)

print(config_outputs)
router_connect.disconnect()