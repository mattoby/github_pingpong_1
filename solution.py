class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not nums or len(nums) <= 3:
            return False
        
        