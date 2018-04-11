class GraphNode:
    def __init__(self, *args, **kwargs):
        self.next = []
        self.val = kwargs.get('val')
    
    @staticmethod
    def check(nodeList):
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        root = [_ for _ in range(len(nodeList))]
        for node in nodeList:
            for endPoint in node.next:
                x = find(node.val)
                y = find(endPoint)
                if x != y:
                    root[x] = y
        connect = 0
        for index in range(len(root)):
            if index == find(index):
                connect += 1
        if connect > 1:
            return False
        return True