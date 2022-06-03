class Solution(object):
    def twoSum(self, nums, target): #2, 7, 11, 15
        # sol 1
        mydic = {}
        for idx, itm in enumerate(nums):
            rest = target - itm
            if rest in mydic:
                return [mydic[rest], idx]
            else:
                mydic[itm] = idx 
        
        # sol 2
        raw_nums = nums[:]
        nums.sort()
        for i in range(0,len(nums)):
            if target - nums[i] in nums[i+1:]:
                if target - nums[i] == nums[i]:
                    # 從第一個之後開始索引 list.index(x[, start[, end]])
                    return sorted([raw_nums.index(nums[i]),raw_nums.index(nums[i],raw_nums.index(nums[i])+1)])
                    break
                else:
                    return sorted([raw_nums.index(nums[i]),raw_nums.index(target-nums[i])])
                    break

ob = Solution() 
print(ob.twoSum([4, 6, 4, 11, 15],8))
print("two sum")