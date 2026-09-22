class Solution:
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        count = 0
        maximum = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1

            if i >= k:
                if s[i - k] in vowels:
                    count -= 1

            if i >= k - 1:
                maximum = max(maximum, count)

        return maximum