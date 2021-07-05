import os, math
from collections import Counter
import sys

arguments = sys.argv[1::]
results_array = {}

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

    elif arguments[i] in ("-p", "-print-confidence"):
        config["confidence_print"] = True


for i in next(os.walk(config["dir"]))[2]:
    with open(config["dir"]+"/"+i, 'rb') as f:
        byteArr = list(f.read())
    p, lns = Counter(byteArr), len(byteArr)
    aa = []
    for count in p.values():
        aa.append(count/lns * math.log(count/lns, 2))
    entropy = int(-sum(aa) / 8 * 100)
    results_array[i] = entropy


if config["descending"] == True:
    results_array = sorted(results_array.items(), 
                            key=lambda x: x[1], reverse=True)
elif config["ascending"] == True:
    results_array = sorted(results_array.items(),
                            key=lambda x: x[1])


for key in results_array:
    if key[1] > config["confidence"]:
        if config["confidence_print"] == True:
            print(str(key[1])+"%", key[0])
        else:
            print(key[0])