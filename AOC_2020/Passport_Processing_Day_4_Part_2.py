with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
array.append('')
optional_fields = ['cid']
mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def byr(n):
    return 1920 <= int(n) <= 2002
    # - four digits; at least 1920 and at most 2002.
def iyr(n):
    return 2010 <= int(n) <= 2020
    # - four digits; at least 2010 and at most 2020.
def eyr(n):
    return 2020 <= int(n) <= 2030
    # - four digits; at least 2020 and at most 2030.
def hgt(n):
    # - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    if 'cm' in n:
        n = n.strip('cm')
        return 150 <= int(n) <= 193
    if 'in' in n:
        n = n.strip('in')
        return 59 <= int(n) <= 76
def hcl(n):
    # - a # followed by exactly six characters 0-9 or a-f.
    list_of_chars = n.lstrip('#')
    count_num = 0
    count_letter = 0
    for lit in list_of_chars:
        count_num += ord(lit) in range(ord('0'), ord(':'))
        count_letter += ord(lit) in range(ord('a'), ord('g'))

    return len(n) == 7 and n.startswith('#') and count_letter + count_num == 6

def ecl(n):
    # - exactly one of: amb blu brn gry grn hzl oth.
    return n in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and len(n) == 3

def pid(n):
    # - a nine-digit number, including leading zeroes.
    count_num = 0
    for lit in n:
        res = ord(lit) in range(ord('0'), ord(':'))
        count_num += res
    return len(n) == 9 and count_num == 9

switcher = {
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
        'pid': pid
    }


valid_passport_count = 0
total_passport = 0
person_separator = ''

fields_present_count = 0

for row in array:

    if person_separator == row:
        if fields_present_count == len(mandatory_fields):
            valid_passport_count += 1
        fields_present_count = 0
        total_passport += 1
    else:
        for field in row.split(' '):
            name, value = field.split(':')
            func = switcher.get(name, lambda: "Invalid")
            if name in mandatory_fields and func(value):
                print(row, name, '- valid')
                fields_present_count += 1
            else:
                print(row, name, '- invalid')

print('total_passport:', total_passport, 'valid_passport_count: ', valid_passport_count)
