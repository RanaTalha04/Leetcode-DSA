class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not str:
            return ""

        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for other_words in strs[1:]:

                if i == len(other_words) or other_words[i] != char:
                    return first_word[:i]

        return first_word
                
