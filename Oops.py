# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create an object

class Calculator:
    num = 100 #class variables
    #default constructor
    def __init__(self, a, b): # parameterized constructor
        self.firstNumber = a
        self.secondNumber = b
        print ("I'm called automatically when object is created")

    def getdata(self):
        print("Executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num # Calculator.num can be called as self.num

 #Create objects in python
obj = Calculator(2,3) #"call the function" to create an object
obj.getdata() # call method
print(obj.summation()) # call and print variable

obj1 = Calculator(4,5) #"call the function" to create an object
obj1.getdata() # call method
print(obj1.summation()) # call and print variable