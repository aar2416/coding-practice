class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1, l2)
        carry = 0
        l3 = None
        
        is_traversed_l1 = False
        
        is_traversed_l2 = False
        while(True):
            element = 0
            if l1 is not None and l1.next is not None:
                element = l1.val
                l1 = l1.next
            elif l1 is not None and l1.next is None and not is_traversed_l1:
                element = l1.val
                l1 = l1.next
                is_traversed_l1 = True
            
            element1 = 0
            if l2 is not None and l2.next is not None:
                element1 = l2.val
                l2 = l2.next
            elif l2 is not None and l2.next is None and not is_traversed_l2:
                element1 = l2.val
                l2 = l2.next
                is_traversed_l2 = True

            sum_of_element = element + element1 + carry
            carry = sum_of_element//10
            sum_of_element %= 10 
            node1 = ListNode()
            node1.next = None
            node1.val = sum_of_element
            if l3 is None:
                l3 = node1
            else:
                node1.next = l3
                l3 = node1
            if is_traversed_l2 and is_traversed_l1:
                if carry == 1:
                    node1 = ListNode()
                    node1.next = None
                    node1.val = carry
                    if l3 is None:
                        l3 = node1
                    else:
                        node1.next = l3
                        l3 = node1
                break
        l4 = None
        if l3 is None:
            return ListNode()
        while(True):
            element = 0
            node1 = ListNode()
            node1.next = None
            node1.val = l3.val
            
            l3 = l3.next
            if l4 is None:
                l4 = node1
            else:
                node1.next = l4
                l4 = node1
                
            if l3 is not None and l3.next is None:
                node1 = ListNode()
                node1.next = None
                node1.val = l3.val
                if l4 is None:
                    l4 = node1
                else:
                    node1.next = l4
                    l4 = node1
                break
            if l3 is None:
                break
        del l3
            
        return l4
        