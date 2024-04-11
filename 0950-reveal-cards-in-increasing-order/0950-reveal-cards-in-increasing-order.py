class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque([i for i in range(n)])
        result = [0]*n
        deck.sort()
        for card in deck:
            result[queue.popleft()] = card
            if queue: queue.append(queue.popleft())
        return result
    
'''Approach: Maintain a queue of indices to know the current index to be filled. After every filled index, 
move the next index to the end of queue (as is the condition of question). Refer approach-2 of official
solution for more detail.
'''