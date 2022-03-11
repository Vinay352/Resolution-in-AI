import os
import sys
from itertools import combinations


def parseFile(s):
    clauses = set()
    predicates = set()
    variables = set()
    constants = set()
    functions = set()

    with open(s) as f:
        clause = 0

        for line in f.readlines():
            if clause == 0:
                if line.startswith("Clauses:"):
                    clause = 1
                elif line.startswith("Predicates:"):
                    temp = line.strip().split(" ")
                    for i in temp[1:]:
                        predicates.add(i.strip().replace("\\", "").replace("{","").replace("}",""))
                elif line.startswith("Functions:"):
                    temp = line.strip().split(" ")
                    for i in temp[1:]:
                        functions.add(i.strip().replace("\\", "").replace("{","").replace("}",""))
                elif line.startswith("Variables:"):
                    temp = line.strip().split(" ")
                    for i in temp[1:]:
                        variables.add(i.strip().replace("\\", "").replace("{","").replace("}",""))
                elif line.startswith("Constants:"):
                    temp = line.strip().split(" ")
                    for i in temp[1:]:
                        constants.add(i.strip().replace("\\", "").replace("{","").replace("}",""))
            elif clause == 1:
                clauses.add(line.strip().replace("\\", "").replace("{","").replace("}",""))

    return clauses, predicates, variables, functions, constants


def call_F(clauses, predicates, variables, functions, constants):
    pass


def canResolve_C(i, j):
    if (i[0] == '!') and (j[0] == '!'):
        return False
    if (i[0] == '!') | (j[0] == '!'):
        return True
    return False


def Resolve_C(set1, set2):
    oneElements = set1.split(" ")
    twoElements = set2.split(" ")

    # print(oneElements)
    # print(twoElements)

    ans = set()
    stop = False
    word = ""

    for i in oneElements:
        temp1 = i.replace("!", "")
        if not stop:
            for j in twoElements:
                if not stop:
                    temp2 = j.replace("!", "")
                    if temp1 == temp2 and canResolve_C(i, j):
                        word = temp1
                        stop = True
                else:
                    break
        else:
            break

    # list1 = list(set1.split(" "))
    # list2 = list(set2.split(" "))
    #
    # list1.extend(list2)
    #
    # print("list1 = ", end = "")
    # print(list1)
    #
    # print("word = " + word)
    #
    # if word != "":
    #     list1.remove(word)
    #     list1.remove("!" + word)
    #
    # print("list1 = ", end="")
    # print(list1)

    ans.update(list(set1.split(" ")))
    ans.update(list(set2.split(" ")))

    if word != "":
        ans.remove(word)
        ans.remove("!" + word)

    # print("After Resolution : " + str(ans))
    # print(ans)

    countWord = countWordFreq(set1, set2, word)
    countNotWord = countWordFreq(set1, set2, "!" + word)

    if countWord > 1:
        ans.add(word)
    if countNotWord > 1:
        ans.add("!" + word)

    correct = ""
    for i in ans:
        correct += i + " "

    # print(correct.strip())

    return correct


def call_C(clauses, predicates, variables, functions, constants):
    new = set()

    # pairOfClauses = list(combinations(clauses, 2))
    # print(pairOfClauses)
    # print(pairOfClauses[0])
    # print(pairOfClauses[0][0])
    # print(pairOfClauses[0][1])
    # print()

    while True:
        pairOfClauses = list(combinations(clauses, 2))
        # print("Clauses Set : ---- " + str(clauses))
        for i in pairOfClauses:
            # print("pair of clauses: " + str(i))
            resolve = Resolve_C(i[0], i[1])
            # print(resolve)
            if not resolve:
                return "no"
            new.add(resolve.strip())
            # print(new)
            # print()
        # print("-----------------")
        if new.issubset(clauses):
            return "yes"
        clauses = clauses.union(new)


