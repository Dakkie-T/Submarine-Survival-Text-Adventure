import random
def outpost():
    print("OUTPOST EVENT TEST")
def roam():
    print("ROAMING EVENT TEST")
def bomb():
    print("BOMB EVENT SUCCESS")
    """
    This will be the bomb outpost event.
    User discovers someone messing with a trashcan, vending machine, or other device.
    NPC will inform player that they are placing a bomb.
    User has three options; help, ignore, or report
    Each choice goes through unique branches of variable length
    with unique outcomes
    """
    #TEXT DEVELOPMENT:
    """
    You see someone in a mechanics uniform on their knees working on the vending machine.
        #OPTIONS:
        1.Ignore
        2.Look Closer
        3.Ask what they're doing
    #OPTION 1:
    You continue on, set chance for explosion to happen while crewmembers are near.
    END
    #OPTION 2:
        You peer over their shoulder, watching them mess with a bundle of wires on a device that clearly doesn't belong.
        The person jumps as they notice you, dropping the device. "Don't scare me like that!"
            #OPTION 1B:
            1."What is that you're working on?
            2."My bad, i'll go now."
            3."This looks suspicious. Security!"
            #OPTION 1C:
            "It's uh..." The person hesitates. "Its a bomb."
            1. Offer to help 
            2. Ignore and move on
            3. Report to security
                #OPTION 1D:
                "You rewire the device successfully and begin to hear a ticking. A timer pops up saying 1:00"
                END 
    
    """
def trash():
    print("You notice a pair of unlabelled bottles in a trashcan. One is blue and the other is green. You take a sniff and the blue one singes in your nostrils.")
    choice=input("Which one do you take? 1: Blue. 2: Green. 3: Neither")
    if choice=="1":
        print("")
    elif choice=="2":
        print("")
    elif choice=="3":
        print("You place the vials back and continue onwards.")
    else:
        print("[INVALID CHOICE]")
def breakout():
    print("CRAWLER EVENT SUCCESS")
def random_outpost():
    event=random.randint(0,100)
    if event % 2 == 0:
        print("No event")
    else:
        polarity=random.choice("gbn")
        severity=random.choice("lmh")
        if polarity=="g":
            if severity=="l":
                event=random.randint(1,4)
            if severity=="m":
                event=random.randint(5,7)
            if severity=="h":
                event=random.randint(8,10)
            #INSERT 10 GOOD EVENTS
            if event==1:
                print("GOOD EVENT 1")
            elif event==2:
                print("GOOD EVENT 2")
            elif event==3:
                print("GOOD EVENT 3")
            elif event==4:
                print("GOOD EVENT 4")
            elif event==5:
                print("GOOD EVENT 5")
            elif event==6:
                print("GOOD EVENT 6")
            elif event==7:
                print("GOOD EVENT 7")
            elif event==8:
                print("GOOD EVENT 8")
            elif event==9:
                print("GOOD EVENT 9")
            elif event==10:
                print("GOOD EVENT 10")
            else:
                print("ERROR ERROR ERROR ERROR")
        elif polarity=="b":
            if severity=="l":
                event=random.randint(1,4)
            if severity=="m":
                event=random.randint(5,7)
            if severity=="h":
                event=random.randint(8,10)
            #INSERT 10 BAD EVENTS 
            if event==1:#LAB BREAKOUT
                """
                CRAWLER RESEARCH LAB BERAKOUT
                BEGINS COMBAT WITHOUT PREPERATION AND INITIIATIVE
                """
                breakout()
            elif event==2:
                print("BAD EVENT 2")
            elif event==3:
                print("BAD EVENT 3")
            elif event==4:
                print("BAD EVENT 4")
            elif event==5:
                print("BAD EVENT 5")
            elif event==6:
                print("BAD EVENT 6")
            elif event==7:
                print("BAD EVENT 7")
            elif event==8:
                print("BAD EVENT 8")
            elif event==9:
                print("BAD EVENT 9")
            elif event==10:
                print("BAD EVENT 10")
            else:
                print("ERROR ERROR ERROR ERROR")
        elif polarity=="n":
            if severity=="l":
                event=random.randint(1,4)
            if severity=="m":
                event=random.randint(5,7)
            if severity=="h":
                event=random.randint(8,10)
            #INSERT 10 NUETRAL/CHOICE EVENTS 
            if event==1:
                trash()
                """
                THIS IS THE TRASHCAN EVENT
                """
            elif event==2:
                print("NUETRAL EVENT 2")
            elif event==3:
                print("NUETRAL EVENT 3")
            elif event==4:
                print("NUETRAL EVENT 4")
            elif event==5:
                print("NUETRAL EVENT 5")
            elif event==6:
                print("NUETRAL EVENT 6")
            elif event==7:
                print("NUETRAL EVENT 7")
            elif event==8:
                print("NUETRAL EVENT 8")
            elif event==9:
                print("NUETRAL EVENT 9")
            elif event==10:#BOMB EVENT
                bomb()
            else:
                "SMTH WRONG???"
        else:
            polarity="smth went wrong"
