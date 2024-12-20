class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else: 
                hi = mid - 1
        
        return -1
