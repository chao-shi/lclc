class Solution(object):
    def largestPalindrome(self, n):
        if n==1: return 9
        if n==2: return 987
        for a in xrange(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337

# I used the following approach. Let's denote the biggest palindrome product as palindrome = M * L. For N > 1 this palidrome has even number of digits and it can be represented as the sum:
# palindrome = upper * 10^N + lower
# We can expect that M and L are close to 10^N and we can represent them as M = 10^N - i, L = 10^N - j and hence
# palindrome = (10^N - i) * (10^N - j) = 10^N * (10^N - (i + j)) + i * j
# If we assume that i * j < 10^N (this assumption turned out to be true for N > 1) we can represent upper and lower in the following way:
# upper = 10^N - (i + j)
# lower = i * j
# This is the system of equations which can be solved if we know upper and lower. Let's denote sum of i and j as a = i + j. It can be calculated as a = 10^N - upper. Because j = a - i equation for lower can be rewritten as
# lower = a * i - i * i
# This is a quadratic equation which can be solved using standard methods from textbooks.

# if n == 1:
#     return 9

# for a in xrange(2, 9 * 10**(n-1)):
#     upper = 10**n - a
#     lower = reverseNumber(upper)
#     # solve the equation 
#     # lower == a * i - i * i
#     # if it has whole number solution then
#     #     return (10**n - i) * (10**n - j) % 1337