import heapq as h

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) 
        self.following = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        user_tweets = self.tweets[userId]
        user_tweets.append([-self.count, tweetId])
        if len(user_tweets) > 10:
            user_tweets.pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId}.union(self.following[userId])
        feed_tweets = []
        for user in users:
            user_tweets = self.tweets[user]
            if user_tweets:
                count, tweet_id = user_tweets[-1]
                ind = len(user_tweets) - 1
                if len(feed_tweets) == 10:
                    h.heappop(feed_tweets)
                h.heappush(feed_tweets, [count, tweet_id, user, ind - 1])

        feed = []
        while len(feed) != 10 and feed_tweets:
            _, tweet_id, user, ind = h.heappop(feed_tweets)
            feed.append(tweet_id)
            if ind >= 0:
                count, tweet_id = self.tweets[user][ind]
                h.heappush(feed_tweets, [count, tweet_id, user, ind - 1])

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

# Approach: Everything other than getNewsFeed and postTweet is self-explanatory.
# For postTweet, append count as well as tweet_id to tweets array maintained for every user. count is needed to know the insertion order.
# For getNewsFeed, we have k ordered arrays (ordered by tweet posting order). Take the most recently posted tweet from each of them and
# create max heap (using -1 * count as key). Store user id and index of current tweet also in heap to add subsequent value if current tweet is
# removed from heap.
# Refer NC video solution for detail: https://youtu.be/pNichitDD2E