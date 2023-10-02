def doesContain(array):
    if(array[0] >= array[2] and array[1] <= array[3]):
        return 1
    elif(array[2] >= array[0] and array[3] <= array[1]):
        return 1
    else:
        return 0
    
def mapAssignmentRange(assignmentRange):
    assignmentRangeArray = assignmentRange.split('-')
    return [int(assignmentRangeArray[0]), int(assignmentRangeArray[1])]

def TwoDto1Darray(list_2D):
    return [item for sub_list in list_2D for item in sub_list]

    
def getAssignmentArray(line):
    assingmentRangesArray = line.split(',')
    return TwoDto1Darray(map(mapAssignmentRange, assingmentRangesArray))

def calculateAssignmentPairsCount(file):
    count = 0
    for line in file.readlines():
        count = count + doesContain(getAssignmentArray(line))
    return count

file = open('input.txt')
try:
    print(calculateAssignmentPairsCount(file))
finally:
  file.close()