with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]

index = 0

count_trees = 0
for row in array:
    count_trees += (row[index % len(row)] == "#")
    index += 3


print(count_trees)
