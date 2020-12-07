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
            if field.split(':')[0] in mandatory_fields:
                fields_present_count += 1

print('total_passport:', total_passport, 'valid_passport_count: ', valid_passport_count)
