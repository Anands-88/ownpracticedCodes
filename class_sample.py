class sampleclass: # Declaring a class called sampleclass.
    count = 0 #  class attribute or class variable

    def increase(self):    
        sampleclass.count += 2
            

    def decrease(self):
        sampleclass.count -= 1
            

sc1 = sampleclass()
sc1.increase() #  calling increase() on an object (sc1)
print(sc1.count)

sc2 = sampleclass()
sc1.decrease() # calling decrease() on an object (sc2)
print(sc2.count) 


class Counting: # we declare a class

    def __init__(self, count):
        self.count = count # instance attribute or instance variable.  THE CLASS HAS 1 I.V.or I.A. 

    def increase(self,count):
        self.count += count
        print(self.count) # Then we printout the value of count using dot notation
    
    def decrease(self, count):
        self.count -= count
        print(self.count)

number = Counting(2) # creating instance of class with a value  2.
# NEXT WE CREATE INSTANCE OF CLASS CALLED "number"
# and assign the value of count variable to 2

number.increase(0) # calling increase() on an object (number) with value 2

number.decrease(1) # calling decrease() on an object (number) with value 1


