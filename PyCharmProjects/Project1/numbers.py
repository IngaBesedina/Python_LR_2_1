nums = [0]*4
for i in range(4):
    print("Введите", i+1, "-ое число:")

    nums[i] = int(input())
print('%.2f' % ((nums[0]+nums[1])/(nums[2]+nums[3])))