def canResolve_P(i, j):
    if (i[0] == '!') and (j[0] == '!'):
        return False
    if (i[0] == '!') | (j[0] == '!'):
        return True
    return False


def countWordFreq(set1, set2, word):
    list1 = list(set1.split(" "))
    list2 = list(set2.split(" "))

    list1.extend(list2)

    return list1.count(word)


def Resolve_P(set1, set2):
    oneElements = set1.split(" ")
    twoElements = set2.split(" ")

    # print(oneElements)
    # print(twoElements)

    ans = set()
    stop = False
    word = ""

    for i in oneElements :
        temp1 = i.replace("!", "")
        if not stop:
            for j in twoElements:
                if not stop:
                    temp2 = j.replace("!", "")
                    if temp1 == temp2 and canResolve_P(i,j):
                        word = temp1
                        stop = True
                else:
                    break
        else:
            break

    # list1 = list(set1.split(" "))
    # list2 = list(set2.split(" "))
    #
    # list1.extend(list2)
    #
    # print("list1 = ", end = "")
    # print(list1)
    #
    # print("word = " + word)
    #
    # if word != "":
    #     list1.remove(word)
    #     list1.remove("!" + word)
    #
    # print("list1 = ", end="")
    # print(list1)

    ans.update(list(set1.split(" ")))
    ans.update(list(set2.split(" ")))

    if word != "":
        ans.remove(word)
        ans.remove("!" + word)

    # print("After Resolution : " + str(ans))
    # print(ans)

    countWord = countWordFreq(set1, set2, word)
    countNotWord = countWordFreq(set1, set2, "!" + word)

    if countWord > 1:
        ans.add(word)
    if countNotWord > 1:
        ans.add("!" + word)

    correct = ""
    for i in ans:
        correct += i + " "

    # print(correct.strip())

    return correct


def call_P(clauses, predicates, variables, functions, constants):
    new = set()

    # pairOfClauses = list(combinations(clauses, 2))
    # print(pairOfClauses)
    # print(pairOfClauses[0])
    # print(pairOfClauses[0][0])
    # print(pairOfClauses[0][1])
    # print()

    while True:
        pairOfClauses = list(combinations(clauses, 2))
        # print("Clauses Set : ---- " + str(clauses))
        for i in pairOfClauses:
            # print("pair of clauses: " + str(i))
            resolve = Resolve_P(i[0], i[1])
            # print(resolve)
            if not resolve:
                return "no"
            new.add(resolve.strip())
            # print(new)
            # print()
        # print("-----------------")
        if new.issubset(clauses):
            return "yes"
        clauses = clauses.union(new)


def canResolve_U(i, j):
    if (i[0] == '!') and (j[0] == '!'):
        return False
    if (i[0] == '!') | (j[0] == '!'):
        return True
    return False


def unificationOnVariable(temp1, temp2):
    return temp1


