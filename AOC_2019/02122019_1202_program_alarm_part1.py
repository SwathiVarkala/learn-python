def processIntCode(gap, index):
  if gap[index] == 99:
    return
  print('index:', index, 'values:', gap[index], gap[index+1], gap[index+2], gap[index+3])
  if gap[index] == 2:
    gap[gap[index+3]] = gap[gap[index+1]] * gap[gap[index+2]]
  elif gap[index] == 1:
    gap[gap[index+3]] = gap[gap[index+1]] + gap[gap[index+2]]
  else:
    print('Unknown OpCode: ', gap[index], end='\n')
  print('indexes:', index)
  if index+5 <= len(gap)-1 : 
    index = index+4
    processIntCode(gap, index)


with open('input.txt', 'r') as reader:
  gravityAssitProgram = reader.readline()
  print(gravityAssitProgram, end='')
  gap = list(map(int, gravityAssitProgram.split(',')))
  #gap = gravityAssitProgram.split(',')
  #Bring back 1202 Program Alart State
  gap[1] = 12
  gap[2] = 2
  print(len(gap), end='')
  processIntCode(gap, 0)
  print(gap, end='')
