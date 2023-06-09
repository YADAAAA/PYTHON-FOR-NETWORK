import getpass
import telnetlib

#user = input('Enter your telnet username: ')
#password = getpass.getpass()

user = "admin"
password = "Cisco@123"

Host = "172.16.212.127"
tn = telnetlib.Telnet(Host)
tn.read_until(b'Username: ')
tn.write(user.encode('ascii') + b'\n')

if password:
    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii') + b'\n')

tn.write(b"enable\n")
tn.write(password.encode('ascii') + b'\n')
tn.write(b"conf t\n")
tn.write(b"int gi0/2\n")
tn.write(b"int gi0/3\n")
tn.write(b"switchport access vlan 100\n")
tn.write(b"end\n")
tn.write(b"show vlan bri\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))