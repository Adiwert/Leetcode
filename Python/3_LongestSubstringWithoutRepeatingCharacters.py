class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 0       # Sliding window technique by assigning two pointers from the left and right side
        result = 0      # Holding the maximum length found
        count = set()   # 'count' is a set that stores characters from the current substring (to ensure no duplicates)
        while right < len(s):                       # Right pointer moves through the string until it reaches the end of the string
            while s[right] in count:                # While the character at s[right] is already in the set 'count'
                count.remove(s[left])
                left += 1                           # Characters are removed from the left and the left pointer is incremented, until all duplicate character is removed
            count.add(s[right])                     # If no repeating characters in set 'count', the current character (s[right]) will be added
            right += 1                              # Move the right pointer to next character
            result = max(result, right - left)      # Calculate length of the current valid substring (right - left) and update result with the maximum length found so far
        return result