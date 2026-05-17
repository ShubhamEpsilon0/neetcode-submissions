from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweetCounter = 0
        self.userTweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCounter += 1
        self.userTweets[userId].insert(0, (self.tweetCounter, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweetLists = [self.userTweets[userId]]
        for following in self.following[userId]:
            allTweetLists.append(self.userTweets[following])

        heap = []

        for tweetListIndex, userTweets in enumerate(allTweetLists):
            if len(userTweets):
                tweetToAdd = userTweets[0]
                heapq.heappush(heap, (-tweetToAdd[0], tweetToAdd[1], (tweetListIndex, 1)))

        picked = 0
        feed = []
        while heap and picked != 10:
            _, tweet, (tweetListIndex, nextTweetIndex) = heapq.heappop(heap)

            feed.append(tweet)
            picked += 1
            if len(allTweetLists[tweetListIndex]) > nextTweetIndex:
                tweetToAdd = allTweetLists[tweetListIndex][nextTweetIndex]
                heapq.heappush(heap, (-tweetToAdd[0], tweetToAdd[1], (tweetListIndex, nextTweetIndex + 1)))

        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
