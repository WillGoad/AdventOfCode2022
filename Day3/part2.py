def getpriority(letter):
    letterAscii = ord(letter)
    if(letterAscii > 96):
        return letterAscii - 96
    else:
        return letterAscii - 38 # -64 + 26
    
def findMatchingLetter(line1, line2, line3):
    for i in range(0, len(line1)):
        for y in range(0, len(line2)):
            for z in range(0, len(line3)):
                if(line1[i] == line2[y] == line3[z]):
                    return line1[i]

def calculateTotalPriority(file):
    lineArr = []
    totalPriority = 0
    for line in file.readlines():
        #If line ends in \n, remove it
        if(line.endswith('\n')):
            line = line[:-1]
        lineArr.append(line);
    #Loop through lineArr, printing every third line (starting at 0)
    for i in range(0, len(lineArr), 3):
        totalPriority = totalPriority + getpriority(findMatchingLetter(lineArr[i], lineArr[i+1], lineArr[i+2]))
    return totalPriority

file = open('input.txt')
try:
    print(calculateTotalPriority(file))
finally:
  file.close()