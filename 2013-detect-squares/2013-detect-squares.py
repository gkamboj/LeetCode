class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.xpoints = defaultdict(set)
        self.ypoints = defaultdict(set)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1
        self.xpoints[point[0]].add(point[1])
        self.ypoints[point[1]].add(point[0])

    def count(self, point: List[int]) -> int:
        ans, in_x, in_y = 0, point[0], point[1]
        for y in self.xpoints[in_x]:
            for x in self.ypoints[in_y]:
                if x != in_x and y != in_y and abs(x - in_x) == abs(y - in_y):
                    ans += (self.points[(x, y)] * self.points[(x, in_y)] * self.points[(in_x, y)])
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# Approach: Maintain a dict to count number of occurences of points and dicts to store y coordinates
# corresponding to an x as well as x coordinates corresponding to a y. Check all combinations from
# the last 2 dicts and add to answer.
# NOTE: Add to answer only if it's square (that is ignore rectangles) and input points is different
# from current point (to ignore zero area squares).