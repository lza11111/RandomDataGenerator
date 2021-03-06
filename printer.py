from util.Graph import GraphNode
from util.Tree import TreeNode
import queue

def printBase(obj):
    if isinstance(obj,list):
        printList(obj)
    elif isinstance(obj,str):
        printString(obj)
    else:
        print(obj,end='')

def printList(lst):    #打印数组
    print('[',end='')
    if len(lst) > 0:
        printBase(lst[0])
        for i in range(1,len(lst)):
            print(',',end='')
            printBase(lst[i])
    print(']',end='')

def printLinkedList(listNode):
    for i in range(len(listNode)):
        print(str(listNode[i]), end = '')
        print('->', end = '')
    print('null',end = '')     

def printString(s):
    print('"',end='')
    print(s,end='')
    print('"',end='')

def printGraph(nodeList):
    print("{",end='')
    if len(nodeList) > 0:
        print(nodeList[0].val,end='')
        for _ in nodeList[0].next:
            print(','+str(_),end='')
    
    for index in range(1,len(nodeList)):
        print('#',end='')
        print(nodeList[index].val,end='')
        for _ in nodeList[index].next:
            print(','+str(_),end='')

    print("}",end='')

def printTree(tree):
    if tree is None:
        print('null', end = '')
        return
    print('{', end = '')
    print(str(tree.val), end = '')
    
    q = queue.Queue()
    q.put(tree)
    count = 0
    while not q.empty():
        cur = q.get()
        
        if cur.left is None:
            count += 1
        else:
            q.put(cur.left)
            print(',', end = '')
            for _ in range(count):
                print('#', end = '')
                print(',', end = '')
            print(str(cur.left.val), end = '')
            count = 0
        
        if cur.right is None:
            count += 1
        else:
            q.put(cur.right)
            print(',', end = '')
            for _ in range(count):
                print('#', end = '')
                print(',', end = '')
            print(str(cur.right.val), end = '') 
            count = 0 
    print('}', end = '')       
     
def printFunc(name,*args):
    argcnt = 0
    print(name,end='')
    print("(",end='')

    for _ in args:
        if argcnt > 0:
            print(',',end='')
        argcnt += 1
        printBase(_)
    print(")",end='')



