# Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.

# Implement the Solution class:

#     Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius and the position of the center (x_center, y_center).
#     randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array [x, y].

 

# Example 1:

# Input
# ["Solution", "randPoint", "randPoint", "randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# Output
# [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

# Explanation
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint(); // return [-0.02493, -0.38077]
# solution.randPoint(); // return [0.82314, 0.38945]
# solution.randPoint(); // return [0.36572, 0.17248]

import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x0 = x_center
        self.y0 = y_center

    # Polar coordinates
    def randPoint(self):
        pi = 3.14
        theta = random.uniform(0, 2 * pi)
        A = random.uniform(0, 3.14 * self.r * self.r)
        R= math.sqrt(A/pi)
        return [self.x0 + math.cos(theta) * R, self.y0 + math.sin(theta) * R]
    # The idea is very simple, that is to take the smallest square that can hold the
    # circle, and randomly generate the points in the square. 
    # If the point is not inside the circle, continue to 
    # regenerate. The random points with equal probability in 
    # the square can be generated easily by using the built-in 
    # random number generator
    def randPointRejectionSampling(self):
        x0 = self.x0 - self.r
        y0 = self.y0 - self.r
        while(True):
            xg = x0 + random.random() * self.r * 2
            yg = y0 + random.random() * self.r * 2
            if (math.pow((xg - self.x0) , 2) + math.pow((yg - self.y0), 2) <= self.r * self.r):
                return [xg, yg]
    
# Your Solution object will be instantiated and called as such:
obj = Solution(5, 5, 5)
param_1 = obj.randPointRejectionSampling()
print(param_1)