def Resolve_U(set1, set2):
    oneElements = set1.split(" ")
    twoElements = set2.split(" ")

    # print(oneElements)
    # print(twoElements)

    ans = set()
    stop = False
    word = ""
    var = ""

    for i in oneElements:
        temp1 = i.replace("!", "")
        temp11 = temp1[0: temp1.index("(")]
        # print("temp1: " + temp1 + ", temp11: " + temp11)
        if not stop:
            for j in twoElements:
                if not stop:
                    temp2 = j.replace("!", "")
                    temp22 = temp2[0: temp2.index("(")]
                    # print("temp2: " + temp2 + ", temp22: " + temp22)
                    if temp11 == temp22 and canResolve_U(i, j):
                        word = temp11
                        var = unificationOnVariable( temp1[temp1.index("(") + 1 : temp1.index(")")], temp2[temp2.index("(") + 1 : temp2.index(")")] )
                        stop = True
                else:
                    break
            # print("---------")
        else:
            break

    # list1 = list(set1.split(" "))
    # list2 = list(set2.split(" "))
    #
    # list1.extend(list2)
    #
    # print("list1 = ", end = "")
    # print(list1)
    #
    if var != "":
        var = "(" + var + ")"

    # print("word = " + word)
    # print("var = " + var)

    #
    # if word != "":
    #     list1.remove(word)
    #     list1.remove("!" + word)
    #
    # print("list1 = ", end="")
    # print(list1)

    ans.update(list(set1.split(" ")))
    ans.update(list(set2.split(" ")))

    # print("After Resolution : " + str(ans))

    firstOccurence = 0
    firstNotOccurence = 0

    notWord = ""
    notNotWord = ""

    for i in ans:
        # print(i, end= " ")
        if i.find("!") != -1 and i[0: i.index("(")].replace("!","") == word and firstNotOccurence == 0:
            firstNotOccurence = 1
            notWord = i
        elif i.find("!") == -1 and i[0: i.index("(")] == word and firstOccurence == 0:
            firstOccurence = 1
            notNotWord = i

    if firstNotOccurence and firstOccurence:
        ans.remove(notWord)
        ans.remove(notNotWord)


    # if word != "":
    #     ans.remove(word + var)
    #     ans.remove("!" + word + var)

    # print("After Resolution : " + str(ans))
    # print(ans)

    countWord = countWordFreq(set1, set2, word)
    countNotWord = countWordFreq(set1, set2, "!" + word)

    if countWord > 1:
        ans.add(word)
    if countNotWord > 1:
        ans.add("!" + word)

    correct = ""
    for i in ans:
        correct += i + " "

    # print("Correct " + correct.strip())

    return correct


def call_U(clauses, predicates, variables, functions, constants):
    new = set()

    # pairOfClauses = list(combinations(clauses, 2))
    # print(pairOfClauses)
    # print(pairOfClauses[0])
    # print(pairOfClauses[0][0])
    # print(pairOfClauses[0][1])
    # print()

    while True:
        pairOfClauses = list(combinations(clauses, 2))
        # print("Clauses Set : ---- " + str(clauses))
        for i in pairOfClauses:
            # print("pair of clauses: " + str(i))
            resolve = Resolve_U(i[0], i[1])
            # print("Resolve " + resolve)
            if not resolve:
                return "no"
            new.add(resolve.strip())
            # print(new)
            # print()
        # print("-----------------")
        if new.issubset(clauses):
            return "yes"
        clauses = clauses.union(new)


def canResolve_UC(i, j):
    if (i[0] == '!') and (j[0] == '!'):
        return False
    if (i[0] == '!') | (j[0] == '!'):
        return True
    return False


def unification(variables, constants, one, two):
    if one in variables and two in variables:
        return True
    if one in variables and two in constants:
        return True
    if two in variables and one in constants:
        return True
    if one in constants and two in constants:
        if one == two:
            return True
        else:
            return False


def unificationOnVariableUC(one, two, variables, constants):
    if one in variables and two in variables:
        return unificationOnVariable(one, two)

    constant = ""
    if one in constants:
        constant = one
    elif two in constants:
        constant = two
    return constant


