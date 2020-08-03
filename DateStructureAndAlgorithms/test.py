class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            # dic[num] = i
            # for j in dic:
            if dic.get(target - num):
                return [i, dic[target - num]]
            else:dic[num] = i


soulution = Solution()
ret = soulution.twoSum([2, 5, 4, 7, 6], 10)
print(ret)
def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
