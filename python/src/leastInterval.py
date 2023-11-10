# https://leetcode.com/problems/task-scheduler

import heapq
from collections import Counter, deque
from typing import Deque, List, Tuple


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(max_heap)

        q: Deque[Tuple[int, int, str]] = deque()

        ticks = 0
        while max_heap or q:
            ticks += 1

            if q:
                # Send task to the heap if task is ready
                ready_at_ticks, count, task = q[0]
                if ready_at_ticks == ticks:
                    q.popleft()
                    heapq.heappush(max_heap, (count, task))

            if max_heap:
                # Process one of the most frequent tasks
                count, task = heapq.heappop(max_heap)
                count += 1

                # Send remaining tasks to the queue
                if count:
                    q.append((ticks + n + 1, count, task))

        return ticks
