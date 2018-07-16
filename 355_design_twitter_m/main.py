class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fm = {}
        self.tweets = {}
        # I though twitter ID was ordered by timestamp, but it isn't
        self.ts_tid = {}
        self.ts = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets.setdefault(userId, []).append(self.ts)
        self.ts_tid[self.ts] = tweetId
        self.ts += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        h = []
        users = self.fm.get(userId, set())
        users.add(userId)
    
        for user in users:
            ts = self.tweets.get(user, [])
            if ts:
                heapq.heappush(h, (-ts[-1], user, -1))
        
        res = []
        while len(res) < 10 and h:
            ts, user, ptr = heapq.heappop(h)
            res.append(self.ts_tid[-ts])
            
            if ptr - 1 >= -len(self.tweets[user]):
                ptr -= 1
                heapq.heappush(h, (-self.tweets[user][ptr], user, ptr))
        return res
            

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.fm.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.fm:
            if followeeId in self.fm[followerId]:
                self.fm[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Test case
# ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
# [[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]