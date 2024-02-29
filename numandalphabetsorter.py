
""" use try and except for checking int values
use the function [a-z] if alpha
"""
#using main function in order to avoid future errors for importing
def main():
    #gets input of user
    intinput = inputchecker()
    #serves as a holder for input of user
    intinputlist = {}
    #gets an overall length for input of user
    intinputvalue = intinput[1]
    lengthofintinput = len(str(intinputvalue))
    
    #main function for sorting
    
    def sorthere(valuehere, listhere, lengthhere):
        try:
            for inter in range(lengthhere):
                currentlist = listhere[valuehere]
                oldlist = listhere[inter]
                if (currentlist < oldlist):
                    popped = listhere[inter]
                    popped2 = listhere[valuehere]
                    del listhere[inter]
                    del listhere[valuehere]
                    listhere[inter] = popped2
                    listhere[valuehere] = popped
            return valuehere, listhere, lengthhere
        except (KeyError):
            pass 

    def sorterhere():
        #contains the input value to avoid any tampering of values
        if (intinput[0] == 2):
            valuecontainer = intinputvalue
            settableshere = []
            #for loop which goes through the length of the screen of the user
            for i in range (lengthofintinput):
                lengthofintinputlist = len(intinputlist)
                # a formula in order to lessen the zeros into a workable integer number which is then put together later on
                formula = 10 ** (lengthofintinput - (i+1))
                # an equation to get the invidividual numbers of the inputted number
                container = valuecontainer // formula
                #valuecontainer to only get the individual characters of a digit and not continually repeat solving
                valuecontainer = valuecontainer - (container * formula)
                intinputlist[i] = container
                sorthere(i,intinputlist,lengthofintinputlist)
        else:
            for i in range(lengthofintinput):
            #65 - 90 A-Z and 97-122 [a-z]
                intinputlist[i] = intinputvalue[i]
                lengthofintinputlist = len(intinputlist)
                sorthere(i,intinputlist,lengthofintinputlist)        
        return print(intinputlist)
            # use .append(to add to a list)
            # use .insert(position, value)    
    sorterhere()

def inputchecker():
    inputhere = input("type here")
    if (inputhere.isnumeric()):
        return 2, int(inputhere)
    elif (inputhere.isalpha()):
        return 1, inputhere
    else:
        return inputchecker()


if __name__ == "__main__":
    main()
