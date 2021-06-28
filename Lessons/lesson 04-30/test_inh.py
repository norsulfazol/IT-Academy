class Test1:

    def m(self):
        print("Test1")

class Test2:

    def m(self):
        print("Test2")

class Test(Test2, Test1): pass

t = Test()
t.m()