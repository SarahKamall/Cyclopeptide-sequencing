import numpy as np

FileOfWeights = open("weight.txt")
speclist = [0, 97, 97, 99, 101, 103, 196, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]
weightsDict = {}

for line in FileOfWeights:
    line = line.rstrip()
    column = line.split(" ")
    weightsDict[column[0]] = int(column[1])
# print(weightsDict)
SpectrumList = []
# speclist2 = speclist.copy()

# size = int(input("Enter the size of the list "))
# SpectrumList = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:size]
# Spectrum list : 0 97 97 99 101 103 196 198 200 202 295 297 299 299 301 394 396 398 400 400 497
# its size : 21
def unique(list1) -> speclist:
    x = np.array(list1)
    list1 = np.unique(x)
    return list1

def InitialList():
    initialList = []
    for key in weightsDict:
        for j in range(len(speclist)):
            if weightsDict[key] == speclist[j]:
                initialList.append(key)
    return initialList

print(InitialList())
# print(list(set(InitialList())))
def LinearScoring(word):
    newlist = []
    listsum=[]
    for i in range(1,len(word)):
        for j in range(0, len(word)-i+1):
            newlist.append(word[j:j+i])
    newlist.append(word)
    for h in newlist:
        sum = 0
        for o in h:
          sum+=weightsDict[o]
        listsum.append(sum)

    return listsum

def isConsistent(num, speclist2):
    flag=False
    for i in range(0, len(num)):
        if num[i] in speclist2:
            flag=True
        else:
            return False

    if flag and len(num)>3:
        speclist2.remove(num[len(num)-1])
    return flag

# initial_list = ['A', 'B', 'C', 'D']
initial_list = InitialList()
NewList = []


def ExtendFunction(initial_list):

    flag = True
    index = 0
    while flag:
        flag = False
        speclist2 = speclist.copy()
        if index == 0:
            for i in range(0, len(initial_list)):
                for j in range(0, len(initial_list)):
                    if i == j:
                        continue
                    else:
                        newstring = initial_list[i] + initial_list[j]
                        if newstring in NewList:
                            continue
                        else:
                            if isConsistent(LinearScoring(newstring), speclist2):
                                #newstring = newstring.split()
                                NewList.append(newstring)
                                flag = True
            two_mers_list = unique(NewList)
            print(two_mers_list)
            NewList.clear()
            index += 1
        else:
            for i in range(0, len(two_mers_list)):
                for k in two_mers_list[i]:
                    initial_list.remove(k)
                for j in range(0, len(initial_list)):
                    newstring = two_mers_list[i] + initial_list[j]
                    if newstring in NewList:
                        continue
                    else:
                        if isConsistent(LinearScoring(newstring), speclist2):
                            NewList.append(newstring)
                            flag = True
                for k in two_mers_list[i]:
                    initial_list.append(k)
            two_mers_list = NewList
            two_mers_list = unique(two_mers_list)
            print(two_mers_list)
            NewList.clear()


ExtendFunction(initial_list)


# print(LinearScoring("LEQN"))