
from curses.ascii import SP


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index1,index2 = 0,1
        while(True):
            if nums[index1]==nums[index2]:
                nums.pop(index2)
            else:
                index1+=1;index2+=1
            if index2 == len(nums): break
        return len(nums)


c = Solution()
print(c.removeDuplicates([1,5,7,7,8]))