# Strings in Python:

word = "Python"
word2 = "Programming"

print(word)
print(word2)

print(len(word))
print(len(word2))

conStr = word + " " + word2

print(conStr)

print(word[2])

for letter in word:
    print(letter)

# String Slicing:
str1 = "Python"
print(str1[2:4])

str2 = "I study from Apna College"
print(str2[13:25])
print(str2[13:])
print(str2[13:len(str2)])
print(str2[:])

str3 = "Python"
print(str3[-4:-2])
