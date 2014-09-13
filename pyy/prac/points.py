# Definition for a point

class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        maxi = -1
        
        if len(points) ==0: return 0
        if len(points) ==1: return 1

        def slope(p1,p2):
            if p1.x == p2.x: return 1
            return ((p1.y-p2.y)/(p1.x-p2.x))
        
        def same(p1,p2):
             return p1.x == p2.x and p1.y == p2.y

        for _p1,p1 in enumerate(points):
            slopes = []
            sam = 1
            for p2 in points[:_p1]+points[_p1+1:]:
                if same(p1,p2): sam += 1
                slopes.append(slope(p1,p2))
            counts = []+[sam]
            for s in set(slopes):
                counts.append(slopes.count(s))
            m = max(counts+[-1])
            maxi = m if m > maxi else maxi
        return maxi

s = Solution()
print s.maxPoints([Point(0,0),Point(0,0)])
