class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        medium=1
        for i in range(1,len(nums)):
            for k in range(0,i):
                if nums[k]==nums[i]:
                    nums[i]=-1
                    break
                else:
                    if nums[k]==-1 :
                        nums[medium]=nums[i]
                        if medium!=i : nums[i]=-1
                        medium+=1
                        break
                    else:
                        if i == k+1:
                            medium+=1
        print 'nums:'
        print nums
        print 'medium'
        print medium
        return nums[:medium]

print Solution().removeDuplicates([1])
