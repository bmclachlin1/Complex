# @author Blake McLachlin

class Complex:
    """
    Represents a complex number of the form x + iy
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __repr__(self):
        return f'Complex({self.real}, {self.imag})'


    def __str__(self):
        if self.imag < 0:
            return f'{self.real} - {abs(self.imag)}i'
        return f'{self.real} + {self.imag}i'
    

    def __neg__(self):
        return Complex(-self.real, -self.imag)


    def conjugate(self):
        return Complex(self.real, -self.imag)


    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        if isinstance(other, (float, int)):
            return Complex(self.real + other, self.imag)
        raise ValueError(f"Cannot add Complex to {type(other)}")


    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        if isinstance(other, (float, int)):
            return Complex(self.real - other, self.imag)
        raise ValueError(f"Cannot subtract {type(other)} from Complex")


    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag, 
                           self.real * other.imag + self.imag * other.real)
        raise ValueError(f"Cannot multiply Complex with {type(other)}")

    
    def __truediv__(self, other):
        if isinstance(other, Complex):
            conj = other.conjugate()
            den = other * conj 
            den = den.real 
            num = self * conj
            return Complex(num.real / den, num.imag / den)
        raise ValueError(f"Cannot divide Complex by {type(other)}")

x = Complex(-2.5, -4)
y = Complex(3.5, -3.2)

print(f"({x}) + ({y}) = {x + y}")
print(f"({x}) + 6 = {x + 6}")
print(f"({x}) * ({y}) = {x * y}")
print(f"({x} / {y}) = {x / y}")
print(f"-({x}) = {-x}")