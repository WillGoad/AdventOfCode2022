def symbolToNumber(symbol):
    if symbol == 'A' or symbol == 'X':
      return 1
    elif symbol == 'B' or symbol == 'Y':
      return 2
    elif symbol == 'C' or symbol == 'Z':
      return 3
    else:
      return 0

def playerWin(opponentNum, playerNum):
    if(playerNum == 1 and opponentNum == 3):
       return True
    elif(playerNum == 2 and opponentNum == 1):
       return True
    elif(playerNum == 3 and opponentNum == 2):
       return True
    else:
       return False


def calculateRoundScore(opponentChoice, playerChoice):
    playerNum = symbolToNumber(playerChoice)
    opponentNum = symbolToNumber(opponentChoice)

    if(playerNum == opponentNum):
       return playerNum + 3
    elif(playerWin(opponentNum, playerNum)):
       return playerNum + 6
    else:
       return playerNum

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