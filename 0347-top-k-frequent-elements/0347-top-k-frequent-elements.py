class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        unique = list(seen.keys())
        unique.sort(key=lambda x: seen[x], reverse = True)

        return unique[:k]