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
        # print("points: ", self.points, " ,\nxpoints: ", self.xpoints, " ,\nypoints: ", self.ypoints, "\n\n")
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