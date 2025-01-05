# sliding window problemb

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        logest_length = 0
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            window_size = (r - l) + 1
            logest_length = max(logest_length, window_size)
            sett.add(s[r])

        return logest_length

if __name__ =="__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))