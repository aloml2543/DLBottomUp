from step07 import *

def square(x):
    return Square()(x)

def exp(x):
    return Exp()(x)

# x = Variable(np.array(0.5))

# #1번째 방법
# a = square(x)
# b = exp(a)
# y = square(b)

# #2번쨰 방법
# y = square(exp(square(x)))

# # y.grad = np.array(1.0)
# y.backward()
# print(x.grad)

# x = Variable(np.array(1.0))
# x = Variable(None)


# x = Variable(1.0) #에러 발생

