
with open('input.txt', 'r') as reader:
    numbers = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
numbers = [int(x.strip()) for x in numbers]
numbers.sort()
for i in range(0, len(numbers)-1):
    s = set()
    for j in range(i+1, len(numbers)):
        if 2020 - numbers[j] - numbers[i] in s:
            print(numbers[i] * numbers[j] * (2020 - numbers[j] - numbers[i]))
            break
        s.add(numbers[j])

