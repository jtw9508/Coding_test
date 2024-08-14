# import bisect
# import sys



# n = int(sys.stdin.readline())



# answer_list = []
# for i in range(n):
#     k = int(sys.stdin.readline())
#     bisect.insort(answer_list,k)
# for n in answer_list:
#     print(n)

# def binary_search(lst, target):
#     start = 0
#     end = len(lst) - 1
#     if len(lst) == 0:
#         lst.append(target)
#         return
#     while start <= end:
#         mid = (start + end) // 2
        
#         if lst[mid] == target:
#             lst.insert(mid, target)
#             return
        
#         elif lst[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1

#     # 삽입할 위치를 찾았을 때
#     lst.insert(start, target)

def location(S, low, high,x):
    if (low > high):
        print(low,high)
        return 0
    else:
        mid = (low + high) // 2
        print(low,mid,high)
        if (x == S[mid]):
            return mid
        elif (x < S[mid]):
            return location(S, low, mid -1,x)
        else:
            return location(S, mid+1, high,x)
        
S = [-1,10,12,13,14,18,20,25,27,30,35,40,45,47]
x = 8
loc = location(S,1,len(S)-1,x)
print(loc)

def merge2(S, low,mid,high):
    U = []
    i = low
    j = mid + 1
    while (i <= mid and j <= high):
        if (S[i] < S[j]):
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1
    if (i <= mid):
        U += S[i : mid + 1]
    else:
        U += S[j : high +1]
    for k in range(low, high + 1):
        S[k] = U[k - low]

def mergesort2 (S, low, high):
    if (low < high):
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        mergesort2(S, mid+1, high)
        merge2(S, low,mid,high)