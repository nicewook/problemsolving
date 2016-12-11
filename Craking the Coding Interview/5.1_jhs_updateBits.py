"""
N = 10000000000
M = 10011
i = 2
j = 6
output : 10001001100
"""

def printBinary(num):
    b_num = bin(num)

    # 두 프린트의 차이는 뭐지?
    print(b_num[2:])
    # bin(num) 함수는 2진수로 만들어주는데 첫 2자리는 0b라고 넣어준다. 이걸 빼고 프린트하기 위해 [2:]라고 한 것이다.
    print(b_num)

# N의 특정부분을 0으로 만들기
def getMask(i, j, max_int):
    # 11100000000
    left = max_int << (j + 1)
    # 00000000011
    right = (1 << i) - 1
    # 11100000011
    return left | right

def UpdateBits(m, n, i, j):
    max_int = 2 ** 32 - 1 # 0xFFFFFFFF
    mask = getMask(i,j,max_int)

    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted
m = 19
n = 1024
i = 2
j = 6

result = UpdateBits(m,n,i,j)
printBinary(result)


