# display philipppine geo time
# display date & weather

def mainscripthere():

    # a loop to check if it is indeed a floating number
    def infinity():
        try:
            return float(input("enter a value: "))
        except ValueError:
            return infinity()  
    
    value_for_initial_temperature = infinity()
    value_for_initial_temperature
    # i'm trying to loop the 2 input statements in order to check if the user do happen to input the letters K F C R both upper and lower
    
    def initial_temperature():
        try:
            char_for_initial_temperature1 = input("heya, what's the sign for your temperature? \n type C for celsius \n type K for kelvin \n type F for fahrenheit \n type R for Rankine \n TYPE AWAY: ").upper()
            if (((char_for_initial_temperature1[0] == "K") or (char_for_initial_temperature1[0] == "F") or (char_for_initial_temperature1[0] == "C") or (char_for_initial_temperature1[0] == "R")) and (len(char_for_initial_temperature1) == 1)):
                return char_for_initial_temperature1 #+ char_for_conversion
            else:
                return initial_temperature()
        except IndexError:
            return initial_temperature()
    char_for_initial_temperature = initial_temperature()
    char_for_initial_temperature

    def final_temperature():
        try:
            char_for_conversion = input("hey so what temperature would you like this to be converted to? \n type C for celsius \n type K for kelvin \n type F for fahrenheit \n type R for Rankine \n TYPE AWAY: ").upper()
            if (((char_for_conversion[0] == "K") or (char_for_conversion[0] == "F") or (char_for_conversion[0] == "C") or (char_for_conversion[0] == "R")) and (len(char_for_conversion) == 1)):
                return char_for_conversion #+ char_for_conversion
            else:
                return final_temperature()
        except IndexError:
            return final_temperature()
    char_for_conversion =  final_temperature()
    char_for_conversion
    
    # main function for checking initial unit
    def conversion():
        if char_for_initial_temperature == "C":
            if char_for_conversion == "K": # -- converts celsius to kelvin
                return conversionforcelsius(1)
            elif char_for_conversion == "F":
                # (9/5)* 0°C+32 = 32F -- converts celsius to fahrenheit
                return conversionforcelsius(2)
            elif char_for_conversion == "R":
                # 0°C × 9/5 + 491.67 = 491.67°R -- converts celsius to rankine
                return conversionforcelsius(3)
            else:
                # return the value for Celsius
                return conversionforcelsius(0)
        elif char_for_initial_temperature == "F":
            if char_for_conversion == "C": # -- converts fahrenheit to celsius
                return conversionforfahrenheit(1)
            elif char_for_conversion == "K": # converts fahrenheit to kelvin
                return conversionforfahrenheit(2)
            elif char_for_conversion == "R": # converts fahrenheit to rankine
                return conversionforfahrenheit(3)
            else:
                # return the value for Fahrenheit
                return conversionforfahrenheit(0)
            # if else statement for the conversion of fahrenheit to the three other units
        elif char_for_initial_temperature == "K":
            if char_for_conversion == "C": # -- converts kelvin to celsius
                return conversionforkelvin(1)
            elif char_for_conversion == "F": # converts kelvin to fahrenheit
                return conversionforkelvin(2)
            elif char_for_conversion == "R": # converts kelvin to rankine
                return conversionforkelvin(3)
            else:
                # return the value for Fahrenheit
                return conversionforkelvin(0)
        else:
            if char_for_conversion == "C": # -- converts rankine to celsius
                return conversionforrankine(1)
            elif char_for_conversion == "F": # converts rankine to fahrenheit
                return conversionforrankine(2)
            elif char_for_conversion == "R": # converts rankine to kelvin
                return conversionforrankine(3)
            else:
                # return the value for Fahrenheit
                return conversionforrankine(0)

    def conversionforcelsius(num):
        # 0°C + 273.15 = 273.15K
        # (9/5)* 0°C+32 = 32F
        # 0°C × 9/5 + 491.67 = 491.67°R
        if num == 1:
            return value_for_initial_temperature + 273.15
        elif num == 2:
            return (9/5)* value_for_initial_temperature + 32
        elif num == 3:
            return (9/5) * value_for_initial_temperature + 491.67
        else:
            return value_for_initial_temperature

    def conversionforkelvin(num):
        # conversion to K-C K-F K-R
        #  0K - 273.15 = 0°C
        # (0K − 273.15) × 9/5 + 32 = -459.7F
        # R = 1.8*K
        if num == 1:
            return (value_for_initial_temperature - 273.15) # kelvin to celsius
        elif num == 2:
            return (value_for_initial_temperature - 273.15) * (9/5) + 32 # fahrenheit
        elif num == 3:
            return (value_for_initial_temperature * 1.8) # rankine
        else:
            return (value_for_initial_temperature)

    def conversionforfahrenheit(num):
        # 32F -32 * 5/9 = C
        # (32F - 32) * 5/9 + 273.15 = K
        # R = 459.67 + 0F
        if num == 1:
            return (value_for_initial_temperature - 32) * (5/9) # fahrenehit to celsius
        elif num == 2:
           return (value_for_initial_temperature - 32) * (5/9) + 273.15 # fahrenheit to kelvin 
        elif num == 3:
            return (value_for_initial_temperature + 459.67) # fahrenheit to rankine
        else:
            return  (value_for_initial_temperature)
    
    def conversionforrankine(num):
        #°C= 0°R * 5/9 - 491.67
        # 0R - 459.67 = F
        # K = R/1.8
        if num == 1:
            return (value_for_initial_temperature * (5/9) - 491.67) # convert rankine to celsius 
        elif num == 2:
            return (value_for_initial_temperature - 459.67) #convert ranknie to fahrenheit
        elif num == 3:
            return (value_for_initial_temperature / 1.8) # convert rankine to kelvin
        else:
            return (value_for_initial_temperature)

    conversion_temp = conversion()
    print(conversion_temp)

    # recieve input from user then analyzes what the value and temperature is, then detects what temperature they want to convert to
# values will go through a series of if else statements checking the validity if it's k, f, c, r and then checking if there's a number
if __name__ == "__main__":
    mainscripthere()
