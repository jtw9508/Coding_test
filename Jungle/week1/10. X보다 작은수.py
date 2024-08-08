iter, X = map(int, input().split())
numbers = list(map(int, input().split())) #input.split()의 결과는 리스트
for i in numbers:
    if i < X:
        print(i, end = " ")