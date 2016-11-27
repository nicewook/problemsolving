import unittest

def reverseString(str):
    return str[::-1]

#use array as stack
def reverseString2(str):
    stack=[]
    for ch in str:
        stack.append(ch)

    print("stack: ", stack)
    result = ""
    while len(stack) > 0:
        #stack.pop() 으로 맨 뒤부터 꺼내주나 보다

        result += stack.pop()

    print("result is: ", result)
    return result

input1 = "abcdefg"
input2 = "good job"

class reverseStringTest(unittest.TestCase):
    def test(self):
        self.assertEqual("gfedcba", reverseString(input1))
        self.assertEqual("boj doog", reverseString(input2))
        self.assertEqual("gfedcba", reverseString2(input1))
        self.assertEqual("boj doog", reverseString2(input2))

print ("input1: ", input1, "input2: ", input2)
print (reverseString2(input1)," and " , reverseString2(input2))


