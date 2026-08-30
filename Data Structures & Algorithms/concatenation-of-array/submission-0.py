class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_2 = nums.copy()
        result = list(nums + nums_2)
        return result
        