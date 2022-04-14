# Given an integer A, which denotes the number of doors in a row numbered 1 to A. All the doors are closed initially.
# A person moves to and fro, changing the states of the doors as follows: the person opens a door that is already
# closed and closes a door that is already opened.
# In the first go, he/she alters the states of doors numbered 1, 2, 3, … , A.
# In the second go, he/she alters the states of doors numbered 2, 4, 6 ….
# In the third go, he/she alters the states of doors numbered 3, 6, 9 …
# This continues till the A'th go in, which you alter the state of the door numbered A.
# Find and return the number of open doors at the end of the procedure.

def numberOfOpenDoors(n):
    return int(n ** 0.5)


print(numberOfOpenDoors(6))

# Approach: Observe that the kth door condition will be changed is the number of factors of k. Also, except for
# perfect squares, factors always occur in pair (for rg., 12 = 1 * 12 = 2 * 6 = 3 * 4) i.e. every number except
# perfect squares will always have even number of factors. If the door condition is changed even number of times,
# its final condition will be same as initial condition i.e. closed. So, only those doors which are numbered perfect
# square numbers will be opened at end as perfect squares have odd number of factors.

# PS: Number of perfect squares less than or equal to n = int(sqrt(n)).
