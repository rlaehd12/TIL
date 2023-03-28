#################### 부분집합 전부 구하기 (for문으로)

a = [1,2,3,4]
bit = [0] * 4
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print(bit, end= ' ')
                pass
                for p in range(4):
                    if bit[p]:
                        # print(a[p], end='')
                        pass
                # print()
                pass

################### 비트연산자 이용 부분집합

arr = [3,6,7,1,8,4]
n = len(arr)                # 원소의 개수

# i는 000 001 010 100 을 가짐
for i in range(1<<n):       # 1<<n: 2^n 즉 부분집합 개수       
    for j in range(n):      # 원소 수만큼 비트 비교
        if (i & (1<<j)) != 0:      # i의 j번째 비트가 1인지 0인지 확인
            print(arr[j], end=', ')  # 1이면 배열 j번째 원소 출력, 0이면 출력 안함
    print()
print()
