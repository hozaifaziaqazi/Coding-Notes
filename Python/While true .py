"""
H =0
while(H<101):
    print(H)
    H = H + 1
    """
H = 0
"""while True:
 print(H + 1, end=" ")
 if H == 44:
    break
 H = H + 1"""

"""E = 0
while True:
    E = E + 1
    if E + 1 < 5:
        continue
    print(E + 1, end=" ")
    if E == 44:
     break
E = E + 1"""


while True:
    Q = int(input("Enter a number:"))
    if Q==50 or Q==100 or Q==500 or Q==1000 or Q==5000:
        print("Congrats you have entered a correct number")
        break
    elif Q>100:
        print("Number Did Not Match Try Again")
        continue
    else:
        print("Number Did Not Match Try Again")
        continue