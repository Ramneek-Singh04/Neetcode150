#This solution is incorrect since it is O(n^2), .index scans the entire list to find the index, which is why this would not work


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            key = target - num
            if key in nums_dict:
                return_list = []
                return_list.append(nums_dict[key])
                return_list.append(nums.index(num))
                return return_list
            nums_dict[num] = nums.index(num)


#if we did this without using .index we can get this solution, which IS in O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in nums_dict:
                return_list = []
                return_list.append(nums_dict[key])
                return_list.append(i)
                return return_list
            nums_dict[nums[i]] = i
