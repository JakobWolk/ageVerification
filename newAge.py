# Raw input End
import os
import time
import re
from datetime import datetime

# setting that variable i to  0.
i = 0

# a while loop starts that is infinte, 0 is always less than or equal to 10.
while i <= 10:

    # A list named data is declared
    data = []
    # Printing the text as follows
    print("\n" + "Please Swipe Your Drivers License")
    # If true
    while True:
        # take the input and declare it as the line variable
        line = input()
        # if line has data
        if line:
            # append it to each line
            data.append(line)
            # if not break the loop
        else:
            break
    # join all the data
    DLinfo = '\n'.join(data)

    text = DLinfo
    
    found = re.search('DBB(.+?)DBA', text).group(1)
    
    cardDOB = datetime.strptime(found, "%m%d%Y")
    
    print(cardDOB)
    




