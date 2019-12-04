
def check_number(n):
    repeat = 0
    n = str(n)
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
          repeat = repeat+1
    return True if repeat > 0 else False 


def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))

listOfPossiblePasswords = []
otherAnswer = []
def convertToInt(array):
  res = sum(d * 10**i for i, d in enumerate(array[::-1])) 
  return(res)

def processPosition(seq, position):
  if position == 5:
    number = convertToInt(seq)
    if (number >= 240298 and number <= 784956):
      if check_number(number):
        listOfPossiblePasswords.append(number)
    return
  
  currentDigit = seq[position]
  for nextDigit in range(currentDigit,10):
    seq[position+1] = nextDigit
    processPosition(seq, position+1)
  return

processPosition([2,4,0,2,9,8], 0)
processPosition([3,4,0,2,9,8], 0)
processPosition([4,4,0,2,9,8], 0)
processPosition([5,4,0,2,9,8], 0)
processPosition([6,4,0,2,9,8], 0)
processPosition([7,4,0,2,9,8], 0)
print(len(listOfPossiblePasswords), end='\n')
