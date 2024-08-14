# import sys
# A, B, C = map(int, sys.stdin.readline().split())

# def calculate_mul(now_num, mul_target, mul_count, B):
#     if mul_count == B: ##다 곱해진 경우 재귀 끝내기
#         return now_num
#     else:
#         if mul_count*2 <= B: ##제곱을 했을 때 곱한 횟수가 제한 횟수에 넘지 않는다면
#             now_num = now_num * mul_target
#             mul_target = mul_target * mul_target
#             return calculate_mul(now_num, mul_target, mul_count*2, B)
#         else:
#             return calculate_mul(now_num, A, 1, B - mul_count)


# result = calculate_mul(A,A,1,B)
# print(result)

import sys
A, B, C = map(int, sys.stdin.readline().split())

def calculate_mul(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    else:
        half = calculate_mul(A, B // 2, C)
        half = (half * half) % C
        if B % 2 == 0:
            return half
        else:
            return (half * A)

result = calculate_mul(A, B)
print(result%C)
