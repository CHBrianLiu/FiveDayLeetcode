class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if s == 0:
            return 1

        if sum(nums) < s:
            return 0

        start, end = 0, 0
        min_subarray = len(nums)

        total = nums[start]
        while start < len(nums) and end < len(nums):

            # The sum of subarray has reached target.
            # Narrow the subarray by moving 'start'.
            if total >= s:
                if end - start + 1 < min_subarray:
                    min_subarray = end - start + 1
                if start < end:
                    total -= nums[start]
                    start += 1
                else:
                    start += 1
                    end += 1
                    if end < len(nums):
                        total = nums[end]
                    else:
                        break
            # The sum of subarray hasn't reached target.
            # Expand the subarray by moving 'end'.
            else:
                end += 1
                if end < len(nums):
                    total += nums[end]
                else:
                    # reach the last digit.
                    break

        return min_subarray


if __name__ == "__main__":
    runner = Solution()
    s = 100
    nums = [2, 3, 1, 2, 4, 100]
    print(runner.minSubArrayLen(s, nums))
