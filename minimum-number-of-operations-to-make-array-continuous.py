# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous

import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = sys.maxsize
        for i in range(len(nums)):
            target = nums[i] + (n-1)
            idx = bisect.bisect_right(nums, target)
            ans = min(ans, n-(idx-i))
        return ans