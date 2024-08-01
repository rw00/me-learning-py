class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        merged = ListNode()
        current = merged
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        while list1 != None:
            current.next = ListNode(list1.val)
            list1 = list1.next
            current = current.next
        while list2 != None:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next
        return merged.next
