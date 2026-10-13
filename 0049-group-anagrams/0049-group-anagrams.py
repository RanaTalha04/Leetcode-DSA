class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}

        for word in strs:
            key = " ".join(sorted(word))

            if key not in result:
                result[key] = []
            
            result[key].append(word)

        return list(result.values())