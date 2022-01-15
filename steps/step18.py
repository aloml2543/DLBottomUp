from step11 import *
import contextlib

@contextlib.contextmanager
def using_config(name, value):
    old_value = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)

# with using_config('enable_backprop', False):
#     x = Variable(np.array(2.0))
#     y = square(x)

def no_grad():
    return using_config('enable_backprop', False)

# with no_grad():
#     x = Variable(np.array(2.0))
#     y = square(x)

# x = Variable(np.array([[1,2,3], [4,5,6]]))
# print(x.shape)