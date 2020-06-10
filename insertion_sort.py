# 插入排序
def insertion_sort(a):
    j = 1
    while j < len(a):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
        j += 1

def insertion_sort_desc(a):
    j = 1
    while j < len(a):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
        j += 1

a = [5,3,2,7,6,1,9,8,0,7]
insertion_sort(a)
print('asc',a)
insertion_sort_desc(a)
print('desc',a)