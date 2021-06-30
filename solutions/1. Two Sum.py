class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return([0,1])
        else:
            dictComplement = {}
            for index1 in range(len(nums)):
                nComplement = target - nums[index1]
                if (nComplement in dictComplement):
                    return sorted([index1,dictComplement[nComplement]])
                else:
                    dictComplement[nums[index1]]=index1
