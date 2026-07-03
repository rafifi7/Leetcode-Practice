class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: # type: ignore
        # O(n) solution

        # list should contain all numbers 1 - n
        # use a hashset to keep track of what we have already seen

        seen = set()
        for num in nums:
            seen.add(num)
        
        # loop from 1 - n
        ret = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                ret.append(i)

        return ret
