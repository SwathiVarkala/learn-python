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
  # print('before',gap[:index+10])
  if index == len(gap)-1:
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
    valueIndex = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    print('print diagnosis code',gap[valueIndex], end=',')
    index +=2
  # print('index:', index, 'values:', gap[index], gap[index+1], gap[index+2], gap[index+3])
  elif opCode == 2:
    value1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    value2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    value3Index = getIndexOfValueForParamMode(paramModes.get(2, 0), index+3, gap[index+3])
    gap[value3Index] = gap[value1Index] * gap[value2Index]
    if index+5 <= len(gap)-1 : 
      index = index+4
  elif opCode == 1:
    value1Index = getIndexOfValueForParamMode(paramModes.get(0, 0), index+1, gap[index+1])
    value2Index = getIndexOfValueForParamMode(paramModes.get(1, 0), index+2, gap[index+2])
    value3Index = getIndexOfValueForParamMode(paramModes.get(2, 0), index+3, gap[index+3])
    # print('opcode:', opCode,'------[',value1Index,']',gap[value1Index],' + [',value1Index,']', gap[value2Index],' = at', gap[value3Index])
    gap[value3Index] = gap[value1Index] + gap[value2Index]
    if index+5 <= len(gap)-1 : 
      index = index+4
  else:
    print(gap[index],' at ',index,'Unknown OpCode: ', opCode, end='\n')
    exit()
  # print('after',gap[:index+10])
  processIntCode(gap, index)


with open('input.txt', 'r') as reader:
  gravityAssitProgram = reader.readline()
  # print(gravityAssitProgram, end='')
  gap = list(map(int, gravityAssitProgram.split(',')))
  #gap = gravityAssitProgram.split(',')
  #Bring back 1202 Program Alart State
  print(len(gap), end='')
  processIntCode(gap, 0)
  # print(gap, end='')
