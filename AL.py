import random
import time

# Step 1: Create 500 random integers between 1 and 10000
numbers = [random.randint(1, 10000) for _ in range(500)]

# ---------------- Sorting Algorithms ---------------- #

def selection_sort(lst):
    """Selection sort algorithm"""
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def merge_sort(lst):
    """Merge sort algorithm"""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted lists"""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# ---------------- Searching Algorithms ---------------- #

def simple_search(lst, item):
    """Linear Search"""
    for idx, value in enumerate(lst):
        if value == item:
            return idx
    return -1

def binary_search(lst, item):
    """Binary Search"""
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ---------------- Comparisons ---------------- #

# Sorting comparison
sel_data = numbers.copy()
merge_data = numbers.copy()

start_time = time.perf_counter()
selection_sort(sel_data)
sel_sort_time = time.perf_counter() - start_time

start_time = time.perf_counter()
merge_sort(merge_data)
merge_sort_time = time.perf_counter() - start_time

print("===== Sorting Algorithm Comparison =====")
print(f"Selection Sort: {sel_sort_time:.6f} seconds")
print(f"Merge Sort    : {merge_sort_time:.6f} seconds")

# Searching comparison
target_value = random.choice(numbers)

start_time = time.perf_counter()
simple_search(numbers, target_value)
linear_time = time.perf_counter() - start_time

sorted_numbers = sorted(numbers)
start_time = time.perf_counter()
binary_search(sorted_numbers, target_value)
binary_time = time.perf_counter() - start_time

print("\n===== Searching Algorithm Comparison =====")
print(f"Target Value : {target_value}")
print(f"Linear Search: {linear_time:.10f} seconds")
print(f"Binary Search: {binary_time:.10f} seconds")
