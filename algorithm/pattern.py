# brute force

p = 'is'  # 찾을 패턴
t = "thirs is book"  # 전체
m = len(p)  # 패턴 길이
n = len(t)  # 전체 길이

def brute_force(p, t):
    i = 0
    j = 0
    while j < m and i < n:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == m: return i-m  # 검색 성공
    else: return -1  # 검색 실패


# KMP
# T : target // P : pattern
def pre_process(p):

    lps = [0] * len(p)# longest prefix suffix
    # lps를 만들기 위한 패턴 인덱스
    j = 0

    for i in range(1, len(p)):
        # 패턴 발견 해당 인덱스에 있는 글자가 같으면
        if p[i] == p[j]:
            lps[i] = j+1
            j += 1
        # 다르다면 j 인덱스 초기화
        else:
            j=0
            if p[i] == p[j]:
                lps[i] = j+1
                j += 1
    return lps

a = 'abcfffabcggggeabc'
print(pre_process(a))
