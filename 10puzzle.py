import time
def possible(inputlist: list[int], goal:int) -> bool:
    recursiondepth = -1
    def allnumbers(inputlist:list[int]):
        nonlocal recursiondepth
        recursiondepth += 1
        binarylist = [0]*len(inputlist)
        storeset = set()
        alreadydone = []
        if len(inputlist) == 1:
            storeset.add(inputlist[0])
            recursiondepth -= 1
            return storeset
        while binarylist[-1] != 1:
            for digits in range(len(binarylist)):
                if binarylist[digits] == 0:
                    binarylist[digits] = 1
                    break
                else:
                    binarylist[digits] = 0
            leftlist = []
            rightlist = []
            for includeinleft in range(len(binarylist)):
                if binarylist[includeinleft] == 1:
                    leftlist.append(inputlist[includeinleft])
                else:
                    rightlist.append(inputlist[includeinleft])
            if leftlist in alreadydone:
                continue
            else:
                alreadydone.append(leftlist)
            left = allnumbers(leftlist)
            right = allnumbers(rightlist)
            for lkeys in left:
                for rkeys in right:
                    storeset.add(lkeys + rkeys)
                    if lkeys >= rkeys:
                        storeset.add(lkeys - rkeys)
                    else:
                        storeset.add(rkeys - lkeys)
                    storeset.add(lkeys * rkeys)
                    if lkeys != 0:
                        storeset.add(rkeys / lkeys)
                    if rkeys != 0:
                        storeset.add(lkeys / rkeys)
            if recursiondepth == 0 and goal in storeset:
                return storeset
            elif recursiondepth == 0:
                storeset.clear()
        recursiondepth -= 1
        return storeset
    if goal in allnumbers(inputlist):
        return True
    else:
        return False

def puzzle(inputlist: list[int], goal:int, getone = False) -> None:
    recursiondepth = -1
    newlist = []
    def allpatterns(inputlist:list[int]):
        nonlocal recursiondepth
        recursiondepth += 1
        binarylist = [0]*len(inputlist)
        storedict = {}
        if len(inputlist) == 1:
            storedict[str(inputlist[0])] = inputlist[0]
            recursiondepth -= 1
            return storedict
        while binarylist[-1] != 1:
            for digits in range(len(binarylist)):
                if binarylist[digits] == 0:
                    binarylist[digits] = 1
                    break
                else:
                    binarylist[digits] = 0
            leftlist = []
            rightlist = []
            for includeinleft in range(len(binarylist)):
                if binarylist[includeinleft] == 1:
                    leftlist.append(inputlist[includeinleft])
                else:
                    rightlist.append(inputlist[includeinleft])
            left = allpatterns(leftlist)
            right = allpatterns(rightlist)
            for lkeys in left:
                lvalue = left[lkeys]
                leftsymbols = []
                leftlastsymbol = set()
                extrabracketonleft = False
                for index, symbol in enumerate(lkeys):
                    if index == 0 and symbol == '-':
                        continue
                    if symbol == '(':
                        leftsymbols.append(symbol)
                    elif symbol == ')':
                        leftsymbols.pop()
                    elif len(leftsymbols) == 0 and symbol in {'+', '-', '*', '/'}:
                        leftlastsymbol.add(symbol)
                for rkeys in right:
                    rvalue = right[rkeys]
                    rightsymbols = []
                    rightlastsymbol = set()
                    extrabracketonright = False
                    for index, symbol in enumerate(rkeys):
                        if index == 0 and symbol == '-':
                            continue
                        if symbol == '(':
                            rightsymbols.append(symbol)
                        elif symbol == ')':
                            rightsymbols.pop()
                        elif len(rightsymbols) == 0 and symbol in {'+', '-', '*', '/'}:
                            rightlastsymbol.add(symbol)
                    if lkeys[0] == '-' and not leftlastsymbol:
                        lkeys = '(' + lkeys + ')'
                    if rkeys[0] == '-' and not rightlastsymbol:
                        rkeys = '(' + rkeys + ')'
                    storedict[f'{lkeys} + {rkeys}'] = lvalue + rvalue
                    if '+' in rightlastsymbol or '-' in rightlastsymbol:
                        storedict[f'{lkeys} - ({rkeys})'] = lvalue - rvalue
                    else:
                        storedict[f'{lkeys} - {rkeys}'] = lvalue - rvalue
                    if '+' in leftlastsymbol or '-' in leftlastsymbol:
                        storedict[f'{rkeys} - ({lkeys})'] = rvalue - lvalue
                    else:
                        storedict[f'{rkeys} - {lkeys}'] = rvalue - lvalue
                    if not extrabracketonleft and ('+' in leftlastsymbol or '-' in leftlastsymbol):
                        lkeys = '(' + lkeys + ')'
                        extrabracketonleft = True
                    if not extrabracketonright and ('+' in rightlastsymbol or '-' in rightlastsymbol):
                        rkeys = '(' + rkeys + ')'
                        extrabracketonright = True
                    storedict[f'{lkeys} * {rkeys}'] = lvalue * rvalue
                    if not extrabracketonleft and ('*' in leftlastsymbol or '/' in leftlastsymbol):
                        lkeys = '(' + lkeys + ')'
                        extrabracketonleft = True
                    if lvalue != 0:
                        storedict[f'{rkeys} / {lkeys}'] = rvalue / lvalue
                    if extrabracketonleft and ('+' not in leftlastsymbol and '-' not in leftlastsymbol):
                        lkeys = lkeys[1:-1]
                        extrabracketonleft = False
                    if not extrabracketonright and ('*' in rightlastsymbol or '/' in rightlastsymbol):
                        rkeys = '(' + rkeys + ')'
                        extrabracketonright = True
                    if rvalue != 0:
                        storedict[f'{lkeys} / {rkeys}'] = lvalue / rvalue
                    if extrabracketonleft:
                        extrabracketonleft = False
                        lkeys = lkeys[1:-1]
            if recursiondepth == 0 and getone == True and goal in storedict.values():
                return storedict
            elif recursiondepth == 0 and getone == True:
                storedict.clear()
        recursiondepth -= 1
        return storedict
    patternslist = allpatterns(inputlist)
    for expression in patternslist:
        if patternslist[expression] == goal:
            print(expression)
            if getone is True:
                return
    return

# create list of all numbers of given digit
def createallset(digits: int) -> list:
    templist = [0]*digits
    possibilityset = ['0'*digits]
    while templist != [9]*digits:
        for index in range(1, digits + 1):
            if templist[-index] != 9:
                templist[-index] += 1
                break
            else:
                if index == digits:
                    break
                templist[-index] = 0
        for index in range(1, digits):
            if templist[index] < (templist[index - 1]):
                templist[index] = (templist[index-1])
        possibilityset.append(''.join(map(str, templist)))
    return possibilityset

# find all combinations of numbers out of given list that can create goal
def findall(possibility: list, goal:int) -> list:
    successlist = []
    for y in possibility:
        templist = []
        for char in y:
            templist.append(int(char))
        if possible(templist, goal):
            successlist.append(y)
    return successlist

def testall(digits: int, goal:int):
    a = createallset(digits)
    b = set(findall(a, goal))
    return b


def main():
    print(testall(4, 10))

if __name__ == '__main__':
    main()