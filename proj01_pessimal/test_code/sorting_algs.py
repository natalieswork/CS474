import random

def is_sorted(arr: list) -> bool:
    """Check if the given list is sorted."""
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def bozosort(lst: list) -> list:    
    while not is_sorted(lst):
        index1 = random.randint(0, len(lst) - 1)
        index2 = random.randint(0, len(lst) - 1)
        lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

def sleepsort(lst: list) -> list:
    """Docstring"""
    # natalie write code here
    return lst

def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
