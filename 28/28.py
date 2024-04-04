#ejercicio de clases en python
#crear una clase llamada calculadora que tenga los siguientes metodos: sumar, restar, multiplicar y dividir
class calculate1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

calculate = calculate1(10, 5)
print(calculate.add())
print(calculate.sub())
print(calculate.mul())
print(calculate.div())
