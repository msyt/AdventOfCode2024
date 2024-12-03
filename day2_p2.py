def is_safe(nums):
    # asc/ dsc
    asc = nums[0] < nums[1]

    # difference
    for i in range(0, len(nums) - 1):
        diff = nums[i] - nums[i+1]
        if asc:
            if diff >= 0 or diff < -3:
                return False
        else:
            if diff <= 0 or diff > 3:
                return False
    return True

def safe(nums, count):
    if count > 1:
        return 0
    if is_safe(nums):
        return 1

    # One modification
    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        if safe(temp, count + 1) == 1:
            return 1
    return 0


sum = 0
with open(r"day2_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
       input = list(map(int, line.split()))
       sum += safe(input, 0)
       
fp.close()

print(sum)