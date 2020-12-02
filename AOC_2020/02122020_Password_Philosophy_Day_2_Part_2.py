with open('input.txt', 'r') as reader:
    valid_passwords_count = 0
    for password_policy_password in reader:
        password_policy, password = password_policy_password.split(': ')
        l_h_policy, letter = password_policy.split(' ')
        l, h = [int(i) for i in l_h_policy.split('-')]
        letter_count = 0
        for i in range(len(password)):
            if password[i] == letter and i+1 in (l, h):
                letter_count = letter_count + 1
        if letter_count == 1:
            valid_passwords_count = valid_passwords_count + 1
            print(l, h, letter, password)

    print(valid_passwords_count)
