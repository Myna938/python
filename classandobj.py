'''class Car:
    brand=""
    model=""
    def person1(self): #fun create
        print("the brand name is:")
    def person2(self):# another fun
        print("the model is:")

P1=Car()#object declaration
P2=Car()#another object declaration
P1.brand="BMW"
Car.person1()
print(P1.brand)
'''
#another method to solve this 
class Car:
    model=""
    brand=0

person1=Car()
person2=Car()
person1.model="BMW"
person1.brand=20
person2.model="Rolex"
person2.brand=24

print("the model is :",person1.model)
