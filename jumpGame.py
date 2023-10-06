# https://leetcode.com/problems/jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = [False]*n
        reachable[0] = True
        for i in range(1, n):
            for j in reversed(range(i)):
                if reachable[j] and nums[j] + j >= i:
                    reachable[i] = True
                    break
        return reachable[n-1]