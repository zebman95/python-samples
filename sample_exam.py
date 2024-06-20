print("*** 1st ***")
s = 'Oct'
s = s + '31'
print(type(s[4]))
print("*** 1st ***")


print("*** 2nd ***")
s = 'stars'
print(s[1:3])
print(s[-2] + s[2] + s[1])
print(s[3:0:-1])
print(s[-2:-5:1])
print(s[::-1])
print("*** 2nd ***")

print("*** 3rd ***")
i = 4
while i < 20:
    print(i)
    i = i + 5
print("*** 3rd ***")

print("*** 4th ***")
print([1,2,3,4,5] in len('hello'))
