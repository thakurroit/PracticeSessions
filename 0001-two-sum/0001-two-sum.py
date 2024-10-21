class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in check.keys():
                return[check[diff], i]
            else:
                check[nums[i]] = i


        return -1 

        