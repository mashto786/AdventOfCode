import os
import time

## Star 1
star1_start = time.time()
with open(os.path.join('Day1', 'input.txt'), 'r') as fh:
    inputData = fh.read()
input_list = [int(item) for item in inputData.split('\n') if item.isnumeric()]
for item in input_list:
    remainder = 2020 - item
    try:
        result = input_list.index(remainder)
    except ValueError:
        continue
    print("{item} * {remain} = {result}".format(item = item, remain = remainder, result = item * remainder))
    break
print("--- {time} seconds ---".format(time=time.time()- star1_start))

##star 2
star2_start = time.time()
for first_item in input_list:
    remainder_1 = 2020 - first_item
    for second_item in input_list:
        remainder_2 = remainder_1 - second_item
        try:
            result = input_list.index(remainder_2)
        except ValueError:
            continue
        print("{first_item} * {second_item} * {remain2} = {result}".format(
            first_item = first_item, 
            second_item = second_item, 
            remain2 = remainder_2, 
            result = first_item * second_item * remainder_2))
        break
print("--- {time} seconds ---".format(time=time.time()- star2_start))
    