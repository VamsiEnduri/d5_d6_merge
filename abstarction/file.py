# # abstraction 
# # abstraction is nothing but hiding implementation of feature but showcasing the just feature

# # class A:
# #     def Aname(self):
# #         print("a name function in A class")
# # class ABC:
# #     def execute(self,iClass):
# #         print(iClass,"999")
# # obj=ABC() 
# # obj.execute(A)               


# # class BankAccount:
# #     def __init__(self):
# #         self.bal=10000
# #     def check_bal(self):
# #         return self.bal 

# # class UserFeatures:
# #     def executeFeature(self,iClass):
# #         b=iClass.check_bal()
# #         print(b)

# # obj=UserFeatures()  
# # obj.executeFeature(BankAccount())      

# class A:
#     def run(self):
#         pass

# class A1(A):
#     def run(self):
#         pass 

# class A2(A) :
#     def run(self):
#         pass        



class Vehicle:
    def start(self):
        print("Vehicle starts")

    def stop(self):
        print("Vehicle stops")


class Car(Vehicle):
    def start(self):
        print("car begins to start")
        super().start()
        print("car begins to end")
        
    def stop(self):
        pass
        
obj=Car()
obj.start()




