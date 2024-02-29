# print("hello world")
# poggers = 12
# namev2 = "joseph"
# namehere = input("What is your name?")
# print("your name is" + namehere)
# print("\"my name is\"", namev2, poggers)
# print(len(namehere))

# print("Poggers" if namehere == "Khrist" else "FAKE")
# int - 1-16
# bool 1-1.5
# complex 1-1.3j

# arithmetic // = integer & !floating point ** = exponent

#random
# import random
# print(random.random())
# print(random.randint(1,50))
# print(random.choice(10,20,30,40))
# print(random.sample([a,b,c,d,e,f,g,h,i],j,k,l,m,n))
# listhere = ["nishi","nei","nege"]
# print(len(listhere))
# make a calculator

#what's my problem? what if the user placed a lot of numbers?

# -- variables ---
check = 1
ans = 0
operatornum = 0
listhere = ["-",".","0","1","2","3","4","5","6","7","8","9"]
list2 = ["+","-","//","/","**","*","%"]
# get input, check number if it corresponds with the list
userinput = None
ui2 = None
ui3 = None
lenlisth = len(listhere)
lenlist2 = len(list2) - 1
while True :
    rebound = 0
    userinput = input("put number here")
    lengthui = len(userinput) - 1
    # checks number inside of userinput
    for x, unknown in enumerate(userinput):
        # checks how much number there is in the list
        for i,unknown2 in enumerate(listhere):
            # compares the inside of userinput with the list and if it matches it returns 1
            if ((userinput == "ans") | (userinput == "ANS")):
                    break
            elif (unknown == unknown2):
                if((x >= 1) & (unknown2 == listhere[0])):
                    rebound = 2
                    check = 2
                    break
                break
            # since the input is always a string, asking if the 
            elif (unknown != unknown2):
                if(i == 11):
                    check = 2
                    rebound = 1
                    break
        if (check != 1):
            break
    #checks whether or not it matches with the list
    if (rebound == 1):
        print("not a number")
        break
    elif (rebound == 2):
        print("wrong place for negative")
        break
    else:
        ui2 = input("operators here")
        for num2, unknown5 in enumerate(ui2):
            for num, unknown3 in enumerate(list2):   
                if (ui2 == unknown3):
                    break
                elif ((ui2 != unknown3) & (num == lenlist2)):
                    rebound = 1
                    break            
        if (rebound == 1):
            print("incorrect operator")
            break
        else:
            ui3 = input("put another number here")
            lenui3 = len(ui3) - 1
            for y, unknown3 in enumerate(ui3):
                # checks how much number there is in the list
                for z,unknown4 in enumerate(listhere):
                    # compares the inside of userinput with the list and if it matches it returns 1
                    if ((userinput == "ans") | (userinput == "ANS")):
                        break
                    if (unknown3 == unknown4):
                        if((y >= 1) & (unknown4 == listhere[0])):
                            rebound = 2
                            check = 2
                            break
                        break
                    # since the input is always a string, asking if the 
                    elif (unknown3 != unknown4):
                        if(z == 11):
                            check = 2
                            rebound = 1
                            break
                if (check != 1):
                    print("d")
                    break
            #checks whether or not it matches with the list
            if (rebound == 1):
                print("not a number")
                break
            elif (rebound == 2):
                print("wrong place for negative")
                break
            else:
                last1 = userinput + ui2 + ui3
                print(eval(last1))
                ans = eval(last1)
    while True:
        anothainput = input("exit? y or n?")
        if(anothainput == "y"):
            break
        elif(anothainput == "n"):
            rebound = 1
            break
    if (rebound == 0):
        break