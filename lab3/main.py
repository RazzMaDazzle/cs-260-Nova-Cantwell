from TextClass import TextClass


def main():
  # uncomment tests to run

    #basic tests
  testHead()
  testTail()
  testQueue()
  testDisplay()
  #testFind()
  #testFindRemove()

  # advanced tests
  #testAppend()
  #testFindNext()
  #testRemoveLast()
  #testInsertLast()
  #testMixed()

  # thinking test
  #testThink()



# basic tests
def testHead():
  print("Testing adding and removing from head\n")
  ADD_HEAD = 5
  heads = 'a', 'b', 'c', 'd', 'e'

  head = TextClass()
  print("Adding five letters to head of list")
  for index in range(ADD_HEAD):
    head.addHead(heads[index])

  print(" removing and displaying them")
  print(" expected e d c b a")
  print(" actually", end=" ")
  for index in range(ADD_HEAD):
    print(head.getHead(), end=" ")
    head.removeHead()
  print("\n")

  print("Now reading an extra value ")
  try:
    head.getHead()
    print(" should have thrown an exception")
  except ValueError:
    print("Caught ValueError")
  except:
    print("Caught something unexpected")

  print("Done testing adding and removing from head\n")


def testTail():
  print("Testing adding and removing from tail\n")
  ADD_TAIL = 5
  tails = 'z', 'y', 'x', 'w', 'v'

  tail = TextClass()
  print("Adding five letters to tail of list")
  for index in range(ADD_TAIL):
    tail.addTail(tails[index])

  print(" removing and displaying them")
  print(" expected v w x y z")
  print(" actually", end=" ")
  for index in range(ADD_TAIL):
    print(tail.getTail(), end=" ")
    tail.removeTail()
  print("\n")

  print("Now getting an extra value ")
  try:
    tail.getTail()
    print(" should have thrown an exception")
  except ValueError:
    print("Caught ValueError")
  except:
    print("Caught something unexpected")

  print("Done testing adding and removing from tail\n")


def testQueue():
  print("Testing queue both ways\n")
  FIFO = 5
  headFifo = 'A', 'C', 'E', 'G', 'I'
  tailFifo = 'M', 'N', 'O', 'P', 'Q'

  fifo1 = TextClass()
  print("Adding five letters to tail of list")
  for index in range(FIFO):
    fifo1.addTail(headFifo[index])

  print(" removing from head and displaying them")
  print(" expected A C E G I")
  print(" actually", end=" ")
  for index in range(FIFO):
    print(fifo1.getHead(), end=" ")
    fifo1.removeHead()

  print("\n")

  fifo2 = TextClass()
  print("Adding five letters to head of list")
  for index in range(FIFO):
    fifo2.addHead(tailFifo[index])

  print(" removing from tail and displaying them")
  print(" expected M N O P Q")
  print(" actually", end=" ")
  for index in range(FIFO):
    print(fifo2.getTail(), end=" ")
    fifo2.removeTail()
  print("\n")

  print("Done testing queue both ways\n")


def testDisplay():
  print("Testing display list\n")
  DISPLAY = 6
  displays = 's', 'p', 'r', 'u', 'c', 'e'

  display = TextClass()
  print("Adding six letters to tail of list")
  for index in range(DISPLAY):
    display.addTail(displays[index])

  print(" displaying them head to tail")
  print(" expected s p r u c e")
  print(" actually " + display.displayList() + "\n")

  print("Done testing display list\n")


def testFind():
  print("Testing find\n")
  FIND = 5
  vowels = 'a', 'e', 'i', 'o', 'u'

  findTail = TextClass()
  print("Adding five vowels to tail of a list")
  for index in range(FIND):
    findTail.addTail(vowels[index])

  print(" displaying them")
  print(" expected a e i o u")
  print(" actually " + findTail.displayList())

  if findTail.find('e'):
    print("  e is there")
  else:
    print("  e is not there and should be")
  if findTail.find('x'):
    print("  x is there and should not be")
  else:
    print("  x is not there")
  print("\n")

  findHead = TextClass()
  print("Adding five vowels to head of a list")
  for index in range(FIND):
    findHead.addHead(vowels[index])
  print(" displaying them")
  print(" expected u o i e a")
  print(" actually " + findHead.displayList())

  if findHead.find('a'):
    print("  a is there")
  else:
    print("  a is not there and should be")
  if findHead.find('r'):
    print("  r is there and should not be")
  else:
    print("  r is not there")
  print("\n")

  print("Done testing find\n")


def testFindRemove():
  print("Testing find and remove\n")
  FIND_REM = 5
  digits = '1', '3', '5', '7', '9'

  findRem = TextClass()
  print("Adding five digits to tail of a list")
  for index in range(FIND_REM):
    findRem.addTail(digits[index])

  print(" displaying them")
  print(" expected 1 3 5 7 9")
  print(" actually " + findRem.displayList())

  print("Finding and removing 3, should succeed")
  if findRem.findRemove('3'):
    print("  3 was there")
  else:
    print("  3 was not there and should have been")
  print("Finding and removing 6, should not succeed")
  if findRem.findRemove('6'):
    print("  6 was there and should not have been")
  else:
    print("  6 was not there")
  print(" displaying them after remove")
  print(" expected 1 5 7 9")
  print(" actually " + findRem.displayList(), end="\n\n")

  print("Now testing find/remove head and tail")
  print("Finding and removing 1, should succeed")
  if findRem.findRemove('1'):
    print("  1 was there")
  else:
    print("  1 was not there and should have been")
  print("Finding and removing 9, should succeed")
  if findRem.findRemove('9'):
    print("  9 was there")
  else:
    print("  9 was not there and should have been")
  print(" displaying them after remove")
  print(" expected 5 7")
  print(" actually " + findRem.displayList(), end="\n\n")

  print("Done testing find and remove\n")


