# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

import os, sys

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
        if i in fields:
            field_check.append(i)
    field_check.sort()
    if fields == field_check:
        passport_count += 1

print(passport_count)

