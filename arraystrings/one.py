#find the closest number to zero

class Solution:
    def findclosestnumber(self, nums:list[int])-> int:
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest):
            return abs(closest)
        else:
            return closest
        