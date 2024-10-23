class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 0
        result = 0
        count = set()
        while right < len(s):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            right += 1
            result = max(result, right - left)
        return result