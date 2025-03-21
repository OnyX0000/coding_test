# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 더미 노드 생성 (결과 연결 리스트의 시작)
        cur = dummy  # 결과 연결 리스트를 작성하기 위한 포인터

        # 두 리스트가 모두 비어있을 때까지 반복
        while list1 and list2 :
            if list1.val < list2.val :
                cur.next = list1
                list1 = list1.next
            else :
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 남은 노드를 결과 리스트에 연결
        if list1 :
            cur.next = list1
        if list2 :
            cur.next = list2

        return dummy.next  # 더미 노드 다음 노드가 실제 결과의 시작