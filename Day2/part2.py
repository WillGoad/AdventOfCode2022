#Where rock is A, paper is B, and scissors is C and goal is X: you need to lose, Y: you need to tie, Z: you need to win, return what you need to play


def calculateRoundScore(opponentChoice, goal):
    score = 0
    if(goal == "X"):
       if(opponentChoice == "A"):
            score = score + 3
       elif(opponentChoice == "B"):
            score = score + 1
       else: 
            score = score + 2
    elif(goal == "Y"):
        if(opponentChoice == "A"):
            score = score + 1
        elif(opponentChoice == "B"):
            score = score + 2
        else: 
            score = score + 3
        score = score + 3
    else:
        if(opponentChoice == "A"):
            score = score + 2
        elif(opponentChoice == "B"):
            score = score + 3
        else: 
            score = score + 1
        score = score + 6
    return score

def calculateTotalScore(file):
    totalScore = 0
    for line in file.readlines():
        totalScore = totalScore + calculateRoundScore(line[0], line[2])
    return totalScore




file = open('input.txt')
try:
    print(calculateRoundScore('A', 'Y'))
    print(calculateRoundScore('B', 'Z'))
    print(calculateRoundScore('C', 'Y'))
    totalScore = calculateTotalScore(file)
    print(totalScore)
finally:
  file.close()