for x in range(5):
    print("* "* 5)
print ("")
for x in range(5):
    print("* "*(x+1))
print ("")
for x in range(5):
    if x == 0 or x == 4:
        print("* "*5)
    else:
        print("*       *")