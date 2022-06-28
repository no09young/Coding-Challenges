def solution(couple):
    if len(couple[0]) > len(couple[1]):
        l_name = couple[0]
        s_name = couple[1]
    elif len(couple[0]) == len(couple[1]):
        if couple[0] == couple[1]:
            ans = 'YES'
        else:
            ans = 'NO'
        
        return ans
    else:
        l_name = couple[1]
        s_name = couple[0]
    
    s, l = 0, 0
    while s < len(s_name) and l < len(l_name):
        if s_name[s] == l_name[l]:
            s += 1
            l += 1
        else:
            l += 1
    
    if s == len(s_name):
        ans = 'YES'
    else:
        ans = 'NO'
    
    return ans

T = int(input())
A = []

for i in range(T):
    A.append(input().split(" "))

for x in A:
    print(solution(x))