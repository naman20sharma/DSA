class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr_sum = 0, 0
        n = len(nums)
        min_length = n + 1

        for r in (range(n)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_length = min(r - l + 1, min_length)
                curr_sum -= nums[l]
                l += 1
        return 0 if min_length == n + 1 else min_length

        