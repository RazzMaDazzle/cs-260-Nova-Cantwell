# Python Driver for CS260 S21 Lab 1 ArrayInt
# Transpiled from Jim Bailey's C++ Driver with modifications by Tina Majchrzak

from ArrayInt import ArrayInt


def main():
  # uncomment functions to run specific tests

  testConstructor()
  testAppend()
  testMakeRoom()
  testFind()
  testFindLargest()

  testInsertRemove()
  testMix()

  testThink()


def readInVals(skip_lines):
    try:
        with open('input', 'r') as file:
            for _ in range(skip_lines):
                file.readline()
            return [int(x) for x in file.readline().strip().split()]
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)


def testConstructor():
  DEFAULT = 10
  OVERLOAD = 15

  print("TESTING default and overloaded constructors and getSize.\n")

  defaultSize = ArrayInt()
  defineSize = ArrayInt(OVERLOAD)

  print("Default size should be " + str(DEFAULT) + " and is " +
        str(defaultSize.getSize()))
  print("Overload size should be " + str(OVERLOAD) + " and is " +
        str(defineSize.getSize()))
  print("\nDone with constructor test\n\n")


def testAppend():
  print("TESTING append, getLast, and deleteLast\n")

  appends = ArrayInt()
  NUM_APPENDS = 5
  appendVals = readInVals(0)
  appendVals = readInVals(0)

  for i in range(NUM_APPENDS):
    appends.append(appendVals[i])

  print("After APPEND array should be: ", end="")
  for i in range(NUM_APPENDS-1, -1, -1):
    print(appendVals[i], end=" ")
  print("\n             array really is: ", end="")
  try:
    for i in range(NUM_APPENDS - 1):
      print(appends.getLast(), end=" ")
      appends.deleteLast()

    print(appends.getLast())
    appends.deleteLast()
  except:
    print("Problem with appending and deleting")

  print("Trying getLast on empty array, should throw exception")
  try:
    print(appends.getLast())
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")

  print("Trying to delete from empty array, should throw exception")
  try:
    appends.deleteLast()
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")

  print("\n")


def testMakeRoom():
  START = 7
  UPDATE = 12
  roomVals = readInVals(1)
  print("TESTING resize, auto expansion on appends, and listElements\n")

  room = ArrayInt(START)
  print("Starting size should be " + str(START) + " and is " +
        str(room.getSize()))
  room.resize(UPDATE)
  print("After resize, size should be " + str(UPDATE) + " and is " +
        str(room.getSize()))

  print("\nNow going to fill array and see if it expands")
  for i in range(UPDATE):
    room.append(roomVals[i])

  print("Filled with 12 values, no problem")
  print("Size should still be " + str(UPDATE) + " and is " +
        str(room.getSize()))
  print("\nAdding one more")
  room.append(88)
  print("Size should now be " + str(2 * UPDATE) + " and is " +
        str(room.getSize()))

  print("\nAfter MAKE ROOM should be:", end="")
  for i in range(UPDATE):
    print(f" {roomVals[i]}", end="")
  print(" 88")
  print(f"                really is:{room.listElements()}")


def testFind():
  FIND_COUNT = 10
  findRemVals = readInVals(2)
  print("\n\nTESTING find and removeVal", end="\n\n")

  findRemove = ArrayInt()
  for i in range(FIND_COUNT):
    findRemove.append(findRemVals[i])
  lastEl = findRemVals[FIND_COUNT-1];

  print("Array contains " + findRemove.listElements())

  print("Testing find on 4 and 7.")
  if findRemove.find(4):
    print("  4 was found")
  else:
    print("  4 was not found")

  if findRemove.find(7):
    print("  7 was found")
  else:
    print("  7 was not found")

  print(
      "Testing removeVal on 4 and 7."
  )
  if findRemove.removeVal(4):
    print("  4 was removed")
  else:
    print("  4 was not removed")

  if findRemove.removeVal(7):
    print("  7 was removed")
  else:
    print("  7 was not removed")

  print("After REMOVE expected:", end="")
  for i in range(FIND_COUNT):
    if findRemVals[i] != 4 and findRemVals[i] != 7:
        print(f" {findRemVals[i]}", end="")
  print("\n             actually:" + findRemove.listElements())

  print(f"\nUsing removeVal on final element, {lastEl}")
  if findRemove.removeVal(lastEl):
    print(f"{lastEl} was removed")
  else:
    print(f"{lastEl} was not removed")
  print(f"Using find to look for {lastEl} after removal.  Should not find")
  if findRemove.find(lastEl):
    print(f"{lastEl} was found")
  else:
    print(f"{lastEl} was not found")


