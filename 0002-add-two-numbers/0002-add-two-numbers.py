# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 더미 노드 생성 (결과 연결 리스트의 시작)
        current = dummy  # 결과 연결 리스트를 작성하기 위한 포인터
        carry = 0  # 초기 자리올림 수는 0

        while l1 or l2 or carry :
            # 현재 노드의 값 계산 (l1, l2가 없으면 0으로 처리)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 두 값을 더하고 자리올림 수를 더함
            total = val1 + val2 + carry
            carry = total // 10  # 자리올림 계산
            new_val = total % 10  # 현재 자리의 값

            # 새 노드를 생성하여 연결 리스트에 추가
            current.next = ListNode(new_val)
            current = current.next

            # l1과 l2를 다음 노드로 이동
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next

        return dummy.next  # 더미 노드 다음 노드가 실제 결과의 시작