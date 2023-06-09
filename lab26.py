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
tn.write(b"ip route 202.44.33.0 255.255.255.0 gi0/0\n")
tn.write(b"ip route 202.44.34.0 255.255.255.0 gi0/0\n")
tn.write(b"ip route 202.44.35.0 255.255.255.0 gi0/0\n")
tn.write(b"end\n")
tn.write(b"show ip route\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))