def Resolve_UC(set1, set2, variables, constants):
    oneElements = set1.split(" ")
    twoElements = set2.split(" ")

    print("Variables " + str(variables))
    print("Constants " + str(constants))

    # print(oneElements)
    # print(twoElements)

    ans = set()
    stop = False
    word = ""
    var = ""

    for i in oneElements:
        temp1 = i.replace("!", "")
        temp11 = temp1[0: temp1.index("(")]
        # print("temp1: " + temp1 + ", temp11: " + temp11)
        if not stop:
            for j in twoElements:
                if not stop:
                    temp2 = j.replace("!", "")
                    temp22 = temp2[0: temp2.index("(")]
                    # print("temp2: " + temp2 + ", temp22: " + temp22)
                    if temp11 == temp22 and canResolve_UC(i, j) and unification(variables, constants, temp1[temp1.index("(") + 1: temp1.index(")")], temp2[temp2.index("(") + 1: temp2.index(")")]):
                        word = temp11
                        var = unificationOnVariableUC(temp1[temp1.index("(") + 1: temp1.index(")")],
                                                    temp2[temp2.index("(") + 1: temp2.index(")")], variables, constants)
                        stop = True
                else:
                    break
            # print("---------")
        else:
            break

    # list1 = list(set1.split(" "))
    # list2 = list(set2.split(" "))
    #
    # list1.extend(list2)
    #
    # print("list1 = ", end = "")
    # print(list1)
    #


    # if var != "":
    #     var = "(" + var + ")"


    print("word = " + word)
    print("var = " + var)

    #
    # if word != "":
    #     list1.remove(word)
    #     list1.remove("!" + word)
    #
    # print("list1 = ", end="")
    # print(list1)

    ans.update(list(set1.split(" ")))
    ans.update(list(set2.split(" ")))

    print("After Resolution : " + str(ans))
    
    
    ans = performUnification(ans, variables, constants)
    

    firstOccurence = 0
    firstNotOccurence = 0

    notWord = ""
    notNotWord = ""

    for i in ans:
        # print(i, end= " ")
        if i.find("!") != -1 and i[0: i.index("(")].replace("!", "") == word and firstNotOccurence == 0:
            firstNotOccurence = 1
            notWord = i
        elif i.find("!") == -1 and i[0: i.index("(")] == word and firstOccurence == 0:
            firstOccurence = 1
            notNotWord = i

    if firstNotOccurence and firstOccurence:
        ans.remove(notWord)
        ans.remove(notNotWord)

    # if word != "":
    #     ans.remove(word + var)
    #     ans.remove("!" + word + var)

    print("After removal : " + str(ans))
    # print(ans)

    countWord = countWordFreq(set1, set2, word)
    countNotWord = countWordFreq(set1, set2, "!" + word)

    if countWord > 1:
        ans.add(word)
    if countNotWord > 1:
        ans.add("!" + word)

    correct = ""
    for i in ans:
        correct += i + " "

    # print("Correct " + correct.strip())

    return correct


def call_UC(clauses, predicates, variables, functions, constants):
    new = set()

    # pairOfClauses = list(combinations(clauses, 2))
    # print(pairOfClauses)
    # print(pairOfClauses[0])
    # print(pairOfClauses[0][0])
    # print(pairOfClauses[0][1])
    # print()

    while True:
        pairOfClauses = list(combinations(clauses, 2))
        # print("Clauses Set : ---- " + str(clauses))
        for i in pairOfClauses:
            print("pair of clauses: " + str(i))
            resolve = Resolve_UC(i[0], i[1], variables, constants)
            # print("Resolve " + resolve)
            if not resolve:
                return "no"
            new.add(resolve.strip())
            # print(new)
            # print()
        # print("-----------------")
        if new.issubset(clauses):
            return "yes"
        clauses = clauses.union(new)


def main():

    # print(sys.argv[1]) # lab2.py
    # print(sys.argv[2]) # testcases/functions/f1.cnf
    # print()

    clauses, predicates, variables, functions, constants = parseFile(sys.argv[2])
    # print(clauses)
    # print(type(clauses))
    # print()

    s = sys.argv[2].split("/")
    check = s[-1]
    if check[0] == 'f':
        print(call_F(clauses, predicates, variables, functions, constants))
    elif check[0] == 'p':
        print(call_P(clauses, predicates, variables, functions, constants))
    elif check[0] == 'c':
        print(call_C(clauses, predicates, variables, functions, constants))
    elif check[0] == 'u' and check[1] == 'c':
        print(call_UC(clauses, predicates, variables, functions, constants))
    elif check[0] == 'u':
        print(call_U(clauses, predicates, variables, functions, constants))


    #if len(sys.argv) == 5:
    # doImageOperations(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == '__main__':
    main()
