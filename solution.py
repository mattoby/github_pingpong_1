class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not nums or len(nums) <= 2:
            return False
        
        n = len(nums)
        i = 0
        j = 0
        
        '''
            Hold a pointer to the last time we found a valid additive sum
        '''
        for k in xrange(n):
            
        
        