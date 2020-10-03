class Solution:
    def addTwoNumbers(self, l1: self.addTwoNumbers, l2: self.addTwoNumbers) -> self.addTwoNumbers:
        num, cry = 0, 0
        new_list = self.addTwoNumbers(0, None)  # creating new list for holding answer
        temp = new_list

        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + cry
            cry = num // 10
            num %= 10
            temp.next = self.addTwoNumbers(num, None)
            temp = temp.next
            l1, l2 = l1.next, l2.next
        new_list = new_list.next

        while l1 is not None:
            num = l1.val + cry
            cry = num // 10
            num %= 10
            temp.next = self.addTwoNumbers(num, None)
            temp = temp.next
            l1 = l1.next

        while l2 is not None:
            num = l2.val + cry
            cry = num // 10
            num %= 10
            temp.next = self.addTwoNumbers(num, None)
            temp = temp.next
            l2 = l2.next

        while cry != 0:
            temp.next = self.addTwoNumbers(cry % 10, None)
            cry //= 10

        return new_list
