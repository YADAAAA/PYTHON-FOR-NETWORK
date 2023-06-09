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
    
tn.write(b"show ip int bri\n")
tn.write(b'exit\n')
output = tn.read_all()
print(output.decode('ascii'))