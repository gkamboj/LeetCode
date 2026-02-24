import heapq as h

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) 
        self.following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append([-self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId}.union(self.following[userId])
        feed_tweets = []
        # print(users)
        for user in users:
            feed_tweets += list(self.tweets[user])
        h.heapify(feed_tweets)
        feed = []
        while len(feed) != 10 and feed_tweets:
            feed.append(h.heappop(feed_tweets)[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)