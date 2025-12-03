from ChainHash import ChainHash
from StringHash import StringHash

BASE_SIZE = 5
baseWords = "maple", "spruce", "oak", "cedar", "cherry"

ADV_SIZE = 10
advWords = "dog", "cat", "ape", "cow", "frog", "fish", "goat", "bear", "deer", "elk"


def main():
  #uncomment functions to run tests

  #print("\nStringHash tests\n")

  #Basic tests
  #testBaseFind()
  #testBaseRemove()
  #testBaseDisplay()
  #testBaseGrow()

  # Advanced tests
  testAdvFind()
  testAdvRemove()
  #testAdvDisplay()

  # Test thinking problem
  testThink()


def testBaseFind():
  print("Testing base addItem and findItem\n")
  baseFind = StringHash()

  for index in range(BASE_SIZE):
    baseFind.addItem(baseWords[index])

  print("Should find maple and not apple")
  if baseFind.findItem("maple"):
    print("  maple found")
  else:
    print("  maple not found")
  if baseFind.findItem("apple"):
    print("  apple found")
  else:
    print("  apple not found")

  print("\nDone testing base addItem and findItem\n")


def testBaseRemove():
  print("Testing base addItem, findItem, and removeItem\n")
  baseRemove = StringHash()

  for index in range(BASE_SIZE):
    baseRemove.addItem(baseWords[index])

  print("Should find maple and then not find maple")
  if baseRemove.findItem("maple"):
    print("  maple found")
  else:
    print("  maple not found")
  baseRemove.removeItem("maple")
  if baseRemove.findItem("maple"):
    print("  maple found")
  else:
    print("  maple not found")
  print("Should find spruce")
  if baseRemove.findItem("spruce"):
    print("  spruce found")
  else:
    print("  spruce not found")

  print("\nDone testing base addItem, findItem, and removeItem\n")


def testBaseDisplay():
  print("Testing base addItem, findItem, removeItem, and display\n")
  baseList = StringHash()

  for index in range(BASE_SIZE):
    baseList.addItem(baseWords[index])

  baseList.removeItem("maple")
  print(
      "Should be \ncedar \ncherry \n_deleted_ \nspruce \n_empty_ \n_empty_ \n_empty_ \n_empty_ \n_empty_ \n_empty_ \noak"
  )

  print("\nActually is")
  print(baseList.displayTable(), end="")

  print("\nDone testing base addItem, findItem, removeItem, and display\n")


def testBaseGrow():
  print("Testing base growing StringHash\n")
  BASE_EXTRA = 3
  baseExtraWords = "bear", "pony", "cow"

  baseGrow = StringHash()

  for index in range(BASE_SIZE):
    baseGrow.addItem(baseWords[index])

  for index in range(BASE_EXTRA):
    baseGrow.addItem(baseExtraWords[index])

  print("After growing the list should be ")
  print("_empty_ \nbear \noak \n_empty_ \nspruce ", end="")
  print("\n_empty_ \n_empty_ \nmaple \ncow ", end="")
  print("\n_empty_ \n_empty_ \npony \n_empty_ ", end="")
  print("\n_empty_ \n_empty_ \ncherry \n_empty_ ", end="")
  print("\ncedar \n_empty_ \n_empty_ \n_empty_ ", end="")
  print("\n_empty_ \n_empty_ ")

  print("\nAnd actually is ")
  print(baseGrow.displayTable())

  print("Now testing find and remove after growing")
  print("Should find maple and then not find maple")
  if baseGrow.findItem("maple"):
    print(" maple found")
  else:
    print(" maple not found")
  baseGrow.removeItem("maple")
  if baseGrow.findItem("maple"):
    print(" maple found")
  else:
    print(" maple not found")
  print("Should find spruce")
  if baseGrow.findItem("spruce"):
    print(" spruce found")
  else:
    print(" spruce not found")

  print("\nDone testing base growing StringHash\n")


def testAdvFind():
  print("Testing advanced addItem and findItem\n")
  advFind = ChainHash()

  for index in range(ADV_SIZE):
    advFind.addItem(advWords[index])

  print("Should find goat and not horse")
  if advFind.findItem("goat"):
    print("  goat found")
  else:
    print("  goat not found")
  if advFind.findItem("horse"):
    print("  horse found")
  else:
    print("  horse not found")

  print("\nDone testing advanced addItem and findItem\n")


def testAdvRemove():
  print("Testing advanced addItem, findItem, and removeItem\n")
  advRemove = ChainHash()

  for index in range(ADV_SIZE):
    advRemove.addItem(advWords[index])

  print("Should find goat and then not find goat")
  if advRemove.findItem("goat"):
    print("  goat found")
  else:
    print("  goat not found")

  advRemove.removeItem("goat")

  if advRemove.findItem("goat"):
    print("  goat found")
  else:
    print("  goat not found")

  print("\nDone testing advanced addItem, findItem, and removeItem\n")


def testAdvDisplay():
  print("Testing advanced addItem, findItem, removeItem, and display\n")
  advList = ChainHash()

  for index in range(ADV_SIZE):
    advList.addItem(advWords[index])

  advList.removeItem("goat")
  print("Should be: \n_empty_ \nfrog deer \ncow fish \n" +
        "_empty_\ndog\nbear\ncat ape elk")

  print("\nAnd is ")
  print(advList.displayTable())

  print("Done testing advanced addItem, findItem, removeItem, and display\n")


def testThink():
  print("Testing thinking problem (growing ChainHash)\n")
  ADV_EXTRA = 6
  advExtraWords = "apple", "pine", "fir", "oak", "maple", "fig"

  advGrow = ChainHash()

  for index in range(ADV_SIZE):
    advGrow.addItem(advWords[index])

  for index in range(ADV_EXTRA):
    advGrow.addItem(advExtraWords[index])

  print("\nAfter growing the list should have 17 rows and ")
  print("include \nfrog \n_empty_ \n_empty_ \n_empty_ ", end="")
  print("\n_empty_ \nfish fir dog pine", end="")
  print("\n_empty_ \nape \ncow \noak ", end="")
  print("\n_empty_ \ndeer fig \nelk \nbear \n_empty_ ", end="")
  print("\napple cat \ngoat maple ")
  print("\nAnd is ")
  print(advGrow.displayTable(), end="")

  print("\nDone testing thinking problem\n")


if __name__ == "__main__":
  main()
