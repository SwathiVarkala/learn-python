import math
def getBaseFuelForModule(mass) :
  return math.floor(int(mass)/3)-2
def getFuelForModule(mass):
  fuel = getBaseFuelForModule(mass)
  print(int(mass),'-', fuel, '\n', end='')
  return 0 if fuel <= 0 else fuel+getFuelForModule(fuel)

totalFuel=0
with open('input.txt', 'r') as reader:
  for mass in reader :
    fuel = getFuelForModule(mass)
    print('Module Fuel', int(mass), '-', fuel, '\n', end='')
    totalFuel = totalFuel + fuel

print('total fuel', totalFuel, end='')