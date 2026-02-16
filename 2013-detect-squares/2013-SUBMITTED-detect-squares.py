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

# Approach: Maintain a dict to count the number of occurrences of points and another dict to store y coordinates
# corresponding to an x. Check all combinations from the last 2 dicts and add to the answer. Consider both sides
# of points as squares can be on the left as well as the right side of the input point.
# A similar approach can be done by considering y-axis as the base instead of the x-axis. Then we would have considered
# squares above and below the input point.
# NOTE: Add to answer only input points is different fromthe  current point (to ignore zero area squares).

# Refer to NC HashMap - II solution for better understanding.
