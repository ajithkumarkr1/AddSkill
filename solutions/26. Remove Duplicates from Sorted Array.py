class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):           
            if i+1 == len(nums):
                    break
            if nums[i] == nums[i+1]:
                del nums[i+1]
                i = i - 1
            i = i + 1
                           
        return len(nums)
