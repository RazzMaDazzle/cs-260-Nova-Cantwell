from ParseTree import ParseTree

display = True


def main():
  # uncomment tests to run
  testBase()
  testAdv()
  #testThink()


def testBase():
  print("Testing Base Parse Tree\n")

  expression1 = "AB+CD-*"
  expression2 = "AB-C+DE*/"

  ptree1 = ParseTree(expression1)
  print(f"Input is {expression1}")
  print("In Order should be (((A)+(B))*((C)-(D)))")
  print("                or ((A+B)*(C-D))")
  print("                or (A+B)*(C-D)")
  print(f"            and is {ptree1.inOrder()}\n")

  print("Post Order should be AB+CD-*")
  print(f"              and is {ptree1.postOrder()}\n")

  print("Pre Order should be *+AB-CD")
  print(f"             and is {ptree1.preOrder()}\n")

  if display:
    print(ptree1.display())

  print()
  ptree2 = ParseTree(expression2)
  print(f"Input is {expression2}")
  print("In Order output should be ((((A)-(B))+(C))/((D)*(E)))")
  print("                       or (((A-B)+C)/(D*E))")
  print("                       or ((A-B)+C)/(D*E)")
  print("                       or (A-B+C)/(D*E)")
  print(f"                   and is {ptree2.inOrder()}\n")

  print("Post Order should be AB-C+DE*/")
  print(f"              and is {ptree2.postOrder()}\n")

  print("Pre Order should be /+-ABC*DE")
  print(f"             and is {ptree2.preOrder()}\n")

  if display:
    print(ptree2.display())

  print("Done with Parse Tree test\n")


def testAdv():
  print("Testing Advanced Parse Tree\n")

  expression3 = "(A+B)*C+D"
  expression4 = "A/(B+C)*(D+E)"
  expression5 = "A/((B+C)*(D+E))"

  ptree3 = ParseTree("")

  ptree3.parseInOrder(expression3)
  print(f"Input is {expression3}")
  print("In Order should be ((((A)+(B))*(C))+(D)) \n"
        "                or (((A+B)*C)+D) \n"
        "                or ((A+B)*C)+D \n"
        "                or (A+B)*C+D \n"
        f"            and is {ptree3.inOrder()}\n")
  print(f"Post Order should be AB+C*D+ \n"
        f"              and is {ptree3.postOrder()}\n")
  print(f"Pre Order should be +*+ABCD \n"
        f"             and is {ptree3.preOrder()}\n")

  if display:
    print(ptree3.display())

  print("")
  ptree3.parseInOrder(expression4)
  print(f"Input is {expression4}")
  print("In Order should be (((A)/((B)+(C)))*((D)+(E))) \n"
        "                or ((A/(B+C))*(D+E)) \n"
        "                or (A/(B+C))*(D+E) \n"
        "                or A/(B+C)*(D+E) \n"
        f"            and is {ptree3.inOrder()}\n")
  print(f"Post Order should be ABC+/DE+* \n"
        f"              and is {ptree3.postOrder()}\n")
  print(f"Pre Order should be */A+BC+DE \n"
        f"             and is {ptree3.preOrder()}\n")

  if display:
    print(ptree3.display())

  print("")
  ptree3.parseInOrder(expression5)
  print(f"Input is {expression5}")
  print("In Order should be ((A)/(((B)+(C))*((D)+(E)))) \n"
        "                or (A/((B+C)*(D+E))) \n"
        "                or A/((B+C)*(D+E)) \n"
        f"            and is {ptree3.inOrder()}\n")
  print(f"Post Order should be ABC+DE+*/ \n"
        f"              and is {ptree3.postOrder()}\n")
  print(f"Pre Order should be /A*+BC+DE \n"
        f"             and is {ptree3.preOrder()}\n")

  if display:
    print(ptree3.display())

  print("Done with Advanced Parse Tree test\n\n")


def testThink():
  print("Testing Thinking Problem\n")

  expression6 = "(((A+B)*C)+(D/(F*G)))"
  expression7 = "((A*B)-(C+D))"
  expression8 = "(A-(B-C))"
  
  ptree4 = ParseTree("")

  ptree4.parseInOrder(expression6)
  print(f"Input is {expression6}")
  print("In Order should be (A+B)*C+D/(F*G)")
  print(f"            and is {ptree4.inOrder()}\n")
  print("Post Order should be AB+C*DFG*/+")
  print(f"              and is {ptree4.postOrder()}\n")
  print("Pre Order should be +*+ABC/D*FG")
  print(f"             and is {ptree4.preOrder()}\n")

  if display:
    print(ptree4.display())

  print("")
  ptree4.parseInOrder(expression7)
  print(f"Input is {expression7}")
  print("In Order should be A*B-(C+D)")
  print(f"            and is {ptree4.inOrder()}\n")
  print("Post Order should be AB*CD+-")
  print(f"              and is {ptree4.postOrder()}\n")
  print("Pre Order should be -*AB+CD")
  print(f"             and is {ptree4.preOrder()}\n")

  if display:
    print(ptree4.display())

  print("")
  ptree4.parseInOrder(expression8)
  print(f"Input is {expression8}")
  print("In Order should be A-(B-C)")
  print(f"            and is {ptree4.inOrder()}\n")
  print("Post Order should be ABC--")
  print(f"              and is {ptree4.postOrder()}\n")
  print("Pre Order should be -A-BC")
  print(f"             and is {ptree4.preOrder()}\n")

  if display:
    print(ptree4.display())

  print("Done with Testing Thinking Problem\n")


if __name__ == '__main__':
  main()
