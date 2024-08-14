import sys
input = sys.stdin.readline

## 순열 1.
def permutations(arr, r):
    result = []

    def permute(path, options):
        if len(path) == r:  # r개의 원소를 다 선택한 경우
            result.append(path)
            return
        
        for i in range(len(options)):
            # 현재 원소를 선택하고, 남은 원소들로 재귀 호출
            permute(path + [options[i]], options[:i] + options[i+1:])

    permute([], arr)
    return result
## 순열 2.

def permutations(arr, r):
    result = []
    used = [False] * len(arr)  # 각 원소의 사용 여부를 저장하는 배열

    def permute(path):
        if len(path) == r:  # r개의 원소를 다 선택한 경우
            result.append(path[:])  # path의 복사본을 추가
            return
        
        for i in range(len(arr)):
            if not used[i]:  # 사용되지 않은 원소만 선택
                used[i] = True  # 해당 원소를 사용으로 표시
                permute(path + [arr[i]])  # path에 원소를 추가하고 재귀 호출
                used[i] = False  # 원소 사용을 해제

    permute([])  # 초기 path는 빈 리스트

## 순열 3.
def permutations(path, arr, r):
    if len(path) == r:
        result.append(path)
        return
    
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            permutations(path + [arr[i]], arr, r)  # path에 원소를 추가하고 재귀 호출
            used[i] = False

# Initial setup
r = 2
arr = [1, 2, 3, 3]
used = [False] * len(arr)
result = []

# Generate permutations
permutations([], arr, r)

print(result)

## 조합 1.
def combinations(arr, r):
    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])  # 조합을 결과에 추가
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)  # 다음 원소를 선택하기 위해 인덱스를 증가
            path.pop()  # 현재 원소를 제거하고 다음 조합을 위해 진행

    result = []
    backtrack(0, [])
    return result

# 예제 사용
arr = [1, 2, 3, 4]
r = 3
print(combinations(arr, r))

## 조합 2. 가지치기
def combinations(arr, r):
    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])  # 조합을 결과에 추가
            return
        
        # 가지치기: 남은 원소의 수가 필요한 개수보다 적으면 종료
        if len(path) + (len(arr) - start) < r:
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)  # 다음 원소를 선택하기 위해 인덱스를 증가
            path.pop()  # 현재 원소를 제거하고 다음 조합을 시도

    result = []
    backtrack(0, [])
    return result

# 예제 사용
arr = [1, 2, 3, 4]
r = 3
print(combinations(arr, r))

## 중복순열
def count_unique_permutations_with_replacement(arr, counts, r):
    """
    :param arr: 사용 가능한 원소들
    :param counts: 각 원소의 사용 가능한 수량
    :param r: 생성할 순열의 길이
    :return: 가능한 순열의 개수
    """
    def backtrack(path, remaining, total_length):
        if total_length == r:
            return 1  # 유효한 순열을 발견했으므로 1을 반환
        
        count = 0
        for i, item in enumerate(arr):
            if remaining[i] > 0:
                # 현재 원소를 path에 추가하고 재귀 호출
                remaining[i] -= 1
                count += backtrack(path + [item], remaining, total_length + 1)
                # 원소를 제거하고 나머지 원소를 시도
                remaining[i] += 1
        
        return count
    
    remaining = counts[:]
    return backtrack([], remaining, 0)

# 예제 사용
arr = [0, 1, 3]
counts = [4, 2, 2]  # 각각의 원소의 수량
r = 4
a = count_unique_permutations_with_replacement(arr, counts, r)
print(a)

def all_unique_permutations_with_replacement(arr, counts, r):
    """
    :param arr: 사용 가능한 원소들
    :param counts: 각 원소의 사용 가능한 수량
    :param r: 생성할 순열의 길이
    :return: 가능한 모든 순열의 리스트
    """
    def backtrack(path, remaining, total_length):
        if total_length == r:
            result.append(path[:])  # 유효한 순열을 발견했으므로 리스트에 추가
            return
        
        for i, item in enumerate(arr):
            if remaining[i] > 0:
                # 현재 원소를 path에 추가하고 재귀 호출
                remaining[i] -= 1
                backtrack(path + [item], remaining, total_length + 1)
                # 원소를 제거하고 나머지 원소를 시도
                remaining[i] += 1
    
    result = []
    remaining = counts[:]
    backtrack([], remaining, 0)
    return result

# 예제 사용
arr = [0, 1, 3]
counts = [4, 2, 2]  # 각각의 원소의 수량
r = 4
all_permutations = all_unique_permutations_with_replacement(arr, counts, r)
# print(all_permutations)

##중복 조합
def combinations(arr, r, remaining_count):
    def backtrack(start, path, remaining_count):
        if len(path) == r:
            result.append(path[:])  # 조합을 결과에 추가
            return
        
        # 가지치기: 남은 원소의 수가 필요한 개수보다 적으면 종료
        if len(path) + remaining_count < r:
            return
        
        for i in range(start, len(arr)):
            if count[i] > 0:
                count[i] -= 1
                path.append(arr[i])
                backtrack(i, path, remaining_count - 1)
                path.pop()  # 현재 원소를 제거하고 다음 조합을 시도
                count[i] += 1

    result = []
    backtrack(0, [], remaining_count)
    return result

# 예제 사용
arr = [1, 2, 3]
count = [2, 3, 1]  # 각 원소의 최대 사용 가능 횟수
r = 4
print(combinations(arr, r, sum(count)))
