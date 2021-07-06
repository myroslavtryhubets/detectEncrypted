import os
import math
import sys
from collections import Counter

arguments = sys.argv[1::]
confidence_array = []
config = {
    "dir": os.getcwd(),
    "confidence": 80,
    "descending": False,
    "ascending": False,
    "confidence_print": False
}

for i in range(len(arguments)):
    if arguments[i] in ("-d", "--dir"):
        i += 1
        config["dir"] = arguments[i]

    elif arguments[i] in ("-c", "--confidence"):
        i += 1
        config["confidence"] = int(arguments[i])

    elif arguments[i] in ("-s"):
        config["descending"] = True

    elif arguments[i] in ("+s"):
        config["ascending"] = True

    elif arguments[i] in ("-p", "--print-confidence"):
        config["confidence_print"] = True

    elif arguments[i] in ("-h", "--help"):
        print("""Command line arguments:
    -d, --dir: specifies the path to directory where to look for encrypted/compressed files. Default - current directory.
    -c, --confidence: specifies the threshold level of confidence (in percents from 0 to 100) to treat a certain file as encryped/compressed. Default - 80%.
    -s: all files in the program output should be sorted by confidence level descending (from high to low).
    +s: all files in the program output should be sorted by confidence level ascending (from low to high).
    -p, --print-confidence: print the confidence level along with the file name.
    -h, --help: print help message for all available options.""")
        exit(0)


for file_name in next(os.walk(config["dir"]))[2]:
    with open(config["dir"] + "/" + file_name, 'rb') as file:
        byte_array = list(file.read())

    counter_byte = Counter(byte_array)
    len_byte = len(byte_array)
    entropie_array= []
    
    for count in counter_byte.values():
        entropie_array.append(count / len_byte * math.log(count / len_byte, 2))

    confidence = int(-sum(entropie_array) / 8 * 100)
    confidence_array.append((file_name, confidence))


if config["descending"] == True:
    confidence_array.sort(key=lambda x: x[1], reverse=True)

elif config["ascending"] == True:
    confidence_array.sort(key=lambda x: x[1])

for element in confidence_array:
    if element[1] > config["confidence"]:

        if config["confidence_print"] == True:
            print(str(element[1])+"%", element[0])
        else:
            print(element[0])
