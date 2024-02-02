import random
import time

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition_standard(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition_standard(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_tukeys_ninther(arr, low, high):
    if low < high:
        pivot_index = partition_tukeys(arr, low, high)
        quicksort_tukeys_ninther(arr, low, pivot_index - 1)
        quicksort_tukeys_ninther(arr, pivot_index + 1, high)

def partition_tukeys(arr, low, high):
    if high - low > 8: # Use Tukey's Ninther if enough elements
        pivot_index = tukeys_ninther(arr, low, high)
    else:
        pivot_index = high
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition_standard(arr, low, high)

def tukeys_ninther(arr, low, high):
    step = (high - low + 1) // 9
    mid1 = median_of_three(arr, low, low + step, low + 2 * step)
    mid2 = median_of_three(arr, low + 3 * step, low + 4 * step, low + 5 * step)
    mid3 = median_of_three(arr, low + 6 * step, low + 7 * step, high - step)
    return median_of_three(arr, mid1, mid2, mid3)

def median_of_three(arr, i, j, k):
    if arr[i] > arr[j]:
        i, j = j, i
    if arr[i] > arr[k]:
        i, k = k, i
    if arr[j] > arr[k]:
        j, k = k, j
    return j

def generate_random_array(n, range_min, range_max):
    return [random.randint(range_min, range_max) for _ in range(n)]

def performance_test(sort_function, arr, name):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.time()
    print(f"{name} took {end_time - start_time:.6f} seconds.")

# 测试参数
N = 128000
MIN_VAL = 0
MAX_VAL = 100000
test_data_standard = generate_random_array(N, MIN_VAL, MAX_VAL)
test_data_tukeys = test_data_standard.copy()

# 性能测试
performance_test(quicksort, test_data_standard, "Standard Quick Sort")
performance_test(quicksort_tukeys_ninther, test_data_tukeys, "Tukey's Ninther Quick Sort")
