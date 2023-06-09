from netmiko import ConnectHandler

dev = {
    'device_type' : 'cisco_ios',
    'host' : '172.16.212.127',
    'username' : 'admin',
    'password' : 'Cisco@123'
    }
    
router_conn = ConnectHandler(**dev)
print(router_conn.send_command("show arp\n"))