import re

# input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open(r"day3_input.txt", 'r') as fp:
    input_string = fp.read()
fp.close()

# regular expression matching
pattern = r"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
matches = re.findall(pattern, input_string)

# print(matches)

# multiplication
sum = 0
for pair in matches:
    sum = sum + int(pair[0]) * int(pair[1])

print(sum)