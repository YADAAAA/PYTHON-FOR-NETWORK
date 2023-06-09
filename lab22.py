import getpass
import telnetlib

user = input('Enter your telent username : ')
password = getpass.getpass()

Host = "172.16.212.127"
tn = telnetlib.Telnet(Host)
tn.read_until(b'Username')
tn.write(user.encode('ascii') + b'\n')

if password:
    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii') + b'\n')

tn.write(b"enable\n")
tn.write(password.encode('ascii') + b'\n')
tn.write(b"conf t\n")

'''
tn.write(b"int gi0/1\n")
tn.write(b"no ip address\n")
#tn.write(b"no switchport\n")
#tn.write(b"ip address 192.168.10.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"end\n")
tn.write(b"show ip int bri\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))
'''

tn.write(b"int gi1/1\n")
tn.write(b"no ip address\n")
tn.write(b"no switchport\n")
tn.write(b"ip address 192.168.10.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"end\n")
tn.write(b"show ip int bri\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))