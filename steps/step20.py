from step18 import *

class Mul(Function):
    def forward(self, x0, x1):
        y = x0 * x1
        return y

    def backward(self, gy):
        x0, x1 = self.inputs[0].data, self.inputs[1].data
        return gy * x1, gy * x0

def mul(x0, x1):
    x1 = as_array(x1)
    return Mul()(x0, x1)





Variable.__mul__ = mul
Variable.__add__ = add
Variable.__rmul__ = mul
Variable.__radd__ = add

# x = Variable(np.array(2.0))
# y = 3.0 * x + 1.0
# print(y)



# a = Variable(np.array(3.0))
# b = Variable(np.array(2.0))
# c = Variable(np.array(1.0))

# y = a * b + c

# y.backward()

# print(y)
# print(a.grad)
# print(b.grad)




