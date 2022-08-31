with open("hozaifa.txt") as f:
    a = f.readlines()
    print(a)

# there is no need to close the file like this
# f.close
f = open("hozaifa.txt")
print(f.readlines())