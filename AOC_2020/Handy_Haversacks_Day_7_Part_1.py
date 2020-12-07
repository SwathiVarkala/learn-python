with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]
array = [x.strip().rstrip('.') for x in array]

bag_map = {' other bag': []}
for row in array:
    split_row = row.split(' contain ')
    container = split_row[0]
    contains = split_row[1].split(', ')
    # for bags in contains:
    bag_map[container.rstrip('s')] = contains


def is_gold_bag(bag):
    for inner_bag in bag_map[bag]:
        if inner_bag[2:].rstrip(' bags') == 'shiny gold':
            return True
        if is_gold_bag(inner_bag.rstrip('s')[2:]):
            return True
    return False

print(bag_map)

gold_bag_count = 0
for bag in bag_map:
    gold_bag_count += is_gold_bag(bag)

print(gold_bag_count)
