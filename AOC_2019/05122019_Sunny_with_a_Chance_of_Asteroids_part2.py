import math

def getOpCodeParamModesMap(opCodeParamModes):
  # print('opCodeParamModes',opCodeParamModes)
  paramModesMap = {i: key for i, key in enumerate(list(map(int,str(math.floor(opCodeParamModes / 100))[::-1])))}
  return opCodeParamModes % 100, paramModesMap

def getIndexOfValueForParamMode(paramMode, position, valueAtPosition):
  if paramMode == 1 :
    return position
  else:
    return valueAtPosition

def processIntCode(gap, index):
  # print(index, 'before',gap[:index+10])
  # print(index, 'before',gap)
  if index >= len(gap):
    exit()
  opCode, paramModes = getOpCodeParamModesMap(gap[index])
  # print('opCode:', opCode, 'paramModes:', paramModes);
  if opCode == 99:
    print('halting',end='\ln');
    return
  elif opCode == 3:
    gap[gap[index+1]] = int(reader.readline())
    index +=2
  elif opCode == 4:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    print('\n-------------------print diagnosis code',gap[param1Index], end='-------------------------------\n')
    index +=2
  elif opCode == 5:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    if gap[param1Index] != 0:
      index = gap[param2Index]
    else : index +=3
  elif opCode == 6:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    if gap[param1Index] == 0:
      index = gap[param2Index]
    else: index +=3
  elif opCode == 7:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    param3Index = getIndexOfValueForParamMode(1, index+3, gap[index+3])
    if gap[param1Index] < gap[param2Index] :
      gap[gap[param3Index]] = 1
    else:
      gap[gap[param3Index]] = 0
    index +=4
  elif opCode == 8:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    param3Index = getIndexOfValueForParamMode(1, index+3, gap[index+3])
    if gap[param1Index] == gap[param2Index] :
      gap[gap[param3Index]] = 1
    else:
      gap[gap[param3Index]] = 0
    index +=4

  # print('index:', index, 'values:', gap[index], gap[index+1], gap[index+2], gap[index+3])
  elif opCode == 2:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    param3Index = getIndexOfValueForParamMode(paramModes.get(2, 0), index+3, gap[index+3])
    gap[param3Index] = gap[param1Index] * gap[param2Index]
    if index+5 <= len(gap)-1 : 
      index = index+4
  elif opCode == 1:
    param1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    param2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    param3Index = getIndexOfValueForParamMode(paramModes.get(2, 0), index+3, gap[index+3])
    # print('opcode:', opCode,'------[',param1Index,']',gap[param1Index],' + [',param1Index,']', gap[param2Index],' = at', gap[param3Index])
    gap[param3Index] = gap[param1Index] + gap[param2Index]
    if index+5 <= len(gap)-1 : 
      index = index+4
  else:
    print(gap[index],' at ',index,'Unknown OpCode: ', opCode, end='\n')
    exit()
  # print(index, 'after',gap[:index+10])
  # print(index, 'after',gap)
  processIntCode(gap, index)


with open('input.txt', 'r') as reader:
  gravityAssitProgram = reader.readline()
  # print(gravityAssitProgram, end='')
  gap = list(map(int, gravityAssitProgram.split(',')))
  #gap = gravityAssitProgram.split(',')
  #Bring back 1202 Program Alart State
  # print(len(gap), end='')
  processIntCode(gap, 0)
  # print(gap, end='')
