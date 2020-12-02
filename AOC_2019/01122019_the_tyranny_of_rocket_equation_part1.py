import math

totalFuel=0
with open('input.txt', 'r') as reader:
 for mass in reader :
   fuel = math.floor(int(mass)/3)-2
   print(mass, '-', fuel, '\n', end='')
   totalFuel = totalFuel + fuel
print('Total Fuel', totalFuel, end='')