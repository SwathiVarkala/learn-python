def processIntCode(gap, index):
  if gap[index] == 99:
    return
  if gap[index] == 2:
    gap[gap[index+3]] = gap[gap[index+1]] * gap[gap[index+2]]
  elif gap[index] == 1:
    gap[gap[index+3]] = gap[gap[index+1]] + gap[gap[index+2]]
  else:
    print('Unknown OpCode: ', gap[index], end='\n')
  if index+5 <= len(gap)-1 : 
    index = index+4
    processIntCode(gap, index)


with open('input.txt', 'r') as reader:
  gravityAssitProgram = reader.readline()
  print(gravityAssitProgram, end='')
  for noun in range(0,99):
    for verb in range(0,99):
      gap = list(map(int, gravityAssitProgram.split(',')))
      gap[1] = noun
      gap[2] = verb
      processIntCode(gap, 0)
      if gap[0] == 19690720:
        print(gap, end='\n')
        print('noun:', noun, 'verb:', verb, end='')
        exit()
