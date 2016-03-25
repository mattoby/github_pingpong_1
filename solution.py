class Solution(object):
    def isAdditiveNumber(self, nums):
        """
        :type num: str
        :rtype: bool
        """
        if not nums or len(nums) <= 2:
            return False
        # nums = int(nums)
        n = len(nums)
        i = 0
        j = 0
        prev = int(nums[0])
        
        '''
            Hold a pointer to the last time we found a valid additive sum
        '''
        for k in xrange(1, n):
            if k < n-1 and  int(nums[k]) + prev == int(nums[k+1]):
                prev = int(nums[k])
                print prev, nums[k], nums[k+1]
            else:
                return False
        return True
        
        