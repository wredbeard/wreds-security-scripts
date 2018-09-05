#!/usr/bin/ python3

import subprocess

#class to make that ifconfig check pop!
class bcolors:
    WARNING = "\033[93m"
    ENDC = "\033[0m"

#gather the name of the interface
print("Enter the name of the interface.\n")
print("Hint: Run ifconfig!\n")
interface = input("Interface: ")

#allow custom or default mac
address = input("\nDesired MAC Address(default is 00:00:00:00:00:01): ")
if len(address) == 17:
    print("Changing MAC to: " + address)
else:
    address = "00:00:00:00:00:01"

#execute mac address modification
subprocess.call("ifconfig " + interface + " down ", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

#warn user to check ifconfig for changes
print(bcolors.WARNING + "\nPlease check ifconfig to ensure changes!" +
      bcolors.ENDC)
print("\nPress ENTER to continue")
input()
