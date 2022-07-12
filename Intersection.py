from asyncio.windows_events import NULL
from types import NoneType


def solution(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return x
    
    return "No Intersection"

list1 = [item for item in input().split()]
list2 = [item for item in input().split()]

print(solution(list1, list2))