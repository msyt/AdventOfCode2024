list = []
list1 = []
list2 = []

with open(r"day1_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
       num1, num2 = line.split()
       list1.append(int(num1))
       list2.append(int(num2))
fp.close()

list1.sort()
list2.sort()

for i in range(len(list1)):
    list.append(abs(list1[i]-list2[i]))

print(sum(list))