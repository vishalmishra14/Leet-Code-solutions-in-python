class Solution:
    def maxSubArray(self, nums):
        max_c = max_g = nums[0]

        for i in range(1,len(nums)):
            max_c = max(nums[i], max_c + nums[i])

            if max_c > max_g:
                max_g = max_c
        return max_g


if __name__ == '__main__':
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-2, 3, 2, -1]
    sub = Solution()

    v = sub.maxSubArray(nums)
    print(v)

