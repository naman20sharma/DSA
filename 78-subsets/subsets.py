class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # start with empty set
        for num in nums:
            # For each num, add it to all existing subsets
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result.extend(new_subsets)
        return result
        