def testFindLargest():
  LARGE_COUNT = 8
  print("\n\nTESTING findLargest and removeLargest ", end="\n\n")

  findLarge = ArrayInt()
  large = [3, 11, 19, 7, 5, 2, 13, 23]
  for i in range(LARGE_COUNT):
    findLarge.append(large[i])

  print("Array contains " + findLarge.listElements())

  print("Largest should be 23 and is " + str(findLarge.findLargest()))

  findLarge.removeLargest()
  findLarge.removeLargest()
  print("After removing two largest should be: 3 11 7 5 2 13")
  print("                         actually is:" + findLarge.listElements())

  print("Emptying array")
  for i in range(LARGE_COUNT - 2):
    findLarge.deleteLast()

  print("\nNow testing findLargest on empty array")
  try:
    findLarge.findLargest()
    print("Should have thrown an exception")
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")

  print("Now testing removeLargest on empty array")
  try:
    findLarge.removeLargest()
    print("Should have thrown an exception")
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")


def testInsertRemove():
  BEGIN = 10
  print("\n\nTESTING insertAt and removeAt \n")

  insRemVals = readInVals(3)
  insertRemove = ArrayInt()
  for i in range(BEGIN):
    insertRemove.append(insRemVals[i])

  print("Array starting with: " + insertRemove.listElements(), end="")
  insertRemove.listElements()
  print("\nSize should be " + str(BEGIN) + " and is " + str(insertRemove.getSize()))

  print("\nNow inserting 5 at index 2")
  insertRemove.insertAt(2, 5)
  print("Size should be " + str(2 * BEGIN) + " and is " + str(insertRemove.getSize()))        
  print("  After INSERT AT expected:", end="")
  for i in range(2):
    print(f" {insRemVals[i]}", end="")
  print(" 5", end="")
  for i in range(2, BEGIN):
    print(f" {insRemVals[i]}", end="")
  print(f"\n  After INSERT AT actually:{insertRemove.listElements()}")

  print("\nTrying to remove values at indices: 8 2 0", end="")
  print("\n                           Removed: ", end="")
  print(str(insertRemove.removeAt(8)), end=" ")
  print(str(insertRemove.removeAt(2)), end=" ")
  print(str(insertRemove.removeAt(0)))

  print("  After REMOVE AT expected:", end="")
  for i in range(1, 7):
    print(f" {insRemVals[i]}", end="")
  for i in range(8, BEGIN):
    print(f" {insRemVals[i]}", end="")

#  " 2, 4, 5, 6, 9, 10, 13, 14, 16, 18 ")
  print("\n  After REMOVE AT actually:" + insertRemove.listElements())

  print("\nNow testing illegal inserts and removes ")
  print("Testing invalid insertAt at index larger than array size")
  try:
    insertRemove.insertAt(BEGIN * 3, -1)
    print("Should have thrown an exception inserting at " + str(BEGIN * 3) +
          "\n")
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")

  print("Testing invalid insertAt at negative index")
  try:
    insertRemove.insertAt(-1, 500)
    print("Should have thrown an exception\n")
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")

  print("\nEmptying the array, expecting:", end="")
  for i in range(BEGIN - 1, 7, -1):
    print(f" {insRemVals[i]}", end="")
  for i in range(6, 0, -1):
    print(f" {insRemVals[i]}", end="")

  print("\n  Actually removed the values:", end="")
  for i in range(BEGIN-2):
    print(f" {insertRemove.getLast()}", end="")
    insertRemove.deleteLast()

  print("\n\nNow testing removeAt on empty array")
  try:
    insertRemove.removeAt(0)
    print("Should have thrown an exception\n")
  except IndexError as ex:
    print(f"Caught IndexError with message: {str(ex)}")
  except Exception as ex:
    print(f"Caught something weird: {str(ex)}")


def testMix():
  print("\n\nTESTING a mixture of appends, insertAts, and removeAts")

  mixed = ArrayInt()

  mixed.append(2);
  mixed.append(4);
  mixed.append(6);
  mixed.deleteLast();
  mixed.append(50000);
  mixed.insertAt(0, 16);
  mixed.append(32);
  mixed.insertAt(2, 19);
  mixed.append(256);
  mixed.removeLargest();
  mixed.append(64);
  mixed.removeAt(4);

  print("Displaying the results")
  print("  After MIX expected: 16 2 19 4 256 64")
  print("  After MIX actually:" + mixed.listElements())

  print("Done testing mixed\n\n")


def testThink():
  NUM_THINK = 10
  print("TESTING the thinking problem")

  think = ArrayInt()
  thinkVals = readInVals(4)

  thinkVals.sort(reverse=True)
  print("  After THINK expected:", end="")
  for i in range(NUM_THINK):
    print(f" {thinkVals[i]}", end="")

  #99, 95, 22, 18, 7, 4, 3, 1, 0, -1")

  think.solveThink(thinkVals, len(thinkVals))
  print(f"\n  After THINK actually:{think.listElements()}")
  print("Done with thinking test\n")


if __name__ == '__main__':
  main()
