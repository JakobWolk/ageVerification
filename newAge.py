# importing the modules for the programming libraries
import os
import time
import re

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

DLinfo = message
print(message.replace(" ", ""))

myString = DLinfo
myString = re.sub(r"[\n\t\s]*", "", myString)
print(myString)

text = new

found = re.search('DBB(.+?)DBA', text).group(1)

print(found)




