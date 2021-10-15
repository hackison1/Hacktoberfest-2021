import re
import subprocess
import time
import pyfiglet 
import optparse

#Function to change MAC
def changer():
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
        subprocess.call(["ifconfig", interface, "up"])


#optparser
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface",help="Mac Interface")
parser.add_option("-m", "--mac", dest="newMac",help="New Mac Address")

(option, arguments) = parser.parse_args()
if not option.newMac:
    parser.error("MacError")
if not option.interface:
    parser.error("Interface Error")


#Show Off
asciitext = pyfiglet.figlet_format("Mac Changer")
print(asciitext) 

interface = option.interface
newMac = option.newMac
#Make Sure You are Su 0
print("Make Sure You are Admin")




#Process
print("Changing Your Mac Address...")
time.sleep(5)
changer()
print("Successfully Changed")
if changer:
    print("sucess")
else:
    print("Failed")


ifconfig_report = subprocess.check_output(["ifconfig", option.interface])
print (ifconfig_report))
