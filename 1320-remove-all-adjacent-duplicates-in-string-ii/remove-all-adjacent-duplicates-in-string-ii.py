class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
    
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                # If we hit the threshold n, remove the sequence
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
                
        # Build the final string from remaining counts
        return "".join(char * count for char, count in stack)