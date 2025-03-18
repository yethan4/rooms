from collections import defaultdict

from chrem import chrem_multiple

def solution(nr):
  rooms = defaultdict(int)

  with open(f"data/{nr}.in")  as f:
    data = f.read().splitlines()

  n = int(data[0]) 
  kidsNumber = int(data[1])
  roomNumbers = list(map(int, data[2].split()))
  targetRoomNumbers = list(map(int, data[3].split()))
  scheme = [ {'A': 0, 'B': 1, 'C': 2, 'D': 3}[letter] for letter in [i for i in data[4]] ]
  schemeLength = len(scheme)

  for i in range(5, 5+n):
    rooms[i-4] = list(map(int, data[i].split()))

  counter = 1
  schemeId = 1

  achieved = 0
  visitedStates = set()
  results = [defaultdict(lambda: defaultdict(list, {0: 0}), {0: 0}) for _ in range(kidsNumber)]
  toSolve = True
  while True and counter<1000000:
    for i in range(kidsNumber):
      newRoom = rooms[roomNumbers[i]][scheme[(schemeId -1) % schemeLength]]
      roomNumbers[i] = newRoom
      
      if newRoom in targetRoomNumbers:
        if results[i][0] == 0:
          if results[i][newRoom][0] == 0 and schemeId != 0:
            if len(results[i][newRoom][schemeId]) == 0:
              results[i][newRoom][schemeId] = [1, counter]
            elif results[i][newRoom][schemeId][0] == 1:
              results[i][newRoom][schemeId][0] = 2
              results[i][newRoom][schemeId].append(counter)
            else:
              continue
            isAchived = True
            
            for key, val in results[i][newRoom].items():
              if key == 0:
                continue
              if val[0] != 2:
                isAchived = False
                break;
            if isAchived:
              results[i][newRoom][0] = 1
              achieved += 1
    
    if achieved == kidsNumber:
      break 
    
    currentState = (tuple(roomNumbers), schemeId)
    if currentState in visitedStates:
      toSolve = False
      return "NIE"
    visitedStates.add(currentState)
    
    if set(roomNumbers).issubset(targetRoomNumbers):
      return counter
    
    schemeId = (schemeId) % schemeLength + 1
    counter+=1
  
  if toSolve and achieved == kidsNumber:
    checkSchemesIds = defaultdict(int)
    for i in range(kidsNumber):
      for roomNr, roomItems in results[i].items():
        if roomNr==0:
          continue
        for key, val in roomItems.items():
          if key==0:
            continue
          checkSchemesIds [key] += 1

    schemeIds = [key for key, value in checkSchemesIds.items() if value == kidsNumber]
    
    for schemeId in schemeIds:
      congruences = []
      try:
        for j in range(kidsNumber):
          for roomNr, roomItems in results[j].items():
            if roomNr==0:
              continue
            for key, val in roomItems.items():
              if key==schemeId:
                congruences.append((val[1], val[2]-val[1]))
        return(chrem_multiple(congruences)[0])
      except:
        continue
  return "NIE"

for i in range(1, 14):
    if i == 3:
        continue
    print(f"{i:02}.in -> {solution(f'{i:02}')}")
