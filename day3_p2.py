import re

# input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open(r"day3_input.txt", 'r') as fp:
    input_string = fp.read()
fp.close()


# regular expression matching
pattern = r"do\(\)|don't\(\)|mul\(\d*,\d*\)"
matches = re.findall(pattern, input_string)

print(matches)

multiplier = 1 # 1 for do(); 0 for don't()
sum = 0 

for match in matches:
    # print(match)
    if match == "don't()":
        multiplier = 0
    elif match == "do()":
        multiplier = 1
    else:
        pair = re.findall(r"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)", match)
        sum = sum + int(pair[0][0]) * int(pair[0][1]) * multiplier


print(sum)