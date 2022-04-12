# There are N players, each with strength A[i]. when player i attack player j, player j strength reduces to max(0,
# A[j]-A[i]). When a player's strength reaches zero, it loses the game, and the game continues in the same manner
# among other players until only 1 survivor remains.

def pubg(arr):
    ans = arr[0]
    for num in arr[1:]:
        ans = gcd(ans, num)
    return ans


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(pubg([8, 4, 28, 12, 2, 92, 12, 8, 14]))

# Approach: Since we want to minimise the strength of last player, we should always try that player with more
# strength attacks a player with lower strength. Had this been the other way round (that is player with lesser strength
# attacking player with more strength), we'd always be ending with maximum strength as our answer. Now,
# coming to approach, consider the case when there are only 2 players: a and b. If player with more strength keeps
# attacking the player with lower strength, we'll get HCF(a, b) as the strength at the end. Extending this to array
# of n players, answer should be the HCF of whole array.
