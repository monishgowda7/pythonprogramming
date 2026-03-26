class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # v=sum(digits)
        # m=v+1
        num=int("".join(map(str ,digits)))
        num=num+1
        return list(map(int,str(num)))