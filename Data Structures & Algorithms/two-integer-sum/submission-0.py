class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            currentnum = nums[i]
            complement = target - currentnum
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


            
            
                




            
            

       
            
            