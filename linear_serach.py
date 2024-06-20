
arr = [2,8,5,3,9,4,1, 11, 2, 5, 7, 8, 9, 7, 7, 6, 14]

print(arr)

num = input("enter the number of instances to count: ")
count = []
index = 0
for x in arr:
   if(int(num) == x):
      count.append(index)
   index += 1

print("indexes of "+num+": "+str(count))

