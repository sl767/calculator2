[![Build Status](https://travis-ci.org/sl767/calculator2.svg?branch=master)](https://travis-ci.org/sl767/calculator2)
# Object Oriented Programming
# Encapsulation
According to Downey, "wrapping a piece of code up in a 
function is called encapsulation." Encapsulation makes the 
internal representation of the function can't be seen from 
outside the function's definition (Klein).

    class Encapsulation (object):
        def__init__(self, a, b, c):
            self.public = a
            self._protected = b
            self.__private = c
The indented functions under the class Encapsulation are examples
of encapsulated data.

# Abstraction
Like encapsulation, abstraction is "hiding the complexity and 
only showing the essential features of the object" (Anshudeep).
As with the example given for encapsulation, abstraction would be the 
indented code within the class attribute.

# Inheritance
According to Downey, "inheritance is the 
ability to define a new class that is a modified version of an existing class."
Here is an example of inheritance from zetcode.com
  
    class Animal:

        def __init__(self):
            print("Animal created")

        def whoAmI(self):
            print("Animal")

        def eat(self):
            print("Eating")


    class Dog(Animal):

        def __init__(self):
            super().__init__()
            print("Dog created")

        def whoAmI(self):
            print("Dog")

        def bark(self):
            print("Woof!")

    d = Dog()
    d.whoAmI()
    d.eat()
    d.bark()