def safe(nums):
    # asc/ dsc
    if nums[0] < nums[1]:
        asc = True
    else: 
        asc = False

    # difference
    for i in range(0, len(nums) - 1):
        diff = nums[i] - nums[i+1]
        if asc:
            if diff >= 0 or diff < -3:
                return 0
        else:
            if diff <= 0 or diff > 3:
                return 0
        
    return 1


sum = 0
with open(r"day2_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
       input = list(map(int, line.split()))
       sum += safe(input)
       
fp.close()

print(sum)