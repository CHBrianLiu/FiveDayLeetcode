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

        start, end = 0, 1
        min_subarray = len(nums)

        while start < len(nums) and end <= len(nums):
            total = sum(nums[start:end])
            # The sum of subarray has reached target.
            # Narrow the subarray by moving 'start'.
            if total >= s:
                if end - start < min_subarray:
                    min_subarray = end - start
                if start < end:
                    start += 1
                else:
                    start += 1
                    end += 1
            # The sum of subarray hasn't reached target.
            # Expand the subarray by moving 'end'.
            else:
                end += 1

        return min_subarray


if __name__ == "__main__":
    runner = Solution()
    s = 100
    nums = [1, 1]
    print(runner.minSubArrayLen(s, nums))
