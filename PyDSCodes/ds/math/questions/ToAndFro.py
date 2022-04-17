# The Guardians of the Galaxy have just landed on Earth. There are N cities in a row numbered from 1 to N. The cost
# of going from a city with number i to a city with number j is the remainder when (i+j) is divided by (n+1). The
# Guardians want to visit every city but in the minimum cost. What is the minimum cost that will be incurred?

def toAndFro(n):
    return int((n - 1) // 2)


print(toAndFro(6))
print(toAndFro(7))

# Approach: Minimum cost will occur when we try to have as many as possible paths with sum of city numbers equal to (
# n + 1). This can be done as: 1 -> n, 2 -> (n - 1), 3 -> (n - 2).... All these paths will have zero cost as
# remainder will be zero. Only cost incurred will be to go from current city to adjacent of previous city which will
# be 1: n -> 2 [cost = (n + 2) % (n + 1) = 1], (n - 1) -> 3, .... Such paths with one cost will be equal to half of (
# n - 1) and hence the answer.
