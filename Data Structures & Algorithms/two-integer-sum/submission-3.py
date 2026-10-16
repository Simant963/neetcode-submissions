class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        if len(nums)==2:
            if nums[0]+nums[-1]==target:
                return [0,1]
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]