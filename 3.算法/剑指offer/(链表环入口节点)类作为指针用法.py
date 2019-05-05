#类作为指针用法
#寻找环的入口
#计入fast和slow香芋距离入口节点b个单位的位置，环剩下的长度为c,则a+b+c+b = 2*(a+b) -> a = c 
class Solution(object):
    def hasCycle(self, head):#传入head为class 类型
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:#
                return True
        return False
	
	def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead== None or pHead.next == None:
            return None
        fast = slow = pHead
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while(fast!=slow):
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
