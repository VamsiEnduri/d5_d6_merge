# # polymorphism 


# # one method, takes no of args each time d/ly but behave same  :-- load :-- method overloading
# # *args :-- varable length arg
# class Cal: #polymorphism with method overloading
#     def result(self,*a):
#         total=0
#         for i in a:
#             total+=i
#         return total            

# obj=Cal()
# print(obj.result(10,20,30,40,50,60,70))
# overriding  poly morph   :-- 
class PayUPI:
    def pay (self):
        print()

class PayCOD:
    def pay (self,amount):
        print(f"{amount } paid via COD")

class PayCard:
    def pay (self,amount):
        print(f"{amount } paid through card")   


def pay_money(method,amount):
    method.pay(amount)

# pay_money(PayCOD(),250)    
pay_money(PayCard(),250)    
# pay_money(PayCOD(),250)


functions
scopes 
return 
class 
obj
self
4 pillars 