from queue import Queue
import heapq
from Graph import *

import numpy as np

####Priority Queue Implementation---------------------

pq = []                                 #list of entities arranged in a heap
entry_finder = {}                       #Mapping of tasks to entries
removed = '<removed-tak>'               #Placeholder for a removed task
counter = iter.count()                  #Unique Sequence count


def add_task(task, priority=0):          #Add a new task or update the priority of an Existing one
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq,entry)

def remove_task(task):                   #Mark existing task as removed and raise error if not found.
    entry = entry_finder.pop(task)
    entry[-1] = removed

def pop_task():                          #Remove and return the lowest priority task and raise error if empty.
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not removed:
            del entry_finder[task]
            return task
    raise  KeyError('pop from an empty priority queue')

