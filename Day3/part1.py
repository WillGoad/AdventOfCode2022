def getpriority(letter):
    print(letter)
    letterAscii = ord(letter)
    if(letterAscii > 96):
        return letterAscii - 96
    else:
        return letterAscii - 38 # -64 + 26
    
def findMatchingLetter(line):
    lineFirstHalf = line[0:int(len(line)/2)]
    lineSecondHalf = line[int(len(line)/2):]
    for i in range(0, len(lineFirstHalf)):
        for y in range(0, len(lineSecondHalf)):
            if(lineFirstHalf[i] == lineSecondHalf[y]):
                return lineFirstHalf[i]

def calculateTotalPriority(file):
    totalPriority = 0
    for line in file.readlines():
        totalPriority = totalPriority + getpriority(findMatchingLetter(line))
    return totalPriority

file = open('input.txt')
try:
    print(calculateTotalPriority(file))
finally:
  file.close()