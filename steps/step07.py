from step06 import *



# A = Square()
# B = Exp()
# C = Square()

# x = Variable(np.array(0.5))
# a = A(x)
# b = B(a)
# y = C(b)

# assert y.creator == C #assert 다음이 true가 아니면 예외 발생
# assert y.creator.input == b
# assert y.creator.input.creator == B

# y.grad = np.array(1.0)

'''
#자동화 전
C = y.creator #함수를 가져온다
b = C.input #함수의 입력을 가져온다.
b.grad = C.backward(y.grad) #함수의 역전파를 호출

B = b.creator
a = B.input
a.grad = B.backward(b.grad)

A = a.creator
x = A.input
x.grad = A.backward(a.grad)

print(x.grad)
'''
# #자동화 후
# y.backward()
# print(x.grad)
