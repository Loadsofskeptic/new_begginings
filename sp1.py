'''
Answered by: Tan, Khristian Roi C.
School: Manila Cathedral School
Section: STEM 12 - ST. BASIL THE GREAT
'''

'''problem set 1'''

print("Answered by: Tan, Khristian Roi C.")
print("School: Manila Cathedral School")
print("Section: STEM 12 - ST. BASIL THE GREAT\n")

#converts cm to inch, foot, and meter

userInput = float(input("type any centimeter value to convert to both inch, foot, and meter: "))
def cmconverter(num):
    inch = num * 0.393701
    foot = num * 0.0328084
    meter = num/100
    print("inch: ", inch)
    print("foot: ", foot)
    print("meter: ", meter)

cmconverter(userInput)

#converts fahrenheit to celsius and kelvin
print("\nconvert from fahrenheit to celsius and kelvin")
userInput = float(input("type any fahrenheit value to convert to both celsius and kelvin "))
def tempconverter(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"the value of fahrenheit to celsius is: {celsius}")
    print(f"the value of fahrenheit to kelvin is: {kelvin}")

tempconverter(userInput)

#applies the formula of the area of a right triangle
print("\n finding the area of a right triangle")
userInput1 = int(input("type number for the base of the triangle "))
userInput2 = int(input("type the height for the triangle "))
def areaOfRightTriangle(base,height):
    return (base*height)/2

print("The area of the right triangle is", areaOfRightTriangle(userInput1, userInput2))

#exponentiates the input of the user
print("\n raising a number to the power of n")
userInput1 = int(input("type your base number "))
userInput2 = int(input("type your exponent "))
def powerOf (num, exponent):
    return num ** exponent

print(f"the value is: {powerOf(userInput1,userInput2)}")

#basic mathematical operations
print("\n type any number for x and y to know each value for each mathematical operation")
userInput1 = int(input("type any number "))
userInput2 = int(input("type another number "))
def basicMathOperations (x,y):
    print(f"sum: {x+y}")
    print(f"difference: {x-y}")
    print(f"product: {x*y}")
    print(f"quotient {x/y}")
    print(f"average: {(x+y)/2}")
    print(f"power: {x**y}")

basicMathOperations (userInput1, userInput2)

'''
Answered by: Tan, Khristian Roi C.
School: Manila Cathedral School
Section: STEM 12 - ST. BASIL THE GREAT
'''

'''problem set 2'''

print("\n PROBLEM SET 2")

#checks whether the input is odd or even through a module operator and a conditional statement
print("\n Odd or Even checker")
userInput = int(input("type number to check for odd or even"))
def oddEvenChecker(num):
    if (num%2 == 0):
        return "even"
    else:
        return "odd"

print(oddEvenChecker(userInput))

# input 3 grades and compute
print("\n grade checker")
userInput1 = int(input("type your first grade"))
userInput2 = int(input("type your second grade"))
userInput3 = int(input("type your last grade"))
def gradeChecker(num1,num2,num3):
    average = (num1 + num2 + num3)/3
    if (average >= 90):
        return "A"
    elif (average >= 80 and average < 90):
        return "B"
    elif (average >= 70 and average < 80):
        return "C"
    elif (average >= 60 and average < 70):
        return "D"
    elif (average >= 60 and average < 50):
        return "E"
    else:
        return "F"

print("your grade is: ", gradeChecker(userInput1,userInput2,userInput3))

#compares num1, num2, and num3 and checks which is the largest
print("\n checks number that is the greatest")
userInput1 = int(input("type your first number "))
userInput2 = int(input("type your second number "))
userInput3 = int(input("type your last number "))
def numChecker (num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
print(f"the greatest number is {numChecker(userInput1, userInput2, userInput3)}")

#asks the user for three angles and then checks it if the angle adds up to 180
print("\n checks if the triangle is correct")
userInput1 = int(input("type your first angle "))
userInput2 = int(input("type your second angle "))
userInput3 = int(input("type your last angle "))
def triangleChecker (angle1, angle2, angle3):
    sumOfAngles = angle1 + angle2 + angle3
    if sumOfAngles != 180:
        return "The triangle is not valid."
    else:
        return "The triangle is valid"
    
print(triangleChecker(userInput1, userInput2, userInput3))

#ask the user for celsius and enters it into an if-else statement to see it's classification"
print("\n checks the classification of temperature through the value of celsius")
userInput = int(input("type any value for celsius: "))
def tempChecker (celsius):
    if celsius < 0:
        return "Freezing Weather"
    elif celsius >= 0 and celsius < 10:
        return "Very Cold Weather"
    elif celsius >= 10 and celsius < 20:
        return "Cold Weather"
    elif celsius >= 20 and celsius < 30:
        return "Normal"
    elif celsius >= 30 and celsius < 40:
        return "Hot"
    else:
        return "Its Very Hot"

print(tempChecker(userInput))