#datetime random string os math browser
#print('Modules')
#import platform

#print(dir(platform))
#import platform, string, os
# from platform import python_version as pv 
#print(platform.python_version())
# print(pv())
# print(system())

# classes
#inheritance example file for working with classes:
# class myClass():
#   def method1(self):
#       print("Guru99")
        
  
# class childClass(myClass):
#   def method1(self):
#         myClass.method1(self);
#         print ("childClass Method1")
        
#   def method2(self):
#         print("childClass method2")     
         
# def main():           
#   # exercise the class methods
#   c2 = childClass()
#   c2.method1()
#   c2.method2()

# if __name__== "__main__":
#   main()

# begins with a double underscore (_). It __init__() met
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to Guru99, " + self.name)

User1 = User("Alex")
User1.sayHello()
