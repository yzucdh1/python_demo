# 插入排序
arr = list([5, 4, 9, 8, 3, 1, 6, 2, 7])
len = arr.__len__()
print('原列表', arr)
# 0-1 0-2 0-3 0-4 0-5 0-6 0-7 0-8
for i in range(1, len):
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j -= 1
# for i in range(len-1):
#     j = i+1
#     while(j>0 and lst[j]<lst[j-1]):
#         lst[j],lst[j-1] = lst[j-1],lst[j]
#         j-=1
print('排序后的列表', arr)