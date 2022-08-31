operator = input("Enter operator :")
firstNum = input("Enter FirstNum :")
secondNum = input("Enter SecondNum :")
FaultyDict={"45*3":"555", "56+9":"77","56/6":"4"}
expression = firstNum+operator+secondNum
reverse = secondNum+operator+firstNum
if expression in FaultyDict.keys():
    print (FaultyDict[expression])
    pass
elif reverse in FaultyDict.keys():
    print (FaultyDict[reverse])
    pass
else:
    print(eval(firstNum+operator+secondNum))