# advanced tests
def testAppend():
  print("Testing appending a list\n")
  APPEND1 = 6
  APPEND2 = 7
  counter = 0
  appendVals = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'

  first = TextClass()
  for index in range(APPEND1):
    first.addTail(appendVals[counter])
    counter += 1

  second = TextClass()
  for index in range(APPEND2):
    second.addTail(appendVals[counter])
    counter += 1

  print("First list is " + first.displayList())
  print("Second list is " + second.displayList())

  first.append(second)
  print("First should now be a b c d e f g h i j k l m")
  print(" and it actually is " + first.displayList())

  print("Done appending a list\n")


def testFindNext():
  print("Testing find next\n")
  FIND_NEXT = 5
  nextVals = 'a', 'p', 'p', 'l', 'e'

  nextFind = TextClass()
  for index in range(FIND_NEXT):
    nextFind.addTail(nextVals[index])

  print("List contains " + nextFind.displayList())
  print("Looking for a, e, p, p, k, a")
  if nextFind.findNext('a'):
    print("a was found")
  else:
    print("a was not found")
  if nextFind.findNext('e'):
    print("e was found")
  else:
    print("e was not found")
  if nextFind.findNext('p'):
    print("p was found")
  else:
    print("p was not found")
  if nextFind.findNext('p'):
    print("p was found")
  else:
    print("p was not found")
  if nextFind.findNext('k'):
    print("k was found")
  else:
    print("k was not found")
  if nextFind.findNext('a'):
    print("a was found")
  else:
    print("a was not found")

  print("Done testing find next\n")


def testRemoveLast():
  print("Testing remove last\n")
  REM_LAST = 7
  removeVals = 'b', 'e', 'a', 'r', 'd', 'e', 'd'

  remLast = TextClass()
  for index in range(REM_LAST):
    remLast.addTail(removeVals[index])
  print("List contains " + remLast.displayList())
  print("Looking to remove first d after wrapping")
  if remLast.findNext('d'):
    print("first d was found")
  else:
    print("first d was not found")
  if remLast.findNext('d'):
    print("second d was found")
  else:
    print("second d was not found")
  if remLast.findNext('d'):
    print("first d was again found")
  else:
    print("first d was not found")
  remLast.removeLast()
  print("Displaying after removes")
  print("List should now be b e a r e d")
  print(" and it is " + remLast.displayList(), end="\n\n")

  print("Looking to remove second e")
  if remLast.findNext('e'):
    print("e was found")
  else:
    print("e was not found")
  if remLast.findNext('e'):
    print("e was found")
  else:
    print("e was not found")
  remLast.removeLast()
  print("Doing an extra remove, should do nothing")
  remLast.removeLast()
  print("Displaying after removes")
  print(" expected b e a r d")
  print(" actually " + remLast.displayList(), end="\n\n")

  print("Done testing remove last\n")


def testInsertLast():
  print("Testing insert last\n")
  INSERT_LAST = 4
  insertVals = '1', '3', '7', '9'

  insLast = TextClass()
  for index in range(INSERT_LAST):
    insLast.addTail(insertVals[index])

  print("List contains " + insLast.displayList())
  print("Looking to insert 4, 5, and 6 in sequence")
  print("First finding 7:", end=" ")
  if insLast.findNext('7'):
    print("7 was found")
  else:
    print("7 was not found")
  insLast.insertLast('5')
  insLast.insertLast('6')
  print("Now finding 5:", end=" ")
  if insLast.findNext('5'):
    print("5 was found")
  else:
    print("5 was not found")
  insLast.insertLast('4')
  print(" displaying result, expected 1 3 4 5 6 7 9")
  print(" actually " + insLast.displayList(), end="\n\n")

  print("Done testing insert last\n")


def testMixed():
  print("Testing mixed inserts and deletes\n")
  MIX = 3
  MIXED = 4
  mixLetters = 'c', 'a', 'w'

  mixed = TextClass()
  for index in range(MIX):
    mixed.addTail(mixLetters[index])

  print("List starts with " + mixed.displayList())
  print(" replacing a with o and adding r")
  mixed.findNext('a')
  mixed.insertLast('o')
  mixed.removeLast()
  mixed.findNext('o')
  mixed.insertLast('r')
  print(" caw should now be crow ")
  print(" and it is", end=" ")
  for index in range(MIXED):
    print(mixed.getHead(), end="")
    mixed.removeHead()
  print("\n")

  print("Done testing mixed inserts and deletes\n")


# thinking test
def testThink():
  codeLetters = [
      'I', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e'
  ]
  debugLetters = [
      'I', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'o', ' ', 'd', 'e', 'b', 'u', 'g'
  ]

  codeText = TextClass()
  for letter in codeLetters:
    codeText.addTail(letter)

  debugText = TextClass()
  for letter in debugLetters:
    debugText.addTail(letter)

  codeText.thinkSolve(debugText)

  print(
      "Expected codeList output: \nI   l i k e   t o   c o d e   a n d   d e b u g"
  )
  print(codeText.displayList())

  print("Expected debugList output: \nI   l i k e   t o   d e b u g")
  print(debugText.displayList())

  print("Done testing thinking solution")


if __name__ == "__main__":
  main()
