import rand
import file
import printer

if __name__=='__main__':
    """
    ----rand.py-----
    rand.genInt(lowbound,upbound)   
                #lowbound:随机数下界 
                #upbound:随机数上界 
    rand.genChar(isUpper = True, isLower = True, isNumber = True, isSpecial = True, customList = None)   
                #isUpper:包含大写字母 
                #isLower:包含小写字母
                #isNumber:包含数字
                #isSpecial:包含特殊符号
                #customList:自定义随机列表
    rand.genFloat(lowbound,upbound,eps) 
                #lowbound:随机数下界 
                #upbound:随机数上界 
                #小数位数
    rand.genBool()
    rand.rndChoice(rndlist)        
                #rndlist: 随机返回rndlist中的一个元素
    rand.genList(randfunc,**kwargs, list_length ,dimen = 1, sorted = False, unique = False, include = None, exception = []) 
                #randfunc: 随机函数
                #**kwargs: 随机函数参数表
                #list_length:长度
                #dimen:维度
                #sorted:是否排序
                #unique:元素是否唯一
                #include: 必定包含的元素
                #exception: 必定不包含的元素
    rand.genLinkedList(length, lowbound, upbound, sorted = False, unique = False)
                #length:长度
                #lowbound:随机数下界
                #uppbound:随机数上界
                #sorted:是否排序
                #unique:元素是否唯一
    rand.genString(str_length, isUpper = True, isLower = True, isNumber = True, isSpecial = True, customList = None) 
                #str_length:长度(可以是rand.genInt,需要提供参数)
                #isUpper:包含大写字母 
                #isLower:包含小写字母
                #isNumber:包含数字
                #isSpecial:包含特殊符号
                #customList:自定义随机列表
    rand.genTree(lowbound, upbound, vertice, unique = False)
                #lowbound:随机数下界
                #uppbound:随机数上界
                #vertice:点数
                #unique:元素是否唯一
    rand.genBST(lowbound, upbound, vertice)
                #lowbound:随机数下界
                #uppbound:随机数上界
                #vertice:点数
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


