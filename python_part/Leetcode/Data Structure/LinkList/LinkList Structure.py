'''
linklist由 node和head组成的：
在python中 linklist的实现也同样是依靠这两个部分而实现的：

在python中：

    node 是一个class的obj
    head是一个特殊的node，用于表示整个list

而之所以node可以实现linklist的原因在于 obj 的赋值本质上是内存地址的赋值，而内存地址的链接，就是linklist 各个node之间的连接方式。

因此node的定义和链接就显得非常的重要。

linklist除了必须要记录list的head，还可以有其他功能，例如：打印，长度，前端插入，后端插入，删除等功能。
'''

'''
    一。 node的定义
'''


class Node:
    def __init__(self, data=None, next=None):  # java中的constructor
        self.data = data
        self.next = next

    def __str__(self):  # java 中的 toString
        return str(self.data)


'''
   二。 LinkList的基本定义
'''


class SimpleLinkList:
    def __init__(self, head: Node = None):
        self.head = head

    def __len__(self):
        current_node = self.head
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next

        return counter


'''
   三。 建立LinkList
'''

# 初始化node
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wensday")

# 建立LinkList
# 1. 给出head
# 2. 链接起所有node

linklist1 = SimpleLinkList(head=node1)

node1.next = node2  # obj的赋值
node2.next = node3

'''
就是因为obj的赋值是地址的赋值，因此也就因此构成了linklist
'''

'''
  四。 使用LinkList的方法
'''


# Linklist的打印

def printList(node):
    while node:
        print(node)
        node = node.next


        '''
        遍历注意事项：
        
        遍历列表的时候，最后一个项之后， node会被赋值为None，此时while就会循环。
        但要注意，如果node都循环到了None，那么此时node == None， 而none是没有property的, 换句话说， node.data, or node. next都是不存在的。
        '''



'''
 五。完整的链表：
 完整的链表还需要包含一些基本的功能，包括：
    前端插入
    后端插入
    在中间插入
    查找
    删除
    打印
'''


class CompleteLinkList:
    def __init__(self, head: Node=None):
        self.head = head

    def __len__(self):
        currnode = self.head
        cnt = 0

        while currnode is not None:
            cnt += 1
            currnode = currnode.next

    '''
    前端插入（插入到head处）
    插入的是data，不是node因此：
    1。 检查data 是否是无效data（None）
    2。 建立node ( next = head)
    3。 更改head 
    '''
    def insertToFront(self, data):
        # 如果被插入的节点是None,那不是扯淡么，直接返回，什么都不做
        if data is None:
            return
        node = Node(data=data, next = self.head)
        self.head = node


    '''
    从后端插入（插入到list的tail上）
    又叫append
    
    1. 判定被插入数据是否是none
    2。 判定list是否为空。（如果把该项并入到while循环中，将会插入到list的第二个位置上，而不是头上）
    3。 while 寻找，直到 next为空为止
    4。 空next 被新插入到node替换掉
    
    
    '''
    def append(self, data):
        if data is None:
            return

        node = Node(data)


        if self.head is None:
            self.head = node
            return


        currnode = self.head
        while currnode.next is not None:
            currnode = currnode.next

        currnode.next = node
        return


    '''
    链表的中间插入
    
    
    '''

    def insert(self, position: Node, data):
        if position is None:
            print(" the position is absent, try another one")
            return

        node = Node(data=data, next=position.next)
        position.next = node















    '''
    打印输出
    '''

    # def __str__(self):  ## __str__函数不是print用的，而是返回一个字符串的， 一定有return string 的格式
    #     currnode = self.head
    #     show = []
    #
    #     while currnode:  # while 循环可以自动循环到none为止
    #         show.append(str(currnode))
    #         currnode = currnode.next
    #     return str(show)

    def print(self):
        currnode = self.head

        while currnode:
            print(currnode, end=", ")
            currnode = currnode.next

        print("\n")



    '''
    linklist的查找
    
    '''

    def find(self, data):
        if data is None:
            return

        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            else:
                curr = curr.next

        return None


    '''
    delete
    
    3个特殊情况：
    1。 被删除的data == None
    2。 linkList是 None
    3。 被删除的data在head上
    
    
    删除的方法：
    若current.next符合条件，则让 current.next = current.next.next 就把 下一项从链中解脱出来了。
    
    '''

    def delete(self, data):

        if data is None:
            return

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next

        curr = self.head
        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return   #放在里面就不用继续找了

            curr = curr.next













# insert testing
l = CompleteLinkList()
l.head = node1
l.print()

l.insert(position=node2, data=6)  # position 必须是node，不是data
l.print()



# delete testing

l = CompleteLinkList()
l.head = node1
l.print()

l.delete("Tuesday")
l.print()

l.delete("Wensday")
l.print()

