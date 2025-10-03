#
#  ArrayInt.py
#  ArrayInt
#
#  C++ version
#  Created by Jim Bailey on 3/31/2021 with modifications by Tina Majchrzak.
#  This work by Jim Bailey is licensed under a Creative
#  Commons Attribution 4.0 International License.
#
#  Transpiled with permission by Katie Strauss on 4/12/2021.
#  Original license restrictions apply

import array


class ArrayInt:

  # constructor, set up the array
  def __init__(self, size=10):
    if size < 1:
      size = 10
    self.size = size
    self.lastIndex = 0
    self.theArray = array.array('i', [0] * size)


  def getSize(self):
    return self.size


  # add value at next location
  # call resize to resize array if full
  def append(self, value):
    if self.lastIndex < self.size:
        self.theArray[self.lastIndex] = value
        self.lastIndex += 1
    elif self.lastIndex >= self.size:   
        self.resize(self.size * 2)
        self.append(value)
    return


  # get value at last location
  # throw exception if empty
  def getLast(self):
    if (self.lastIndex - 1) < 0:
        raise IndexError("Array is empty!")
    else:
        return self.theArray[self.lastIndex - 1]
    return

  # remove value at last location
  # does nothing if empty
  def deleteLast(self):
    if self.lastIndex > 0:
        self.lastIndex = self.lastIndex - 1
    else:
        raise IndexError("Array is empty!")
    return


  # create new array of newSize and copy to it
  def resize(self, newSize):
    tmp = 0
    if self.lastIndex > 0:
        tmp = self.theArray
    self.__init__(newSize)
    if tmp:
        for i in range(len(tmp)):
            self.append(tmp[i])
    return


  # list the elements from 0 to self.lastIndex
  def listElements(self):
    if self.lastIndex < 1:
        return "Array is empty!"
    else:
        rtrnstr = ""
        for i in range(0, self.lastIndex):
            rtrnstr += " " + str(self.theArray[i])
        return rtrnstr
            


  # find a value if present
  def find(self, value):
    for i in range(self.lastIndex):
        if self.theArray[i] == value:
            return True
    else:
        return False


  # remove a value if found
  def removeVal(self, value):
    for i in range(0, self.lastIndex):
        if self.theArray[i] == value:
            for x in range(i + 1, self.lastIndex):
              self.theArray[x - 1] = self.theArray[x] 
            self.lastIndex = self.lastIndex - 1
            self.removeVal(value)
            return True
    return False


  # find and return the largest value
  def findLargest(self):
    if self.lastIndex < 1:
        raise IndexError("Attempt to read from empty array.")
    else:
        max = 0
        for i in range(self.lastIndex):
            if self.theArray[i] > max:
                max = self.theArray[i]
        return max

  # remove largest value
  def removeLargest(self):
    if self.lastIndex < 1:
        raise IndexError("Attempt to remove from empty array.")
    tmp = self.findLargest()
    self.removeVal(tmp)
    return


  # insert into array at specified location
  def insertAt(self, index, value):
    if not (-1) < index < self.lastIndex + 2:
         raise IndexError("Attempt to write at invalid location.")
    else:
        if self.lastIndex + 1 > self.size:
            self.resize(self.size * 2)
        self.lastIndex = self.lastIndex + 1
        for i in range(self.lastIndex, index - 1, -1):
            if not i == index:
                self.theArray[i] = self.theArray[i - 1]
            else:
                self.theArray[i] = value
    return


  # remove an item and compress the array
  def removeAt(self, index):
    if not (-1) < index < self.lastIndex + 1:
         raise IndexError("Attempt to remove at invalid location.")
    elif self.lastIndex == 0:
         raise IndexError("Attempt to remove from empty array.")
    else:
        tmp = self.theArray[index]
        self.removeVal(self.theArray[index])
    return tmp


  # use append,findLargest,and remove to arrange values in descending order
  def solveThink(self, values, numValues):
    self.__init__(numValues)
    for i in range(len(values)):
        self.append(values[i])
    tmp = self.findLargest()
    return tmp

