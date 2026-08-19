# Lists in Python: Mutable sequence of values.

marks = [99, 89, 100, 65, 92]

print(marks)
print(type(marks))
print(len(marks))

print(marks[1])

marks[1] = 100
print(marks)

print(marks[1:3])

# List Methods: Functions
nums = [1, 2, 3, 4, 5]
print(nums)

nums.append(6)
print(nums)

nums.insert(1, 7)
print(nums)

nums.remove(1)
print(nums)

nums.sort()
print(nums)

# Loop in lists:
for num in nums:
    print(num)

nums.clear()
print(nums)
