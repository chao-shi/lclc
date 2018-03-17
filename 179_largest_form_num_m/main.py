class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(num1, num2):
            a, b = str(num1) + str(num2), str(num2) + str(num1)
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0
        nums = sorted(nums, cmp=compare)
        ans = "".join(map(str, nums))
        ans = ans.lstrip('0')
        return "0" if not ans else ans

# Test case of [0, 0]