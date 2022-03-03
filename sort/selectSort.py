# 选择排序
arr = [9, 7, 8, 6, 4, 5, 2, 3, 1]
len = arr.__len__()
print('原列表:', arr)
# 0-8 1-8 2-8 3-8 4-8 5-8 6-8 7-8
for i in range(len - 1):
    minIndex = i
    for j in range(i + 1, len):
        if arr[minIndex] > arr[j]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
# for i in range(len-1):
#     minIndex=i
#     for j in range(i+1,len):
#         if lst[minIndex]>lst[j]:
#             minIndex=j
#     lst[i],lst[minIndex] = lst[minIndex],lst[i]
print('排序后的列表:', arr)