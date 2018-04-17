import random
import printer
import queue 
from util.Graph import GraphNode
from util.Tree import TreeNode

def genInt(lowbound,upbound):
    return random.randint(lowbound,upbound)

def genBool():
    if random.randint(1,2) % 2 == 1:
        return True
    return False

def genFloat(lowbound,upbound,eps):
    return round(random.uniform(lowbound,upbound),eps)

def genChar(isUpper = True,isLower = True,isNumber = True,isSpecial = True,customList = None):
    s = ""
    if customList is not None:
        for char in customList:
            s += char
        return rndChoice(s)
    if isLower == True:
        s += 'abcdefghijklmnopqrstuvwxyz'
    if isUpper == True:
        s += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if isNumber == True:
        s += '0123456789'
    if isSpecial == True:
        s += r'!@#$%^&*()_+-=[]{};\':\",./<?>\|`'
    return rndChoice(s)

def rndChoice(rndlist):
    return random.choice(rndlist)

def genString(str_length,isUpper = True,isLower = True,isNumber = True,isSpecial = True,unique = False,customList = None,**kwargs):
    s = ""
    if not isinstance(str_length,int):
        str_length = str_length(**kwargs)
    for _ in range(str_length):
        while True:
            char = genChar(isLower=isLower,isUpper=isUpper,isNumber=isNumber,isSpecial=isSpecial,customList=customList)
            if not unique or char not in s :
                break
        s += char
    return s

def genList(randfunc,
            list_length,
            dimen = 1,
            sorted = False,
            unique = False,
            include = None,
            exception = [],
            **kwargs):
    temp = []
    if include is not None:
        temp = include
    if dimen > 1:
        for _ in range(list_length):
            temp.append(genList(randfunc,list_length,dimen - 1,sorted = sorted,unique = unique,**kwargs))
    else:
        for _ in range(list_length-len(temp)):
            t = randfunc(**kwargs)
            while unique and t in temp or t in exception:
                t = randfunc(**kwargs)
            temp.append(t)
        if sorted == True:
            return temp.sort()
    return temp

def genLinkedList(length, lowbound, upbound, sorted = False, unique = False):
    res = []
    if unique and length > upbound - lowbound + 1:
        return []
    for _ in range(length):
        element = genInt(lowbound,upbound)
        if unique:
            while element in res:
                element = genInt(lowbound,upbound)
        res.append(element)
    if sorted:
        res.sort()    
    return res


def genGraph(vertice,edge,dircted = False,connected = False):
    if edge > vertice * (vertice - 1):
        raise Exception("Edge exceeded maximum value!")
    if edge < vertice - 1:
        raise Exception("Edge exceeded minimum value!")
    while True:
        nodeList = [GraphNode(val = _) for _ in range(vertice)]
        if dircted == False:
            edge *= 2
        edgeRemain = edge
        
        for node in nodeList:
            node.next=genList(
                genInt,
                lowbound = 0, 
                upbound = vertice - 1, 
                unique = True,
                prevList = node.next,
                exception = [node.val],
                list_length = min((edge + 1) // vertice, edgeRemain)
            )
            edgeRemain -= (edge + 1) // vertice
            if dircted == False:
                for endPoint in node.next:
                    for index in nodeList:
                        if index.val == endPoint and node.val not in index.next:
                            index.next.append(node.val)
        #printer.printGraph(nodeList)
        if connected and GraphNode.check(nodeList):
            break
    return nodeList

def genTree(lowbound, upbound,vertice, unique = False):
    #if (unique and nodes > upbound - lowbound + 1) or nodes < 1:
    #    return None
    head = TreeNode(genInt(lowbound, upbound))   
    res = []
    res.append(head.val) 
    count = 1
    q = queue.Queue()
    q.put(head) 
    while not q.empty():
        length = q.qsize()
        Idx = genInt(0, length - 1)
        for i in range(length):
            if count == vertice:
                return head
            node = q.get()
            if i == Idx:
                roll = genInt(1, 3)
            else:
                roll = genInt(0, 3)

            num = (roll + 1) // 2
            if count + num > vertice:
                roll = genInt(1, 2)
            if roll == 0:
                continue
            elif roll == 1 or roll == 2:
                ele = genInt(lowbound, upbound)
                if unique:
                    while ele in res:
                        ele = genInt(lowbound, upbound)
                cur = TreeNode(ele)
                res.append(cur.val)
                q.put(cur)
                if roll == 1:
                    node.left = cur
                else:
                    node.right = cur
            else:
                ele1 = genInt(lowbound, upbound)
                ele2 = genInt(lowbound, upbound)
                if unique:
                    while ele1 in res:
                        ele1 = genInt(lowbound, upbound)
                    res.append(ele1)    
                    while ele2 in res:
                        ele2 = genInt(lowbound, upbound)
                    res.append(ele2)
                left = TreeNode(ele1)
                right = TreeNode(ele2)
                node.left = left
                node.right = right
                q.put(left)
                q.put(right)
            count += num

    return head

def genBST(lowbound, upbound,vertice):
    if vertice > upbound - lowbound + 1:
        return None
    head = TreeNode(genInt(lowbound,upbound))
    res = []
    count = 1
    res.append(head.val)
    while count < vertice:
        ele = genInt(lowbound, upbound)
        while ele in res:
            ele = genInt(lowbound, upbound)
        node = TreeNode(ele)
        head = TreeNode.insertBSTNode(head, node)
        count += 1
    return head     