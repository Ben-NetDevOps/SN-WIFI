import paramiko
import re
import time

def ISValidMac(mac):
    if re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac): return True
    return False

def IPOUTPUT(output):
    if re.search(r'(IP Address\b).*', output, re.M): return True
    return False

def ISVadlidINT(i):
    if re.match(r"^[1-4]$",i,re.M): return True
    return False

## device settings
print('''
Welcome to SN WIFI TOOL For Suzhou
1. Disable the Sharkrobot WIFI (YOU DON'T HAVE THE PERMISSION)
2. Enabling the Sharkrobot WIFI (YOU DON'T HAVE THE PERMISSION)
3. Checking the IP address related the Mac address
4. Quit this application
*****************************Notes***********************************
The format of the Mac address:
    E8:2A:EA:26:B2:6D
*********************************************************************
''')
import paramiko
import time
HOST = '10.144.19.101'
Username = 'test'
Password = 'Test@123456'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname=HOST, username=Username, password=Password, look_for_keys=False)
command = ssh_client.invoke_shell()
output = 0
test = 0
# Str = input("Please input the number that you want to excute the job:");
Str = 1
i = 0
while Str != '4':
    Str = input("Please input the number that you want to excute the job:")
    i = Str
    while ISVadlidINT(Str) == False:
        print('You input the wrong number')
        break
    else:
       i = int(Str)
       if i == 1 or i == 2:
           print('YOU DON\'T HAVE THE PERMISSION')
       elif i == 3:
           MACADDRESS = input('Please input Mac address:');
           while ISValidMac(MACADDRESS) == False:
               MACADDRESS = input('Please input the right Mac address:')
           else:
               command.send('show client detail {} \n'.format(MACADDRESS))
               time.sleep(0.5)
               output = command.recv(65535).decode('ASCII')
               #print(output)
               if  IPOUTPUT(output) == False:
                   print('Sorry, We can\'t find the IP address')
               else:
                   test = re.search(r'(IP Address\b).*|(Client MAC Address\b).*', output, re.M)
                   print(test.group())
                   test = re.search(r'(IP Address\b).*', output, re.M)
                   print(test.group())
       else:
           ssh_client.close()
           print('Bye!')
else:
    ssh_client.close()