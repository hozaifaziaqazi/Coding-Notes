def runagain():
    user = input("Do u want to run again? y/n : ")
    if(user=="y"):
        mygame()
    elif(user=="n"):
        print("Bye Bye Thankyou ")

def mygame():
        car = str(input("What Is Your Car Name:"))
        if car == "Yaris" or car == "yaris":
            print("Excellent")
            runagain()

        elif car == "Aslvin" or car == "alsvin":
            print("Good")
            runagain()

        elif car == "Gli" or car == "gli":
            print("Not Bad")
            runagain()

        elif car == "City" or car == "city":
            print("Bad")
            runagain()

        else:
            print("Good Enough")
            runagain()


mygame()

