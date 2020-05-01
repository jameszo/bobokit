#!/usr/bin/env python3

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, iterm, priority):
        heapq.heappush(self._queue, (-priority, self._index, iterm))
        self._index++

    def pop(self):
        return heapq.heappop(self._queue)[-1]
