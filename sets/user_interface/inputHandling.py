import re

def cleanUp(txt):
    # find all numbers in the input
    values = re.findall("-?[0-9]+", txt)
    #convert them to integers
    for i in range(len(values)):
        try:
            values[i] = int(values[i])
        except:
            return "Input array contains non-digit characters"
    return set(values)
