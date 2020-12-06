with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]

map_chars = {'a': 0}
group_separator = ''
questions = [0] * 26
total_answers = 0
count_person = 0
print(ord('a'))
array.append('')
for row in array:
    if group_separator == row:
        for question in questions:
            if count_person == question:
                total_answers += 1
        print(questions)
        print('count_person: ', count_person, 'total_answers: ', total_answers)
        questions = [0] * 26
        count_person = 0
    else:
        for question_answered in row:
            questions[ord(question_answered) - 97] += 1
        count_person += 1

print(total_answers)
