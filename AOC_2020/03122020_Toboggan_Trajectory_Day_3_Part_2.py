with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]

index = 0

map_of_slopes = [
    [1,1,0,0,0],
    [3,1,0,0,0],
    [5,1,0,0,0],
    [7,1,0,0,0],
    [1,2,0,0,0]
]

count_trees_index = 4
right_index = 0
down_index = 1
x_index = 2
y_index = 3

loop = len(array)
for i in range(0, loop):
    for slope in map_of_slopes:
        if slope[x_index] < loop:
            row = array[slope[x_index]]
            slope[count_trees_index] += (row[slope[y_index] % len(row)] == "#")
            slope[y_index] += slope[right_index]
            slope[x_index] += slope[down_index]

print(map_of_slopes)
print(map_of_slopes[0][count_trees_index]
      * map_of_slopes[1][count_trees_index]
      * map_of_slopes[2][count_trees_index]
      * map_of_slopes[3][count_trees_index]
      * map_of_slopes[4][count_trees_index])

# print(count_trees)
