# Raw input End
import os
import time
import re
from datetime import datetime

# Setting that variable i to  0.
i = 0

# A while loop starts that is infinte, 0 is always less than or equal to 10.
while i <= 10:

    # A list named data is declared
    data = []
    # Printing the text as follows
    print("\n" + "Please Swipe Your Drivers License")
    # If true
    while True:
        # Take the input and declare it as the line variable
        line = input()
        # If line has data
        if line:
            # Append it to each line
            data.append(line)
            # If not break the loop
        else:
            break
    # Join all the data
    DLinfo = '\n'.join(data)
     
    # Declare text variable as DLinfo
    text = DLinfo
    
    # Search the input string for the Date of Birth
    found = re.search('DBB(.+?)DBA', text).group(1)
    
    
    # Convert output to useable format
    cardDOB = datetime.strptime(found, "%m%d%Y")
    
 
    now = datetime.now()

    current_time = now.strftime("%m-%d-%Y")
    
    
    # Print the current time
    print("\n" + current_time)

    # Print the card DOB
    print(cardDOB)


    DB = cardDOB
    now = datetime.now()
    
    if DB <

    print(db < now)
    
    then = datetime(1985, 1, 1)
    now = datetime.now()

    diff = now - then
    print(diff)




