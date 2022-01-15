import numpy as np
import weakref

#클래스형 변수 생성
class Variable:
    __array_priority__ = 200
    def __init__(self, data, name = None):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{}은(는) 지원하지 않습니다. np.ndarray를 이용해주세요.'.format(type(data)))

        self.data = data
        self.name = name
        self.grad = None #step06
        self.creator = None #이 변수를 만든 함수
        self.generation = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1

    @property
    def shape(self):
        return self.data.shape


    @property
    def ndim(self):
        return self.data.ndim

    @property
    def size(self):
        return self.data.size

    @property
    def dtype(self):
        return self.data.dtype

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        if self.data is None:
            return 'variable(None)'
        p = str(self.data).replace('\n', '\n' + ' ' * 9)
        return 'variable(' + p + ')'
    
    # def backward(self): #재귀 방식
    #     f = self.creator #함수를 가져온다
    #     if f != None:
    #         x = f.input #함수의 입력을 가져온다
    #         x.grad = f.backward(self.grad) # 함수의 backward 호출
    #         x.backward() # 하나 앞 변수의 backward를 호출(재귀)

    def backward(self, retain_grad = False): #반복 방식
        if self.grad == None:
            self.grad = np.ones_like(self.data)

        funcs = []
        seen_set = set()

        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key=lambda x: x.generation)
        
        add_func(self.creator)

        while funcs:
            f = funcs.pop() #함수를 가져온다
            gys = [output().grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x.creator is not None:
                    add_func(x.creator)

            if not retain_grad:
                for y in f.outputs:
                    y().grad = None
    
    def cleargrad(self):
        self.grad = None

'''
data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)
'''

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

def as_variable(obj):
    if isinstance(obj, Variable):
        return obj
    return Variable(obj)

class Config:
    enable_backprop = True

#함수의 기능
class Function:
    def __call__(self, *inputs):
        inputs = [as_variable(x) for x in inputs]

        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        if Config.enable_backprop:
            self.generation = max([x.generation for x in inputs])
            for output in outputs:
                output.set_creator(self)
            self.inputs = inputs
            self.outputs = [weakref.ref(output) for output in outputs]
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, xs):
        raise NotImplementedError() #하위 클래스에서 구현할 예정이라 구현되지 않으면 에러를 표시

    def backward(self, gys):
        raise NotImplementedError()

class Square(Function):#Fuction을 상속하여 구현
    def forward(self, x):
        return x **2
    
    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2 * x * gy
        return gx

'''
x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)
'''