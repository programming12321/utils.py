# ----------- STRING UTILITIES -----------
def startsWith(string, prefix):
    return string[:len(prefix)] == prefix

def endsWith(string, suffix):
    return string[-len(suffix):] == suffix

def reverseString(string):
    return string[::-1]

def toBinary(num):
    return bin(num)[2:]

def fromBinary(binaryString):
    return int(binaryString, 2)

def toHex(num):
    return hex(num)[2:]

def fromHex(hexString):
    return int(hexString, 16)

def removeSpaces(string):
    return string.replace(" ", "")

# ----------- MATH UTILITIES -----------
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def toRoman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def fromRoman(romanString):
    val = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
        'I': 1
    }
    i = 0
    num = 0
    while i < len(romanString):
        if i + 1 < len(romanString) and romanString[i:i+2] in val:
            num += val[romanString[i:i+2]]
            i += 2
        else:
            num += val[romanString[i]]
            i += 1
    return num

# ----------- LIST UTILITIES -----------
def reverseList(lst):
    return lst[::-1]

def removeDuplicates(lst):
    return list(set(lst))

# ----------- ARCHIVE UTILITIES -----------
def readJSON(filePath):
    import json
    with open(filePath, 'r') as file:
        return json.load(file)
    
def writeJSON(filePath, data):
    import json
    with open(filePath, 'w') as file:
        json.dump(data, file, indent=4)

def fileExists(path):
    import os
    return os.path.exists(path)

# ----------- OTHER -----------
def wait(seconds):
    import time
    time.sleep(seconds)

def currentTime():
    import datetime
    return datetime.datetime.now().strftime("%H:%M:%S")

def currentDate():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d")
