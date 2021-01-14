
class Byte():
    def __init__(self, num=0, flag="s"):
        if type(num) == int: self.num = num
        else: self.num = int(num, 2)
        if flag == "s" and -128 <= self.num <= 127 or flag == "u" and 0 <= self.num <= 255:
            self.str = '{0:08b}'.format(self.num if self.num > 0 else self.num + (1<<8))
            self.count = 8
        else:
            raise Exception("Overflow Exception")
        
    def __and__(self, other):
        return Byte(self.num & other.num)
    
    def __or__(self, other):
        return Byte(self.num | other.num)
    
    def __invert__(self):
        return Byte(~self.num)
    
    def __add__(self, other):
        return Byte(self.num + other.num)
    
    def __sub__(self, other):
        return Byte(self.num - other.num)
    
    def __getitem__(self, key):
        return int(self.str[len(self.str)-key-1])
    
    def __setitem__(self, key, value):
        i = len(self.str)-key-1
        self.str = self.str[:i]+str(value)+self.str[i+1:]
        self.num = int(self.str, 2)
        
    def __iter__(self):
        return self   
    
    def __next__(self):
         self.count -=1
         if self.count+1: return int(self.str[self.count])
         else: 
             self.count = 8
             raise StopIteration
    
    def __str__(self):
        return f'0b{self.str}'
        
a = Byte(100)
b = Byte(50)
c = Byte("0b01000110")
print(a)
print(~a)
print(b)
print(c)
print(a[2])
print(a & b)
for i in a:
    print(i)
print(a - b)
print(next(a))
print(next(a))
print(next(a))
