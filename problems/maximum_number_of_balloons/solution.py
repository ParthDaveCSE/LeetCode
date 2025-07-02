class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        chars = defaultdict(int)
        balloon = defaultdict(int)

        for c in word:
            balloon[c] += 1

        for c in text:
            if c in balloon:
                chars[c] += 1

        for c in chars:
            chars[c] = int(chars[c]/balloon[c])
            
        if len(chars) == 5:
            return min(chars.values())
        else:
            return 0