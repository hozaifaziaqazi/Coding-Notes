# Health Management System
# 3 clients - Zia, Sadia and Hozaifa.
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Zia-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Zia-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Sadia-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Sadia-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Hozaifa-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Hozaifa-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Zia),2(Sadia),3(Hozaifa)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Zia-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Zia-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Sadia-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Sadia-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Hozaifa-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Hozaifa-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Zia,Sadia,Hozaifa)")


print("Welcome to Health Management System: ")
a = int(input("Press 1 for Input the value and 2 for Output: "))

if a == 1:
    b = int(input("Press 1 for Zia 2 for Sadia 3 for Hozaifa "))
    take(b)
else:
    b = int(input("Press 1 for Zia 2 for Sadia 3 for Hozaifa "))
    retrieve(b)
