"""
이 알고리즘은
개념의 이해가 중요하겠다.

계단을 한개에서 세개까지 한꺼번에 뛸 수 있을때에
n개의 계단을 오를 수 있는 방법은 몇가지 인가? 하는 것이다.
"""
import unittest

def countWays(n):
    if(n < 0): # 오를 계단이 없다면 방법개수 추가할 필요 없음
        return 0
    elif(n == 0): # 오를 계단이 0개라면 방법은 하나뿐
        return 1
    else:
        # 이 부분이 중요하다.
        # 최종 n 계단으로 오르는 마지막 방법은 1계단, 2계단, 3계단 아래에서 한 번에 오르는 세가지 경우의 수 뿐이다.
        # 그렇다면 그 1, 2, 3계단 아래까지 오르는 방법 역시 마찬가지로 구할 수 있다.
        return countWays(n-1) + countWays(n-2) + countWays(n-3)

class test_countWays(unittest.TestCase):
    def test(self):
        self.assertEqual(4, countWays(3))
        self.assertEqual(7, countWays(4))
