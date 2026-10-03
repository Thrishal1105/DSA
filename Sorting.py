# BUBBLE SORT

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr

# arr = [5,3,1,2]
# print(bubble_sort(arr))





# SELECTION SORT


# def select_sort(arr):
#     for i in range(len(arr)):
#         mid = i

#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[mid]:
#                 mid = j
#         arr[i], arr[mid] = arr[mid], arr[i]

#     return arr

# arr = [5, 3, 1, 2]
# print(select_sort(arr))





# INSERTION SORT

# def insertion(arr):
#     for i in range(len(arr)):
#         key = arr[i]
#         j = i-1

#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
# arr = [5,2,1,3]
# print(insertion(arr)) 





# MERGE SORT

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [6,2,4,1,9,3,8,5]
print(merge_sort(arr))