class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.xpoints = defaultdict(set)
        self.ypoints = defaultdict(set)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1
        self.xpoints[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        ans = 0
        in_x, in_y = point
        for y in self.xpoints[in_x]:
            side = abs(in_y - y)
            if not side:
                continue
            x1, x2 = in_x + side, in_x - side
            ans += self.points[(x1,in_y)] * self.points[(in_x,y)] * self.points[(x1,y)]
            ans += self.points[(x2,in_y)] * self.points[(in_x,y)] * self.points[(x2,y)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# Approach: Maintain a dict to count number of occurences of points and another dict to store y coordinates
# corresponding to an x. Check all combinations from the last 2 dicts and add to answer. Consider both sides
# of point as square can be on left as well as right side of input point.
# Similar approach can be done by considering y axis as base instead of x-axis. Then we would have considered
# squares above and below of input point.
# NOTE: Add to answer only input points is different from current point (to ignore zero area squares).

# Refer NC HashMap - II solution for better understanding.
