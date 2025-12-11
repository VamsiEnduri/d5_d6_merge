# import math

# a=10
# def abc():
#     pass
# print(type(a))
# print(type(abc))
# print(math)


# class syntax :-- 
# class cls_name:
#     #code
#     # varaibles attributes class local instance
#     # defined functions  methods r properties
    #   inuilt method 

# class InstagramFeature:
#     featureName="post" # var
#     print(featureName)
#     def __init__(a): # default method ( constructor function ) # inbuilt func
#         print("init method")
#     def postImg(): # defined func
#         print("postImg method")
#     def postText():
#         pass 
#     def postSEOkeywords():
#         pass 
# InstagramFeature()  # class invokation              



class InstagramFeature: #home plan home bp sketch
    featureName="post" # var
    # print(featureName)
    def __init__(self,i,t,k): # things need to build all rooms # default method ( constructor function ) # inbuilt func
        self.imgLink =i
        self.text =t
        self.keywords=k
        # print(self.text)
        # print(self)

    def postImg(self): # defined func #KITCHEN
        print("postImg method")
        print(self.imgLink)
    def postText(self): #BEDROOM
        print(self.text)
        
    def postSEOkeywords(self): #DINING HALL
        print(self.keywords)
        
    # print(InstagramFeature.text,"text")    
abc=InstagramFeature("https://www.mindrops.com/images/nodejs-image.webp","nodejs is very concurrant for handling n no of users at single glance","nodejs #nodjes #backend")
# print(abc).
print(abc.imgLink,"55")
print(abc.text,"56")
print(abc.keywords,"57")
print(abc.featureName,"58")
abc.postImg()
abc.postText()
abc.postSEOkeywords()
abc.__init__()


youtube any feature blueprint
linkedin any feature 
netflix any feature