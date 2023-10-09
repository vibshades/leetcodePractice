# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class WrapperNodes:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyHead = ListNode()
        prevNode = dummyHead
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, WrapperNodes(lists[i]))
                lists[i] = lists[i].next
        while(len(heap)):
            currNode = heapq.heappop(heap).node
            prevNode.next = currNode
            prevNode = prevNode.next
            if currNode.next:
                heapq.heappush(heap, WrapperNodes(currNode.next))
        return dummyHead.next