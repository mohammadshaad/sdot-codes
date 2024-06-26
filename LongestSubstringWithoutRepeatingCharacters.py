class Solution:
    def longestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[r] = chars.get(r, 0) + 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1

        return res
    
if __name__=="__main__":
    s = input()
    obj = Solution()
    ans = obj.longestSubstring(s)
    print(ans)