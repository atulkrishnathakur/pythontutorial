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