import copy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0 or target == 0:
            return []

        candidates.sort()
        self.ans = []

        self.try_combination(target, candidates, [])

        return self.ans

    def try_combination(
            self, remainds, availables, previous_combination):

        for index in xrange(len(availables)):
            current_combination = copy.deepcopy(previous_combination)
            current_combination.append(availables[index])

            if remainds > availables[index]:
                self.try_combination(remainds - availables[index],
                                     availables[index:],
                                     current_combination)
            elif remainds == availables[index]:
                self.ans.append(current_combination)
                return
            else:
                return


if __name__ == "__main__":
    runner = Solution()
    candidates = [1, 2]
    target = 1
    print(runner.combinationSum(candidates, target))
