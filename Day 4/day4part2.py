# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

import os, string, sys

passports = [{}]
dict_index = 0
last_line_blank = False
passport_count = 0

with open(os.path.join(sys.path[0], "day4input.txt")) as file:
    for line in file.read().splitlines():   
        if (line != ''):
            if last_line_blank == True:
                dict_index += 1
                passports.append({})
                last_line_blank = False
            fields = line.split(' ')
            for field in fields:
                passports[dict_index][field.split(':')[0]] = field.split(':')[1]
        else:
            last_line_blank = True

for passport in passports:
    fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    field_check = []
    for i in passport:
        if i == 'byr':
            if len(passport[i]) == 4 and int(passport[i]) >= 1920 and int(passport[i]) <= 2002:
                field_check.append(i)
        elif i == 'iyr':
            if len(passport[i]) == 4 and int(passport[i]) >= 2010 and int(passport[i]) <= 2020:
                field_check.append(i)
        elif i == 'eyr':
            if len(passport[i]) == 4 and int(passport[i]) >= 2020 and int(passport[i]) <= 2030:
                field_check.append(i)
        elif i == 'hgt':
            if passport[i][-2:] == 'cm':
                if int(passport[i].strip('cm')) >= 150 and int(passport[i].strip('cm')) <= 193:
                    field_check.append(i)
            elif passport[i][-2:] == 'in':
                if int(passport[i].strip('in')) >= 59 and int(passport[i].strip('in')) <= 76:
                    field_check.append(i)
        elif i == 'hcl':
            if passport[i][0] == '#':
                hex_check = True
                for char in passport[i].strip('#'):
                    if char not in string.hexdigits:
                        hex_check = False
                        break
                if hex_check == True:
                    field_check.append(i)
        elif i == 'ecl':
            if passport[i] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                field_check.append(i)
        elif i == 'pid':
            if len(passport[i]) == 9 and isinstance(int(passport[i]), int):
                field_check.append(i)
    field_check.sort()
    if fields == field_check:
        passport_count += 1

print(passport_count)

