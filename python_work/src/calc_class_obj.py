class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b 

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = calculator(a,b)
while True:
    print('1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Exit')
    choice = int(input('Enter the digit'))
    if choice == 1:
        print(c.add())
    elif choice == 2:
        print(c.sub())
    elif choice == 3:
        print(c.div())
    elif choice == 4:
        print(c.mul())
    elif choice == 5:
        break
