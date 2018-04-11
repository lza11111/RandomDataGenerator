import rand
import file
import printer

if __name__=='__main__':
    """
    ----rand.py-----
    rand.genInt(lowbound,upbound)   
                #lowbound:随机数下界 
                #upbound:随机数上界 
    rand.genChar(isUpper = True, isLower = True)   
                #isUpper:包含大写字母 
                #isLower:包含小写字母
    rand.genFloat(lowbound,upbound,eps) 
                #lowbound:随机数下界 
                #upbound:随机数上界 
                #小数位数
    rand.genBool()
    rand.rndChoice(rndlist)        
                #rndlist: 随机返回rndlist中的一个元素
    rand.genList(randfunc,**kwargs, length,dimen = 1, sorted = False, unique = False) 
                #randfunc: 随机函数
                #**kwargs: 随机函数参数表
                #length:长度
                #dimen:维度
                #sorted:是否排序
                #unique:元素是否唯一
    rand.genLinkedList(length, lowbound, upbound, sorted = False, unique = False)
                #length:长度
                #lowbound:随机数下界
                #uppbound:随机数上界
                #sorted:是否排序
                #unique:元素是否唯一
    rand.genString(length,isUpper = True, isLower = True) 
                #length:长度
                #isUpper:包含大写字母 
                #isLower:包含小写字母
    rand.genTree(lowbound, upbound,maxDepth, unique = False)
                #lowbound:随机数下界
                #uppbound:随机数上界
                #maxDepth:最大深度
                #unique:元素是否唯一
    rand.genBST(lowbound, upbound,maxDepth)
                #lowbound:随机数下界
                #uppbound:随机数上界
                #maxDepth:最大深度
    rand.genGraph(vertice,edge,dircted = False,connected = False)
                #vertice: 点数
                #edge:边数
                #dircted:是否为有向图
                #connected:图是否连通

    -----file.py-----
    file.writeToFile(filename)  
                #filename:文件名
    file.closeFile()

    -----printer.py------
    printer.printList(list)   
                #list:待输出List
    printer.printString(list)
                #list:输出为string的格式
    printer.printFunc(name,*args)
                #name:方法名
                #*args:参数
    printer.printTree(tree)
                #tree:树的根节点(TreeNode)
    printer.printGraph(nodeList)
                #nodeList:包含GraphNode的list
    """
    
    
