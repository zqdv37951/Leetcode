
from tracemalloc import start
from webbrowser import get


class Solution:
    def longestPalindromeRETURNint(self, s: str) -> str:
        ls = [[0]*len(s) for i in range(len(s))]
        print(len(s))
        for j in range(0,len(s)):
            print("j",j)
            for i in range(0,j+1):
                print("i",i)
                if i == j: 
                    ls[j][i]=1
                    print(ls)
                if (i+1 < len(s)) & (j-1 >=0):
                    print("TTT")
                    if (s[i]==s[j])&(ls[j-1][i+1]!=0):ls[j][i]=ls[j-1][i+1]+2
                    print(j,i,ls[j][i])
                print(j,i)
                
        return()
    def longestPalindrome(self, s: str) -> str:
        def getLen(l,r):
            while l >=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r -l -1
        length = 0
        start = 0
        for i in range(len(s)):
            cur = max(getLen(i,i),getLen(i,i+1))
            if cur <= length:continue
            length = cur
            start = i - (cur-1)//2
        return s[start:start+length]
c = Solution()
print(c.longestPalindrome("abaab"))