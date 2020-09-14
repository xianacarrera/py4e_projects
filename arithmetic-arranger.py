''' 
    Author: Xiana Carrera Alonso
    Date: 21/08/2020
    This is a program made for the 'Scientific Computing with Python' course of freeCodeCamp.
    This code corresponds to the first assigment, 'Arithmetic Formatter'.
    The purpose of the code is to 'create a function that receives a list of strings that are 
    arithmetic problems and returns the problems arranged vertically and side-by-side'.
    Complete instructions for this assigment can be found at
    https://repl.it/repls/OutrageousPunctualHypercard#README.md
'''



def arithmetic_arranger(my_list, resp = False):
    # arithmetic_arranger receives a list with the set of problems and an optional argument indicating is answers are required or not
    # It returns a string with the appropiate format or a description of an error in case one occured
    
    list_len = len(my_list)
    if list_len > 5 :
        return("Error: Too many problems.")
        # The program accepts up to 5 problems
    
    evrth = []    
    for op in my_list :
        prob = op.split()
        # prob now should contain 3 elements: the first number of the operation, the operator and the second number
        
        if len(prob) != 3 :
            return("Error: Incorrect format.")
            # This error was added to prevent errors in case the format isn't the specified one
        
        if prob[1] != "+" and prob[1] != "-" :
            return("Error: Operator must be '+' or '-'.")
            # No more operations are allowed
        
        if not(prob[0].isdigit() and prob[2].isdigit()) :
            return("Error: Numbers must only contain digits.")
            
        if len(prob[0]) > 4 or len(prob[2]) > 4 :
            return("Error: Numbers cannot be more than four digits.")
        
        prob.append(max(len(prob[0]), len(prob[2])))    # This line will prove useful later on
        evrth.append(prob)

    # All comprobations were passed. On to the real code
    text = ""       # The final string that will be returned
    for i in range(list_len) :           # First line
        for j in range(2 + evrth[i][3] - len(evrth[i][0])) :    # There are always 2 blank spaces. Additional blank spaces depend on a comparison of the numbers length
            text = text + " "
        text = text + evrth[i][0]       # First number is added
        if i == (list_len - 1) :         # Final loop -> new line
            text = text + "\n"
        else :                          # Not the final loop -> 4 spaces
            text = text + "    "
    
    
    for i in range(list_len) :           # Second line
        text = text + evrth[i][1]       # The operator is added
        for j in range(1 + evrth[i][3] - len(evrth[i][2])) :    # Same as before, only that there is only one mandatory space (the other one was used for the operator)
            text = text + " "
        text = text + evrth[i][2]       # Second number
        if i == (list_len - 1) :
            text = text + "\n"
        else :
            text = text + "    "


    for i in range(list_len) :           # Dashed line
        for j in range(2 + evrth[i][3]) :       # The two aforementioned spaces + the largest number 
            text = text + "-"
        if i != (list_len - 1) :
            text = text + "    "
        elif resp:
            text = text + "\n"
    
    if resp :    # Answers are required
        for i in range(list_len) :
            num1 = int(evrth[i][0])
            num2 = int(evrth[i][2])
            ans = num1 + num2 if evrth[i][1] == "+" else num1 - num2
            for j in range(2 + evrth[i][3] - len(str(ans))) :
                text = text + " "
            text = text + str(ans)
            if i != (list_len - 1) :
                text = text + "    "
    
    return(text)
    
        
        
        
              
        
print(arithmetic_arranger(["32 + 698", "1 - 3801", "45 + 43", "123 + 49"], True))


# Note: I didn't know of the function rjust when I completed this challenge. That would have made it way easier!
