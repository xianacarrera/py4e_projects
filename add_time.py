''' 
    Author: Xiana Carrera Alonso
    Date: 22/08/2020
    This is a program made for the 'Scientific Computing with Python' course of freeCodeCamp.
    This code corresponds to the second assigment, 'Time Calculator'.
    The purpose of the code is to 'write a function named "add_time" that can add a duration 
    to a start time and return the result'.
    Complete instructions for this assigment can be found at
    https://repl.it/repls/LargeDirectModem#README.md
'''


def add_time(ini, dur, day = None) :
    # add_time takes a start time in the 12-hour format, a duration time in hours and minutes, and an optional day of the week
    # The function adds the duration time to the start time and returns the result
    # No libraries are allowed
   
    try :
        # Decode the ini parameter into two integers that express the initial time
        ini = ini.split()
        
        ini[0] = ini[0].split(":")
        
        # ini_hour is stored in a 24-hour format
        ini_hour = int(ini[0][0]) % 12 if ini[1] == "AM" else int(ini[0][0]) % 12 + 12
        ini_min = int(ini[0][1])
        
        # Decode the dur parameter into two integers that express the duration
        dur = dur.split(":")
        for i in range(2) :
            dur[i] = int(dur[i])
    
    except :
        return("Error: incorrect format")
    
    passed_days = dur[0] // 24
    dur[0] = dur[0] % 24

    # Sum the duration to the initial time
    end_min = (ini_min + dur[1]) % 60
    carry = (ini_min + dur[1]) // 60
    
    end_hour = (ini_hour + dur[0] + carry) % 24
    passed_days += (ini_hour + dur[0] + carry) // 24 
    

    # Transform the result into the required format
    if end_hour < 12 :
        form = "AM"
    else :
        form = "PM"
        end_hour = end_hour % 12
    
    if end_hour == 0 :
        end_hour = 12
    
    msg = ""
    if passed_days == 1 :
        msg = " (next day)"
    elif passed_days > 1 :
        msg = " (" + str(passed_days) + " days later)" 
    # If no days passed, msg is just an empty string
    
    final_day = ""
    if day :   
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(7) :
            if day.lower().capitalize() == week_days[i] :      # day is case insensitive
                final_day = week_days[(i + passed_days) % 7]
        return(str(end_hour) + ":" + str(end_min).rjust(2, "0") + " " + form + ", " + final_day + msg)
    
    # If day was not provided, the return format must be different
    return(str(end_hour) + ":" + str(end_min).rjust(2, "0") + " " + form + msg) 
    
print(add_time("6:30 PM", "205:12"))
