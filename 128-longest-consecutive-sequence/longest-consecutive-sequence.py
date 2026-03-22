class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums.sort()

        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                curr_len = 1
            
            if curr_len > max_len:
                max_len = curr_len

        return max_len
            
        