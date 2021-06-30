class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reader=0
        low=0
        high=len(nums)-1
        while reader<=high:
            if nums[reader]==0:
                nums[reader],nums[low]=nums[low],nums[reader]
                reader=reader+1
                low=low+1
            elif nums[reader]==1:
                reader=reader+1
            else:
                nums[reader],nums[high]=nums[high],nums[reader]
                high=high-1
