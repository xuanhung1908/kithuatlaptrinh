class nguoi:
    def __init__(self):
        pass
    def getgender(self):
        pass
class nam(nguoi):
    def __init__(self):
        nguoi.__init__(self)
    def getgender(self):
        print('Nam')
class nu(nguoi):
    def __init__(self):
        nguoi.__init__(self)
    def getgender(self):
        print('Nu')
nam=nam()
nam.getgender()
nu=nu()
nu.getgender()
