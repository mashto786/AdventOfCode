import os
import re

pattern = r'^(?P<min_val>\d+)-(?P<max_val>\d+) (?P<char_val>.): (?P<password>\S+)'
compiled_pattern = re.compile(pattern)

with open(os.path.join('Day2', 'input.txt'), 'r') as fh:
    rowData = fh.readlines()

def check_group_1(re_result):
    password = re_result.group('password')
    min_val = int(re_result.group('min_val'))
    max_val = int(re_result.group('max_val'))
    char_val = re_result.group('char_val')
    if min_val <= password.count(char_val) <= max_val:
        return True

def check_group_2(re_result):
    password = re_result.group('password')
    min_val = int(re_result.group('min_val'))
    max_val = int(re_result.group('max_val'))
    char_val = re_result.group('char_val')
    if (password[min_val - 1] == char_val) != (password[max_val - 1] == char_val):
        return True

row_data = [compiled_pattern.match(row) for row in rowData]
q1_answer = [row for row in row_data if check_group_1(row)]
q2_answer = [row for row in row_data if check_group_2(row)]
print(len(q1_answer))
print(len(q2_answer))





