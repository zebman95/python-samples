list = [1,2,3,4,5,6,7,8,9]

rowCount = 1
for x in list:
   if(rowCount < 3):
     print(x,end=" | ")
     rowCount += 1
   else:
     print(x)
     rowCount = 1
