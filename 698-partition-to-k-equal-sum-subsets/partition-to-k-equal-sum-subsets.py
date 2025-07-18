class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        target = total // k

        if total % k != 0:
            return False

        nums.sort(reverse=True)
        taken = ['0'] * n

        memo = {}
        def backtracking(curIndex, curSides, curSum):
            if curSides == k - 1:
                return True

            if curSum > target:
                return False

            if curSum == target:
                return backtracking(0, curSides + 1, 0)

            if (curIndex, curSides, curSum, ''.join(taken)) in memo:
                return memo[(curIndex, curSides, curSum, ''.join(taken))]

            for i in range(n):
                if taken[i] == '1':
                    continue

                taken[i] = '1'

                b = backtracking(i + 1, curSides, curSum + nums[i])

                taken[i] = '0'
                if b:
                    memo[(curIndex, curSides, curSum, ''.join(taken))] = True
                    return True

            memo[(curIndex, curSides, curSum, ''.join(taken))] = False
            return False

        return backtracking(0, 0, 0)
        