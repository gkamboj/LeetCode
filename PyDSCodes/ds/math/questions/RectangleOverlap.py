# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane. For the first rectangle,
# its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left
# corner is (E, F), and the top right corner is (G, H). Find and return whether the two rectangles overlap or not.

def checkRectangleOverlap(a, b, c, d, e, f, g, h):
    if c <= e or g <= a or d <= f or h <= b:
        return 0
    return 1


print(checkRectangleOverlap(0, 0, 4, 4, 2, 2, 6, 6))

# Approach: Rectangles will not overlap if highest y-coordinate of a rectangle is below lowest y-coordinate of other
# rectangle (or vice-versa). This argument holds true wrt x-coordinates also. For every other possible case,
# there'll be an overlap.
