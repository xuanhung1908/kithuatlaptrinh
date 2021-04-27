class cr:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
a=cr(5)
print(a.area())
