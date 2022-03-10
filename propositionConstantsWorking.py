import os
import sys
from itertools import combinations


def parseFile(s):
    clauses = set()
    with open(s) as f:
        clause = 0
        for line in f.readlines():
            if clause == 0:
                if line.startswith("Clauses:"):
                    clause = 1
            elif clause == 1:
                clauses.add(line.strip().replace("\\", "").replace("{","").replace("}",""))

    return clauses


def call_U(clauses):
    pass


def call_F(clauses):
    pass


def call_UC(clauses):
    pass


def call_C(clauses):
    return call_P(clauses)


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



def call_P(clauses):
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



def main():

    # print(sys.argv[1]) # lab2.py
    # print(sys.argv[2]) # testcases/functions/f1.cnf
    # print()

    clauses = parseFile(sys.argv[2])
    # print(clauses)
    # print(type(clauses))
    # print()

    s = sys.argv[2].split("/")
    check = s[-1]
    if check[0] == 'f':
        print(call_F(clauses))
    elif check[0] == 'p':
        print(call_P(clauses))
    elif check[0] == 'c':
        print(call_C(clauses))
    elif check[0] == 'u' and check[1] == 'c':
        print(call_UC(clauses))
    elif check[0] == 'u':
        print(call_U(clauses))



    #if len(sys.argv) == 5:
    # doImageOperations(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == '__main__':
    main()
