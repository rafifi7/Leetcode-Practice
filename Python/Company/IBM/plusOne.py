from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # so idea is to iterate backwards through the digits array
        # if the left most isn't a 9 we can simply change that to + 1

        # if it is a 9 we want to continue iterating backwards until the next one is not a 9
        added = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                added = True
                break
            else:
                digits[i] = 0
        if not added:
            digits.insert(0, 1)

        return digits