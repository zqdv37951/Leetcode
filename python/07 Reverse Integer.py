class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        try:
            a = int(s[0])
            an = int(s[::-1])
            if (-2**31) > an or an > (2**31 - 1):
                return 0
            else:
                return an
        except:
            s = s[1:]
            an = 1 - int(s[::-1]) -1
            if (-2**31) > an or an > (2**31 - 1):
                return 0
            else:
                return an


c = Solution()
print(c.reverse(-123))