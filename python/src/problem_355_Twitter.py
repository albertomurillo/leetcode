# https://leetcode.com/problems/design-twitter

from __future__ import annotations

import heapq
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

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
        self._tweets: dict[UserId, list[Tweet]] = defaultdict(list)
        self._follows: dict[UserId, set[UserId]] = defaultdict(set)

    def postTweet(self, userId: UserId, tweetId: TweetId) -> None:
        tweet = Tweet(datetime.now(tz=UTC), tweetId)
        self._tweets[userId].append(tweet)

    def getNewsFeed(self, userId: UserId) -> list[TweetId]:
        def helper(userId: UserId) -> Iterable[Tweet]:
            user = userId
            yield from self._tweets[user][-self._feed_size :]

            for user in self._follows[userId]:
                yield from self._tweets[user][-self._feed_size :]

        return [tweet.id for tweet in heapq.nlargest(self._feed_size, helper(userId))]

    def follow(self, followerId: UserId, followeeId: UserId) -> None:
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: UserId, followeeId: UserId) -> None:
        self._follows[followerId].discard(followeeId)
