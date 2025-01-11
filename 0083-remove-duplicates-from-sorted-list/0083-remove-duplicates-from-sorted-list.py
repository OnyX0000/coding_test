# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # 현재 노드 시작

        while current and current.next :
            if current.val == current.next.val :
                # 현재 노드와 다음 노드의 값이 같으면 중복 제거
                current.next = current.next.next
            else :
                # 값이 다르면 다음 노드로 이동
                current = current.next

        return head  # 중복 제거된 연결 리스트 반환