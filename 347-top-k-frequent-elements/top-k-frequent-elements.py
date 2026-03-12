'''
- find the k most frequent elements
- array size up to 100k
- must be better than o(nlogn)

approach
- counting freq with hash maps
- group nums by freq bucket
- scan buckets from high to low

example:
nums = [1, 1, 1, 2, 2, 3] k = 2
1 -> 3
2 -> 2 
3 -> 1

at freq 6, 5, 4, bucket. would be empty 

at freq 3 i find [2]
res [1]

at freq 2, I find [2]
res becomes [1, 2]

nums = [1], k = 1

freq map 1 -> 1


Time: O(n)
Space: O(n) 

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, -1, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result