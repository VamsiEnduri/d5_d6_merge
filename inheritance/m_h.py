# #  multi - level
# # multiple 
# # 
# modularity #
# reusability # class multiple objs
# security # ecnapu
# many forms  #poly
# hiding implemetations # abstrac


# class B: #parent1
#     cName="B"
#     def Bdetails(self):
#         print("b property")

# class A: #parent2
#     cName="A"
#     def Adetails(self):
#         print("a property")
#         # pass

# class C(A,B):
#     cName="C"
#     def __init__(self):
#         A.Adetails()
#         B.Bdetails()
#         print(B.cName)
# C()
# B.age # b object age attribute
# B["age"] # b dict age key

# hierarchail 

class A :
    surName="Enduri"
    town="Darsi"
    def details(self):
        print("parent method")

class A1(A):
    print(A.surName) 
    def __init__(self):
        print(super().town)
        super().details()
A1()    

class A2(A):
    print(A.surName)
    def __init__(self):
        print(super().town)
        super().details()

A2()          