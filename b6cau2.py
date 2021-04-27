class hinhchunhat:
    def __init__(self,cd,cr):
        self.chieudai=cd
        self.chieurong=cr
    def area(self):    
       return self.chieudai*self.chieurong
a=hinhchunhat(2,6)
print(a.area())
    
