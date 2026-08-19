# Tuples in Python: Immutable

nums = (1,2,3,4,5)
num2 = (1,)

print(nums)
print(type(nums))
print(len(nums))
print(nums[2])

print(num2)
print(type(num2))
print(len(num2))
print(num2[0])

print(nums[0:3])

for num in nums:
    print(num)

sum_ = 0
for num in nums:
    sum_ = sum_ + num
print(sum)

# Tuple Methods:
newNums = (1, 2, 2, 3, 2, 4)

print(nums.index(2))
print(newNums.count(2))
