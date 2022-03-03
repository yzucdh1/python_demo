# 冒泡排序
arr = list([4, 2, 8, 9, 7, 6, 1, 3, 5])
print('原列表:', arr)
len = arr.__len__()
# 0-8 0-7 0-6 0-5 0-4 0-3 0-2 0-1
for i in range(len - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
# for i in range(len-1):
#     for j in range(len-1-i):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
#
print('排完序的列表:', arr)