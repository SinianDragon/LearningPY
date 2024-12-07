import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [9, 3, 6, 5, 2, 7, 8, 1]
print("冒泡排序结果:", bubble_sort(arr))
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [9, 3, 6, 5, 2, 7, 8, 1]
print("选择排序结果:", selection_sort(arr))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
arr = [9, 3, 6, 5, 2, 7, 8, 1,15]
print("归并排序结果:", merge_sort(arr))

# 随机生成1000, 10000, 100000个数字
sizes = [1000, 10000, 100000]
for size in sizes:
    nums = random.sample(range(1, 500001), size)
    # 冒泡排序
    start_time = time.time()
    bubble_sort(nums.copy())
    end_time = time.time()
    print(f"冒泡排序 ({size}个数) 时间：{end_time - start_time:.5f}秒")
    # 选择排序
    start_time = time.time()
    selection_sort(nums.copy())
    end_time = time.time()
    print(f"选择排序 ({size}个数) 时间：{end_time - start_time:.5f}秒")
    # 归并排序
    start_time = time.time()
    merge_sort(nums.copy())
    end_time = time.time()
    print(f"归并排序 ({size}个数) 时间：{end_time - start_time:.5f}秒")




