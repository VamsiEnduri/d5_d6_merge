#  pillars of oops
# inheritance 
# accessing / acquiring parent class attributes ( vars ) and 
# parent class properties (methods/functions) in child class and using them in child class


# single-level 
# in single-level inh we have one parenyt class and one child class adn we can access parent class attr and props in child class 

class viratKohli: # class 
    pName="viratKohli" # cls var attr
    def __init__(self): # def con method  self 
        pass 

    def profession(self): # defined methods
        print("kohli with 84 centuries in intl cricket")

    def age(self):
        pass    

class akaayKohli(viratKohli):
    cName="akaay"
    def __init__(self):
        print(super().pName) #viratKohli
        super().profession()

    def profession(self):
        print("going to become crickter") 

    def age(self):
        print("3 age")  
objChild=akaayKohli()  
print(objChild.cName) 
objChild.profession()         
objChild.age()         