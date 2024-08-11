# import sys
# N = int(sys.stdin.readline())
# word_temp = [[] for _ in range(50)]
# for i in range(N):
#     word = sys.stdin.readline().strip()
    
#     word_temp[len(word)-1].append(word)

# for word_list in word_temp:
#     word_t = ''
#     if len(word_list) >= 1:
#         for word in sorted(word_list):
#             if word != word_t:
#                 print(word)
#                 word_t = word
#             else:
#                 continue


import sys
N = int(sys.stdin.readline())
word_temp = [set() for _ in range(50)]
for i in range(N):
    word = sys.stdin.readline().strip()
    
    word_temp[len(word)-1].add(word)

for word_list in word_temp:
    for word in sorted(word_list):
        print(word)
