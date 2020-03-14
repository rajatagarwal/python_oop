# Classes and Instances

## Why should we even use classes? 
They allow us to logically group data and functions in a way that's easy to reuse and also easy to build upon if need be.

#### Side Note: 
A function which is associated with a class is known as Method
Data which is associated with a class is known as Attribute

### Example: 
Say we have an application in our company and we wanted to represent employees.
This is a good use case for a class because each company can have many employees and they all share common data and functions. So in programming way, each employee can be represented as a Class as they share same attributes and methods.

Attributes
==========
Name, Email Address
Pay()

Another example, say our company has clients as well.
This is also a good use case for a class because all the clients can share some basic attributes and methods.

##### So a class is basically a blueprint for creating instances.

## Instance Variables and Class Variables
Instances variables contains data that are unique to the instance.

```
class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@company.com'
        self.pay = pay
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

emp_1 = Employee('Rajat', 'Agrawal', 50000)
emp_2 = Employee('Test', 'User', 56000)
```