#Start Info Imports/Start !!!DO NOT ALTER!!!
import random
import stats
import base
import severity
import os
import events
start=1
rods=5
condition=100
crew=100
mechanics=100
status=0
usage=100
sub=0
#END IMPORTS

#name=input("What is your name? ") THIS LIKELY ISN'T USED
sub=input("Choose a class for your sub.(Scout, Attack, Transportation) ")

#End Info
if sub=="Scout":
    print("")
    print("Your sub is the Scouter, a Scout Class vessel with a ")
    print("max horizontal speed of 22 km/h, maxdiving speed of 12 km/h, and armed with 2 ")
    print("coilguns and one electric discharge coil.")
elif sub=="Attack":
    print("")
    print("Your sub is the Scout, a Scout Class vessel with a")
    print("max horizontal speed of 18 km/h, maxdiving speed of 12 km/h, and an improved") 
    print("armament with 3 coilguns and one electric discharge coil.")
elif sub=="Transportation":
    print("")
    print("Your sub is the Carrier, a transport class vessel")
else:
    print("INVALID")
start=0
#Functions !!!DO NOT ALTER!!
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def event():
    if severity.polarity==1:
        print("")
        print("TEST GOOD PASS")
    elif severity.polarity==0:
        print("")
        print("TEST BAD PASS")
    elif severity.polarity==2:
        print("")
        print("TEST NEUTRAL PASS")
    else:
        print("")
        print("TEST FAILED")
def status():
    if start!=1:
        print("")
        stats.status()
def leave():
    choice=input("Are you ready to undock? (Y/N)")
    if choice=="Y":
        clear()
        status()
        print(f"Leaving from {base.outpost}")
    else:
        events.outpost
#End Functions

#TESTING AREA
