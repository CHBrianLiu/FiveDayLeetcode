import copy


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def is_achieved_requirement(requirement, now_have):
            for key in requirement.keys():
                if now_have[key] < requirement[key]:
                    return False
            return True

        if len(s) == 0 or len(t) == 0:
            return ""

        # Create a dictionary to track.
        letter_required = {letter: 0 for letter in t}
        letter_statistics = {}
        for letter in t:
            letter_required[letter] += 1
            letter_statistics[letter] = 0

        ans_found = False
        start = 0
        end = 0
        min_substring = copy.deepcopy(s)

        if s[start] in letter_statistics.keys():
            letter_statistics[s[start]] += 1

        while start < len(s) and end < len(s):
            # Haven't achieved the goal. Expand the window.
            if not is_achieved_requirement(letter_required, letter_statistics):
                end += 1
                # Not exceed the string range.
                if end < len(s):
                    if s[end] in letter_statistics.keys():
                        letter_statistics[s[end]] += 1
            # Narrow the window.
            else:
                # Because there's only one unique answer, 1 is minimum length.
                if start == end:
                    return s[start]

                # If the length of substring is minimum, store the substring.
                if end - start + 1 <= len(min_substring):
                    ans_found = True
                    min_substring = s[start:end+1]

                if s[start] in letter_statistics.keys():
                    letter_statistics[s[start]] -= 1
                start += 1

        if ans_found:
            return min_substring
        else:
            return ""


if __name__ == "__main__":
    runner = Solution()
    full_string = "AA"
    target_string = "AAA"
    print(runner.minWindow(full_string, target_string))
