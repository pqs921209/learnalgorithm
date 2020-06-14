# 选择排序，先选出最小的，然后插入A[1],再依次选择剩余数组中最小的，插入后边，以此类推.
def selection_sort(a):
    i = 0
    while i < len(a)-1:
        min = i
        j = i + 1
        while j < len(a):
            if(a[j]<a[min]):
                min = j
            j += 1
        # 交换a[i]和a[min]
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
        i += 1
    pass


a = [5,3,2,7,6,1,9,8,0,7]
print('before sort: ',a)

selection_sort(a)

print('sorted: ',a)