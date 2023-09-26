def sumCalories(file):
  totalCaloriesArray = []
  currentTotal = 0
  for line in file.readlines():
     if(line != '\n'):
       currentTotal = currentTotal + int(line)
     else:
       totalCaloriesArray.append(currentTotal)
       currentTotal = 0
  return totalCaloriesArray

def sumHighestThreeElements(array):
  prevArr = array
  topThree = []
  for i in range (0,3):
    index = prevArr.index(max(prevArr))
    value = prevArr[index]
    topThree.append(value)
    prevArr.pop(index)
  return sum(topThree)
  
file = open('input.txt')
try:
   sumCalArr = sumCalories(file)
   print(max(sumCalArr))
   print(sumHighestThreeElements(sumCalArr))
finally:
  file.close()

