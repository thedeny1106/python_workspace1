class MyType:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    
import inspect
t = MyType(1, 2)
print(*[(n, v) for (n, v) in inspect.getmembers(t) if not inspect.isfunction(v) and not n.startswith('__') and not inspect.ismethod(v)])
print(*[(n, v) for (n, v) in inspect.getmembers(t) if inspect.ismethod(v) and not n.startswith('__')])
setattr(t, 'x', 10)
setattr(t, 'y', 5)
print(getattr(t, 'add')())