class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        counter = 0
        substring = ""
        maxLength = 0
        for i in range(start_index, len(s)):
            if s[i] in substring:
                # find the index
                index = substring.index(s[i])
                start_index = i + 1
                if maxLength < counter:
                    maxLength = counter
                counter = counter - index
                if index + 1 < len(substring):
                    substring = substring[index + 1 :]
                else:
                    substring = ""
                substring += s[i]
            else:
                substring += s[i]
                counter += 1
        if maxLength < counter:
            maxLength = counter
        return maxLength
