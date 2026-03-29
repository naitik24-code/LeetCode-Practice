class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        # Step 1: Check valid pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Custom GCD function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_len = gcd(len(str1), len(str2))
        
        # Step 3: Return result
        return str1[:gcd_len]