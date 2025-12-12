v1=int(input("enter v1 here :--  "))
v2=int(input("enter v2 here :--  "))

def A():
    return "10000Coders"
class A:
    clsName="A" #class varaible
    def __init__(self): # CONstructor function
        pass
    def add(self): # defined function
        x=self.v1Value
        y=self.v2Value
        return x+y   

class B(A):
    clsName="B"
    def __init__(self):
        pass
    def getter(self):
        
        aDefinedM=super().add()
        return aDefinedM    

class C(B):
    clsName="C"
    def __init__(self,v1_,v2_):
        self.v1Value=v1_
        self.v2Value=v2_
    def finalOutput(self):
        abc=A()
        print(abc)
        o_p=super().getter()
        print(o_p)    
o=C(v1,v2)    
o.finalOutput()    