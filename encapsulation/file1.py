# __abcd=1000
# _a=100
# # print(__abcd)
# class BankAccount:
#     __abc=100 #pri
#     _xyz=2000 # prote
#     def __init__(self,aN,nH,mB):
#         self.accountNumber=aN # public vars
#         self._accountHolder=nH # protected vars
#         self.__accountMinBal=mB # private vars    # very private  very sensistive data
#     # print(self.__accountMinBal)
#     print(BankAccount.__accountMinBal)
#     def amountGetter(self): # getter function used to get privtae var data
#         print(self.__accountMinBal)  

#     def amountSetter(self,iAmount):
#         if iAmount<0:
#             print("enter amount >0")
#         else:
#             self.__accountMinBal+=iAmount
#             print(self.__accountMinBal)    
# obj=BankAccount("123123321","vamsiEnduri",5000) 
# # print(obj._BankAccount__accountMinBal) #accessing privv var outside r getting value of priv var oitisde of class
# # print(obj._BankAccount__abc)
# # print(obj._xyz)
# obj.amountGetter() # invoking method and getting result of private var data in o/p
# obj._BankAccount__accountMinBal+=2000
# print(obj._BankAccount__accountMinBal)
# obj.amountSetter(2000)
# # name mangling  ------------
# # using  methods

encpauslation :--
hiding data as like protected with _ and as like private with __ 

in order to access private vars outside of a class , we can do it in 2 ways
1. name mangling 
outside of clas i can access private vars 
outside of clas i can set / update private vars data

2. methods
i can create a method inside a class and in that method i can access private vars and now i can call that method outside of class  with obj and i can access private vars without name  mangling

i can set / update private vars data by creating setter function and i need to create that setter function inside a class and i can call it ourside of class with obj


------------
i can access self private vars inside that functions only if i wanna access them inisde class diectly and no need of name mangling

does nt have any errors related lines in class 