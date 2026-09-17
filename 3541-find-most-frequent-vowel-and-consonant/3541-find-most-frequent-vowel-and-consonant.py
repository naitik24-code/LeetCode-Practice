class Solution(object):
    def maxFreqSum(self, s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        vowels="aeiou"
        max_vowels=0
        max_consonant=0
        for ch in freq:
            if ch in vowels:
                max_vowels=max(max_vowels,freq[ch])
            else:
                max_consonant=max(max_consonant,freq[ch])
        return max_vowels+max_consonant

        