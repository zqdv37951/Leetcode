from dis import disco
import queue


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = []
        ans = 0
        if len(s) == 0: return ans
        else:
            l = 0
            for i in range(len(s)):
                while s[i] in q:
                    q.pop(0)
                    l+=1
                q.append(s[i])
                ans = max(ans,i-l+1)
        return ans

c = Solution()
print(c.lengthOfLongestSubstring('abcabcbb'))

def long(s):
    dicts ={}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value]+1
            if sums >start :
                start = sums
        num = i-start +1
        if num > maxlength :
            maxlength = num
        dicts[value] = i
def long(s):
    dicts = {}
    maxlength = start = 0
    if len(s)==0: return 0
    for index, item in enumerate(s):
        if item in dicts:
            tem = dicts[item] +1
            if tem > start: start = tem
        num = index -start +1
        if num > maxlength: maxlength = num
        dicts[item] = index
    return maxlength
    
print(long("pwwkew"))