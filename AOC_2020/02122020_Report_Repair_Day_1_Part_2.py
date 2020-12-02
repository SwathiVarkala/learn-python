
with open('input.txt', 'r') as reader:
    numbers = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
numbers = [int(x.strip()) for x in numbers]
numbers.sort()

left = 0
right = len(numbers) - 1
print(left, right, len(numbers))
while left < right:
    print(left, right)
    if numbers[left] + numbers[right] < 2020:
        left = left + 1
    elif numbers[left] + numbers[right] > 2020:
        right = right - 1
    else:
        print(numbers[left] * numbers[right])
        break
