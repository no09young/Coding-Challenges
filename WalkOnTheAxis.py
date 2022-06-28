def solution(x):
    return int((x*(x+1)/2)+x)
    
T = int(input())
A = []

for i in range(T):
    A.append(int(input()))
    
for x in A:
    print(solution(x))