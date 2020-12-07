with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]
array = [x.strip().rstrip('.') for x in array]

bag_map = {' other': ['']}
for row in array:
    split_row = row.split(' contain ')
    container = split_row[0].rstrip(' bags')
    contains = split_row[1].split(', ')
    # for bags in contains:
    if 'no other bags' not in contains:
        bag_map[container.rstrip('s')] = contains
    else:
        bag_map[container.rstrip('s')] = []


def gold_bag_count(bag) -> int:
    total = 0
    if bag not in bag_map or bag_map[bag] == []:
        return 1
    for inner_bag in bag_map[bag]:
        count = inner_bag[:1].strip(' ')
        inner_bag = inner_bag[2:].rstrip(' bags')
        total += int(count) * gold_bag_count(inner_bag)
        print(bag, ':', count, inner_bag, total)
    return total + 1


print(bag_map)

gold_bag = 'shiny gold'
print(gold_bag_count(gold_bag) -1)

