def arrayToFinalElement(array):
    stackString = ''
    for i in range(len(array)):
        stackString = stackString + array[i][-1]
    return stackString

def craneInstruction(array, size, start, end):
    # where start and end are indexes of the 2d array "array" and size is the number of elements to move, move elements from start to end and return the new array
    newArray = array
    for i in range(size):
        newArray[end].append(newArray[start].pop())
    return newArray

def lineToInputs(line):
    lineArray = line.split(' ')
    return [int(lineArray[1]), int(lineArray[3])-1, int(lineArray[5])-1]

def horizontalToVertical2Darray(horizontal2Darray):
    vertical2Darray = []
    for i in range(len(horizontal2Darray[0])):
        vertical2Darray.append([])
        for j in range(len(horizontal2Darray)):
            if(horizontal2Darray[j][i] != '*'):
                vertical2Darray[i].append(horizontal2Darray[j][i])
        vertical2Darray[i] = vertical2Darray[i][::-1]
    return vertical2Darray
    
def lineToArray(line):
    array = []
    for i in range(len(line)):
        if(i % 4 == 0 and i+1 < len(line)):
            letter = line[i+1]
            if(letter == ' '):
                array.append('*')
            else:
                array.append(letter)
    return array

def calculateTopOfStacks(file):
    instructions = []
    horizontal2Darray = []
    setUpArray = True
    for line in file.readlines():
        if(line[0] == ' '):
            setUpArray = False
        if(setUpArray):
            horizontal2Darray.append(lineToArray(line))
        else:
            if(line[0] == 'm'):
                instructions.append(line)
    vertical2darray = horizontalToVertical2Darray(horizontal2Darray)
    for i in range(len(instructions)):
        inputs = lineToInputs(instructions[i])
        vertical2darray = craneInstruction(vertical2darray, inputs[0], inputs[1], inputs[2])
    topOfStacks = arrayToFinalElement(vertical2darray)
    return topOfStacks

file = open('input.txt')
try:
    print(calculateTopOfStacks(file))
finally:
  file.close()