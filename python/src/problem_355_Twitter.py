# https://leetcode.com/problems/design-twitter

from __future__ import annotations

import heapq
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Set

# Type stubs
UserId = int
TweetId = int


@dataclass
class Tweet:
    time: datetime
    id: TweetId

    def __lt__(self, other: Tweet):
        return self.time < other.time


class Twitter:
    def __init__(self):
        self._feed_size: int = 10
        self._tweets: Dict[UserId, List[Tweet]] = defaultdict(list)
        self._follows: Dict[UserId, Set[UserId]] = defaultdict(set)

    def postTweet(self, userId: UserId, tweetId: TweetId) -> None:
        tweet = Tweet(datetime.now(), tweetId)
        self._tweets[userId].append(tweet)

    def getNewsFeed(self, userId: UserId) -> List[TweetId]:
        def helper(userId: UserId) -> Iterable[Tweet]:
            user = userId
            for tweet in self._tweets[user][-self._feed_size :]:
                yield tweet

            for user in self._follows[userId]:
                for tweet in self._tweets[user][-self._feed_size :]:
                    yield tweet

        return [tweet.id for tweet in heapq.nlargest(self._feed_size, helper(userId))]

    def follow(self, followerId: UserId, followeeId: UserId) -> None:
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: UserId, followeeId: UserId) -> None:
        self._follows[followerId].discard(followeeId)
