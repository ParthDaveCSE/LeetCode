class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for x in arr:
            if x + 1 in arr:
                count += 1
        return count


# Note that we could also do this as a one-liner generator comprehension.
# return sum(1 for x in arr if x + 1 in arr)