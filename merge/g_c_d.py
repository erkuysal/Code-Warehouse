class Solution(object):
    def greatest_common_divider(self, str1, str2):
        # Calculate the greatest common divisor of two values.
        """
            def gcd(x, y):
                iterator = 0
                value1 = x
                value2 = y
                print(f'Initial Values < X: {x} | Y:{y} >')
                while y:
                    x, y = y, x % y
                    print(f'Iteration {iterator} < X: {x} | Y:{y} >')
                    iterator += 1
                return f'Greatest Common Divider of {value1} and {value2} is {x}'
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Check if the concatenation property holds
        if str1 + str2 != str2 + str1:
            return ""

        # Calculate the greatest common divisor of the lengths
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]


str1 = "ABCABCABC"
str2 = "ABC"

greatest_common_divider = Solution().greatest_common_divider(str1, str2)
print(greatest_common_divider)