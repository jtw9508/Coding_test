# ##삽입 정렬
# def insertion_sort(list):
#     if len(list) == 1:
#         return list
#     for i in range(1, len(list)):
#         index = i
#         key = list[i]
#         while key < list[i-1]:
#             i -= 1
#             if i == 0:
#                 break
#         list.pop(index)
#         list.insert(i,key)
#     return list

# a = insertion_sort([2,-1,3,4,7,1,4,3,5])
# print(a)

# def insertion_sort_(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         # 이동하는 방식으로 비교를 수행합니다.
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]  # 키보다 큰 값을 오른쪽으로 이동
#             j -= 1
#         arr[j + 1] = key  # 키를 올바른 위치에 삽입
#     return arr
# b = insertion_sort_([2,-1,3,4,7,1,4,3,5])
# print(b)

def merge(arr, s, m, l):  # 시작 인덱스, 중간 인덱스, 마지막 인덱스
    arr1 = arr[s:m+1]  # 첫 번째 하위 배열
    arr2 = arr[m+1:l+1]  # 두 번째 하위 배열

    arr1.append(float('inf'))  # 무한대 값을 추가하여 비교를 쉽게 만듦
    arr2.append(float('inf'))

    i = 0  # arr1의 인덱스
    j = 0  # arr2의 인덱스

    for k in range(s, l+1):  # 원래 배열에 합치는 작업
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1

def merge_sort(arr, s, l):
    if s < l:
        q = (s+l) // 2  # 중간 인덱스를 계산
        merge_sort(arr, s, q)  # 왼쪽 하위 배열 정렬
        merge_sort(arr, q+1, l)  # 오른쪽 하위 배열 정렬
        merge(arr, s, q, l)  # 정렬된 하위 배열을 병합

array = [3, 4, 1, 2, 5, 7, 1, 2, 3]
merge_sort(array, 0, len(array) - 1)  # 올바른 마지막 인덱스를 전달
print(array)
