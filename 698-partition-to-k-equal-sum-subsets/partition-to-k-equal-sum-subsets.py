class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False  # Can't divide evenly
        
        target = total_sum // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False  # Largest number can't fit into any subset
        
        buckets = [0] * k  # Track the sum in each subset group
        
        def backtrack(index):
            if index == len(nums):
                return all(bucket == target for bucket in buckets)
            
            current = nums[index]
            
            for i in range(k):
                if buckets[i] + current <= target:
                    buckets[i] += current
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= current
                
                if buckets[i] == 0:
                    break  # Optimization: avoid placing same number in identical empty buckets
            
            return False
        
        return backtrack(0)
        