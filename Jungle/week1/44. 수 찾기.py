import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))
input_list.sort()

def binary_search(num_list,start, last, k):
    if start > last:
        return 0    
    else:
        mid = (start + last) // 2

        if num_list[mid] == k:
            return 1        
        elif num_list[mid] > k:
            return binary_search(num_list,start,mid-1,k)
        else:
            return binary_search(num_list,mid+1,last,k)

for n in check_list:
    is_in = binary_search(input_list,0,len(input_list)-1,n)
    print(is_in)