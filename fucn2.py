class Solution(object):
    def twoSum(self, nums, target):
       sum = 0
       sum_list = []
       for i, value in enumerate(nums):
            if i > (len(nums)-1):
              sum = nums[i] + nums[i+1] 
              if sum == target:
                 sum_list.extend([i,i+1])
                 return sum_list