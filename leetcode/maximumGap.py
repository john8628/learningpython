# -*- coding: utf-8 -*-

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""

class Solution(object):

    def __init__(self,nums):
        self.nums = nums

    """
    bubble sort：
    time:n*n;
    space:n

    """

    def simpleMaxGap(self):
        nums = self.nums
        max = nums[0]
        newNum = []

        for index in range(0,len(nums)-1):
            for index2 in range(0,len(nums)-1):
                if nums[index2] > nums[index2+1]:
                    temp = nums[index2]
                    nums[index2] = nums[index2+1]
                    nums[index2+1] = temp
            #print nums
        return nums

    def biggap(self,sortedNums):
        #sortedNums =nums
        print len(sortedNums)
        if len(sortedNums) < 2:
            return
        maxgap = sortedNums[1]-sortedNums[0]
        if len(sortedNums) ==2:
            return sortedNums[1]-sortedNums[0]

        for i in range(0,len(sortedNums)-1):
            if (sortedNums[i+1]-sortedNums[i])>=maxgap:
                maxgap = sortedNums[i+1]-sortedNums[i]
        return maxgap

solution = Solution([4,2,3,0,899,0,8,7,6,4,2])
#print solution.nums
list = solution.simpleMaxGap()

print solution.biggap(list)
#//solution.simpleMaxGap(solution)