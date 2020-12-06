with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]


group_separator = ''
questions_set = set()
total_answers = 0

array.append('')
for row in array:
    if group_separator == row:
        total_answers += len(questions_set)
        print(questions_set)
        questions_set.clear()
    else:
        for question_answered in row:
            questions_set.add(question_answered)

print(total_answers)
