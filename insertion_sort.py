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
print('before sort',a)
insertion_sort(a)
print('asc',a)
insertion_sort_desc(a)
print('desc',a)


# 计算两个n位二进制整数相加之和
# A + B = C, C为n+1位

a = [0,1,0]
b = [1,1,0]
c = []
def bit_sum(a, b):
    k = 0 # 进位标志
    i = len(a) - 1
    while i >= 0:
        sum = a[i]+b[i]+k
        if sum > 1:
            k = 1
            c.insert(0,1)
        else:
            k = 0
            c.insert(0,sum)
        i -= 1
    c.insert(0,k)

bit_sum(a,b)
print('%s + %s = %s' % (a , b, c))