import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

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
#tn.write(b"vlan 100\n")
#tn.write(b"name PR-Department\n")
#tn.write(b"end\n")
tn.write(b"vlan 200\n")
tn.write(b"name IT-Department\n")
tn.write(b"end\n")
tn.write(b"vlan 300\n")
tn.write(b"name ITDI-Department\n")
#tn.write(b"end\n")
tn.write(b"show vlan bri\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))