from step10 import *

class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y #튜플 반환

    def backward(self, gy):
        return gy, gy

def add(x0, x1):
    x1 = as_array(x1)
    return Add()(x0, x1)



# xs = [Variable(np.array(2)), Variable(np.array(3))]
# f = Add()
# ys = f(xs)
# y = ys[0]
# print(y.data)

# x0 = Variable(np.array(2))
# x1 = Variable(np.array(3))
# y = add(x0, x1)
# print(y.data)

# x = Variable(np.array(2.0))
# y = Variable(np.array(3.0))

# z=add(square(x), square(y))
# z.backward()
# print(z.data)
# print(x.grad)
# print(y.grad)

# x = Variable(np.array(2.0))
# a = square(x)
# y = add(square(a), square(a))
# y.backward()

# print(y.data)
# print(x.grad)

# for i in range(10):
#     x = Variable(np.random.randn(10000))
#     y = square(square(square(x)))

# x0 = Variable(np.array(1.0))
# x1 = Variable(np.array(1.0))
# t = add(x0, x1)
# y = add(x0, t)
# y.backward()

# print(y.grad, t.grad)
# print(x0.grad, x1.grad)

# Config.enable_backprop = True
# x = Variable(np.ones((100,100,100)))
# y = square(square(square(x)))
# y.backward()

# Config.enable_backprop = False
# x = Variable(np.ones((100,100,100)))
# y = square(square(square(x)))

