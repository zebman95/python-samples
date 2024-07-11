# recursive function that crawls through the sewer system.
#  captures the sinks (alphabets) along the way and keeps track of locations visted
def probing(x, y, sewer, sinks, visited=""):

   # check that coordinates are within the bounds of the sewer space
   if((x >= 0 and x <= maxX) and (y >= 0 and y <= maxY)):
      # check we can move to the right without falling out of the sewer
      if(x+1 <= maxX):
         # track the coordinate visited
         nextCoordPair = "("+str(x+1)+","+str(y)+")"
         # if a sink is detected, log it
         if(sewer[maxY-y][x].isalpha() and sewer[maxY-y][x] not in sinks):
            sinks += sewer[maxY-y][x]
         # determine if location to the right is a valid pipe outlet and compatible with current pipe
         # also check that it's not a visited coordinate (prevent infinite recursion loops)
         # if conditions are acceptable, move right and log it as being visited
         if((sewer[maxY-y][x+1] == '═' or sewer[maxY-y][x+1] == '╗' or
            sewer[maxY-y][x+1] == '╝' or sewer[maxY-y][x+1] == '╣' or
            sewer[maxY-y][x+1] == "╦" or sewer[maxY-y][x+1] == '╩' or
            sewer[maxY-y][x+1].isalpha()) and nextCoordPair not in visited and
            (sewer[maxY-y][x] != '╝' and sewer[maxY-y][x] != '╗' and sewer[maxY-y][x] != '╣' and sewer[maxY-y][x] != '║')):
            visited += nextCoordPair
            sinks = probing(x+1,y,sewer, sinks,visited)
         
      # check we can move up without falling out of the sewer
      if((maxY - (y+1)) >= 0):
         nextCoordPair = "("+str(x)+","+str(y+1)+")"
         # if a sink is detected, log it
         if(sewer[maxY-y][x].isalpha() and sewer[maxY-y][x] not in sinks):
            sinks += sewer[maxY-y][x]
         # determine if location above is a valid pipe outlet and compatible with current pipe
         # also check that it's not a visited coordinate (prevent infinite recursion loops)
         # if conditions are acceptable, move up and log it as being visited
         if((sewer[maxY-(y+1)][x] == '║' or sewer[maxY-(y+1)][x] == '╔' or
            sewer[maxY-(y+1)][x] == '╗' or sewer[maxY-(y+1)][x] == '╣' or
            sewer[maxY-(y+1)][x] == '╦' or sewer[maxY-(y+1)][x] == '╠' or
            sewer[maxY-(y+1)][x].isalpha()) and nextCoordPair not in visited and
            (sewer[maxY-y][x] != '╔' and sewer[maxY-y][x] != '╗' and sewer[maxY-y][x] != '═' and sewer[maxY-y][x] != '╦')):
            visited += nextCoordPair
            sinks = probing(x,y+1,sewer,sinks,visited)

      # check we can move to the left without falling out of the sewer
      if(x-1 >= 0):
         nextCoordPair = "("+str(x-1)+","+str(y)+")"
         # if a sink is detected, log it
         if(sewer[maxY-y][x].isalpha() and sewer[maxY-y][x] not in sinks):
            sinks += sewer[maxY-y][x]
         # determine if location to the left is a valid pipe outlet and compatible with current pipe
         # also check that it's not a visited coordinate (prevent infinite recursion loops)
         # if conditions are acceptable, move up and log it as being visited
         if((sewer[maxY-y][x-1] == '═' or sewer[maxY-y][x-1] == '╔' or
            sewer[maxY-y][x-1] == '╚' or sewer[maxY-y][x-1] == '╠' or
            sewer[maxY-y][x-1] == '╦' or sewer[maxY-y][x-1] == '╩' or
            sewer[maxY-y][x-1].isalpha()) and nextCoordPair not in visited and
            (sewer[maxY-y][x] != '║' and sewer[maxY-y][x] != '╔' and sewer[maxY-y][x] != '╚' and sewer[maxY-y][x] != '╠')):
            visited += nextCoordPair
            sinks = probing(x-1,y,sewer,sinks,visited)
      
      # check we can move down without falling out of the sewer
      if(maxY-(y-1) <= maxY):
         nextCoordPair = "("+str(x)+","+str(y-1)+")"
         # if a sink is detected, log it
         if(sewer[maxY-y][x].isalpha() and sewer[maxY-y][x] not in sinks):
            sinks += sewer[maxY-y][x]
         # determine if location below is a valid pipe outlet and compatible with current pipe
         # also check that it's not a visited coordinate (prevent infinite recursion loops)
         # if conditions are acceptable, move up and log it as being visited
         if((sewer[maxY-(y-1)][x] == '║' or sewer[maxY-(y-1)][x] == '╚' or
            sewer[maxY-(y-1)][x] == '╝' or sewer[maxY-(y-1)][x] == '╣' or
            sewer[maxY-(y-1)][x] == '╩' or sewer[maxY-(y-1)][x] == '╠' or
            sewer[maxY-(y-1)][x].isalpha()) and nextCoordPair not in visited and
            (sewer[maxY-y][x] != '╝' and sewer[maxY-y][x] != '╚' and sewer[maxY-y][x] != '╩' and sewer[maxY-y][x] != '═')):
            visited += nextCoordPair
            sinks = probing(x,y-1,sewer,sinks,visited)
         
   return sinks

# primary method used in finding all the sinks and sorting them in alphabetical order
def sinkFinder(filepath):
   # first find the full limits of the 2D space
   file = open(filepath, "r")
   filecontent = file.readlines()
   global maxX
   global maxY
   maxX = -1
   maxY = -1
   for line in filecontent:
      xcoord = int(line.split(" ")[1])
      ycoord = int(line.split(" ")[2])
      if(xcoord > maxX):
         maxX = xcoord
      if(ycoord > maxY):
         maxY = ycoord

    # initialize the full 2D space initialize " " as space holder
   sewer = [["-" for x in range(maxX+1)] for y in range(maxY+1)]

   # revisit the file for processing
   file.close()
   file = open(filepath, "r")
   filecontent = file.readlines()
   # store the pipes and sinks in the coordinates specified
   # identify where the source begins
   sourceXcoord = -1
   sourceYcoord = -1
   sourceLine = ""

   for line in filecontent:
      xcoord = int(line.split(" ")[1])
      ycoord = int(line.split(" ")[2])
      sewer[maxY-ycoord][xcoord] = line.split(" ")[0]
      if(line.split(" ")[0] == "*"):
         sourceLine = line
         sourceXcoord = xcoord
         sourceYcoord = ycoord

   # begin the journey from the source and traverse through the pipes looking for accessible sinks
   # return a sorted string of the sinks found
   sinks = ""
   return "".join(sorted(probing(sourceXcoord, sourceYcoord, sewer, sinks))).upper()

# print the sewer system (used for debugging purposes)
#def printSewer(sewer):
#   for x in sewer:
#     for y in x:
#       print(y,end="")
#      print()


print("sinks result: "+sinkFinder("long.txt"))