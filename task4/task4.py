nums = []
with open("test.txt") as file:
    for line in file:
        line=int(line)
        nums.append(line)
arifmet = round(sum(nums) / len(nums))
count = 0
for id, i in enumerate(nums):
    while i != arifmet:
        if i <arifmet:
            i += 1
            count += 1
        elif i > arifmet:
             i -= 1
             count += 1
        else:
            nums[id] = i
print(count)