import getpass
import telnetlib

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
tn.write(b"int gi1/0\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"switchport trunk allow vlan 100,200,300\n")
tn.write(b"end\n")
tn.write(b"show int trunk\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))