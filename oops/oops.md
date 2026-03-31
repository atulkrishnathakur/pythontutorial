# programming pradigms
1. Ways of organizing program
2. python supports multiple paradigms. Thease are as follows.  
   2.1 procedural oriented paradigm
   2.2 Functional oriented paradigm
   2.3 Object oriented paradigm


# object in oop
1. An object in oop represent real life object. like man, animal, fan etc.
2. Every object has two properties:  
   2.1 Attributes
   2.2 Behaviours

# What is Object Oriented Programming?
1. Object oriented programming is an approach of writing programs by creating classes and objects.
2. More focus on data rather than logic


# Why oop?
1. To solve real-world problem effectively
2. OOP provide some feature  
   2.1 Inheritance:- reusability
   2.2 encapsulation:- data security
   2.3 abstraction:- Data hiding

# What is class?
1. class is a template/blueprint/prototype for creating objects.
2. every object blong from a class.
3. technically, class is a user define datatype
4. In python every thing is object.
5. class is a collection of attributes and methods
6. Class is a collection of objects
7. `class` keyword use to create class


# Built-in class functions
1. getattr(object_name, attribute_name)
2. setattr(object_name, attribute_name, new_value)
3. delattr(object_name, attribute_name)
4. hasattr(object_name, attribute_name)

# Built in class attributes
1. `__dict__` dictionary contains class names
2. `__doc__` class documentation string
3. `__name__` class name
4. `__module__` Module name in which class is defined
5. `__bases__` List of base classes


# instance variables 
1. Variable made for particular instance
2. Separate copy is created for every object.
3. Values of variable differs from object to object
4. Modification in one object won't effect other objects. 


# class variables
1. Class variable made for entire class(All ojects)
2. Only one copy is created and distributed to all objects.
3. Modification in class variable impact on all objects.


# class method
1. class method works on class variable
2. First argument is class reference
3. `@classmethod` decorator used to make class method


# static method 
1. Mainly static method perform operation on external data
2. It can also perform operations on class data
3. No need to pass object or class referece.
4. `@staticmethod` decorator used to create static method

# What is inheritance?
1. Derriving a new class from an existing class so that new class inherits all members(attributes + methods) of existing class is called as inheritance.
2. old class is called Parent Class, Base class, Existing Class, Supper Class.
3. new class is called Child class, sub class, derived class.
4. All classes in python are derrived from a built-in `object` class
```
class Employee(object):
   bonos = 2000
   def display(self):
      print("This is employee class method")
```

# Need of inheritance
1. For the code-reusability(Write once use many times)
2. When you have relations among classes.

# super() function in inheritance
1. Using super() function, We can access parent class properties.
2. This function returns a temporary object which contains referece to parent class.
3. It makes inheritance more manageable and extensible.


# What is encapsulation in python?
1. Wrapping up data and methods working on data togather in a single unit(i.e class) is called as encapsulation.
2. If you access variable data outside of class then it not follow the encapsulation concept. In encapsulation you will not access variable data outside of class.
3. Generally, We restrict data access outside of the class in encapsulation
4. Encapsulation can be achived by declaring the data members and method of a class as private.
5. private variable can be access inside the class by methods
6. Encapsulation can protect accidental modification of variable by using private accessifier.


# Access Modifiers in python:
1. public: Accessible anywhere by using object referece.
2. private: Accessible within the class. Accessible via methods only.
3. protected: Accessible within the class and it's subclass. It is not more usefull in the class.


# name mangling in python
1. Private varibale can be access outside of class by `_classname.__variable_name`. because python change the private variable name. So it is called name mangling.
2. In python we can access variable by name mangling. So python does not follow full concept to encapsulation. 

# video 26 start from zero