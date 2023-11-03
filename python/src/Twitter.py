# https://leetcode.com/problems/design-twitter

import heapq
from collections import defaultdict
from datetime import datetime
from typing import Generator, List


class Twitter:
    def __init__(self):
        self._feed_size = 10
        self._tweets = defaultdict(list)
        self._follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._tweets[userId].append((datetime.now(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        def helper(userId: int) -> Generator[int, None, None]:
            user = userId
            for tweet in self._tweets[user][-self._feed_size :]:
                yield tweet

            for user in self._follows[userId]:
                for tweet in self._tweets[user][-self._feed_size :]:
                    yield tweet

        return [tweet for _, tweet in heapq.nlargest(self._feed_size, helper(userId))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._follows[followerId].discard(followeeId)
