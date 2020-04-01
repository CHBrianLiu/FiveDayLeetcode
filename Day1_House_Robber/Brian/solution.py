class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        if nums_length == 0:
            return 0

        # Create a list for dynamic programming caching.
        dp_caching = []
        for _ in xrange(nums_length):
            dp_caching.append(-1)

        # Calculate the robbing value from the rightest element.
        for index in xrange(nums_length - 1, -1, -1):
            if nums_length - index == 1 or nums_length - index == 2:
                # The last or last 2 element. -> No choice but itself.
                dp_caching[index] = nums[index]
                continue

            # List all possible combination of first layer.
            possible_choice_value = []
            for possible_choice_index in xrange(index + 2, nums_length):
                possible_choice_value.append(
                    nums[index] + dp_caching[possible_choice_index])
            dp_caching[index] = max(possible_choice_value)

        # Return the max number in the list.
        return max(dp_caching)
