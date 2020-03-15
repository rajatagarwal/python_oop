import datetime

class Employee:
    raise_amount = 1.04  # Class variable (common for all the instances)
    num_of_employees = 0    # Initially 0 employees

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@company.com'
        self.pay = pay
        # Since init method runs whenever we create an instance of Employee, this can be a good place to increment num_of_employees counter.
        Employee.num_of_employees += 1  # We must start it with the class value so that it can do tracking at the class level.
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def appy_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # raise_amout is a class variable
        # But you cannot just access raise_amount class variable because you will get undefined error.
        # To access a class variable we need to call it via class: Employee.raise_amount
        # Or via instance itself: self.raise_amount
        # So class variables can be access to the instances by using class or by using instance itself (self)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):    # static method don't take input arguments as cls or self.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    # repr is meant to be developer friendly, that's why we put format in a way that if copy the output of it,  we can just paste it to create new object.
    # if you both have __str__ and __repr__ method in your class, print will always use __str__ first, and __repr__ is used just for fallback.
    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.pay})"
    
    # str is meant to be user friendly. 
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

emp_1 = Employee('Rajat', 'Agrawal', 50000)
emp_2 = Employee('Test', 'User', 56000)

print(emp_1)
print(emp_2)

# Instance variables
# emp_1.first_name = 'Rajat'
# emp_1.last_name = 'Agrawal'
# emp_1.email = 'rajat.agrawal@company.com'
# emp_1.pay = 50000

# emp_2.first_name = 'dqawda'
# emp_2.last_name = 'dac'
# emp_2.email = 'rawad.agdefwwcl@company.com'
# emp_2.pay = 70000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

# Basically when you call a method in a class it passes the Employee instance as a parameter to the method (to tell method which instance this method execution is for). 
# By using above syntax it implicitly passes emp_1 as a parameter when you call fullname() method. So that we must pass "self" as a parameter to the method inside class, 
# otherwise it would throw error like "fullname() takes 0 positional arguments but 1 was given", because emp_1.fullname() implicitly passes emp_1 as an parameter.

# We can do call a method using Employee class as well, but in that case we need to pass emp_1 instance as the parameter explicitly. Both syntaxes mentioned below works exactly same
print(Employee.fullname(emp_1))
print(emp_1.fullname())             # works same as above with less code. 


print(emp_1.pay)
print(emp_1.appy_raise())
print(emp_1.pay)

# We can print namespace for the instances
print(emp_1.__dict__)    # You will see all the instance variables and their values but not the class variable (raise_amount)

# And we can print namespaces for the class
print(Employee.__dict__)  # See raise amount here

# Now you can change the raise_amount for all the employees using class
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("=" * 50)
# You can also change raise_amount for the particular instance using that instance
emp_1.raise_amount = 1.07
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# Now if we run again the namespace for emp_1, this time we will find raise_amount as well
print(emp_1.__dict__)
# So bascially what is happening is that when you call a class variable, at that time instance searches first inside itself if there is any assignment to the class variable,
# if not then it will take value from the class variable.

print(Employee.num_of_employees)

# Regular Methods vs Class Methods vs Static Methods
Employee.set_raise_amount(1.12)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Class methods as Constructor
emp_str_3 = 'Bob-Marley-80000'
emp_3 = Employee.from_string(emp_str_3)
print(Employee.num_of_employees)
print(emp_3.__dict__)

# Static method: The key point of when to use or don't use static method in a class is if in a method you don not need self or cls, then you must declare it as a static method in that class
my_date = datetime.date(2020, 3, 14)            # Saturday
print(Employee.is_workday(my_date))

# Inheritence
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Generally a good approach when you are having single inheritence, makes code clear.
        # OR
        # Employee.__init__(self, first, last, pay)
        # Using class name with the init method is useful when you are having multiple inheritence.
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
            # Now you might be wondering why we didn't pass as an empty list as a argument instead on None at the first place.
            # That's because you never want to pass mutable datatype like list or dictionary as default argument. - Find out why?
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print(f'==> {emp.fullname()}')

# dev1 = Developer('deve', 'loper', 64300)
dev1 = Developer('deve', 'loper', 53266, 'python')

print(dev1.fullname())

# Very useful method to visualize inheritence for a given class
# print(help(Developer))

print(dev1.pay)
dev1.appy_raise()            # It will apply Developer specific raise amount
print(dev1.pay)


man1 = Manager('Mana', 'ger', 256452) # Allow to add without employee coz we have specified employee=None in the init method of the manager.
man1.add_emp(dev1)
man1.print_emp()

man2 = Manager('Big', 'Mana', 555555, [man1, dev1])
# Here we are passing man1 as reportee to man2 because Manager are Employee as well and hence can be managed by others.
print('Big Manager reportees are')
man2.print_emp()
# print(help(Manager))

# Python method isinstance tell if the given value is the instance of the class.
print('is instance test')
print(isinstance(man1, Manager))            # True
print(isinstance(man1, Employee))           # True
print(isinstance(man1, Developer))          # False

# Python method issubclass tells if a class is subclass of another class
print('is sub class test')
print(issubclass(Developer, Employee))      # True
print(issubclass(Developer, object))        # True
print(issubclass(Developer, Manager))       # False

# print(help(ArithmeticError))

# Dunder/Magic Method
# ====================

emp_4 = Employee('Dun', 'Der', 32452)
# print(emp_4)   # <__main__.Employee object at 0x036A9778>       
# So when we do this it prints without having repr and address of the object something like : <__main__.Employee object at 0x036A9778>
# But what if we want to see the actual values instead? We can use 

# repr is used for debugging purpose and really meant to be seen by other developers
# str is more of a readable representation of a object and meant to be used as a display for a user.

# Printing with repr, we try to give structure of the string whcih can be useful for the developers, so in this case if we want to recreate the Employee object
# we can copy the output and use it.
# print(emp_4)  # Employee('Dun', 'Der', 32452)

# Now after adding __str__ method, we get following output
print(emp_4)    # Dun Der - Dun.Der@company.com

# if you still want to print repr, you can call it explicitly
print(repr(emp_4))            # Employee('Dun', 'Der', 32452)
# OR
print(emp_4.__repr__())       # Employee('Dun', 'Der', 32452)

# Similarly you can do for str, but that will be redundant code as by default print will take str into account. Anyway
print(str(emp_4))            # Dun Der - Dun.Der@company.com
print(emp_4.__str__())       # Dun Der - Dun.Der@company.com

# There are other dunder methods as well like __add__. So both str and int have add methods which works differently
# in int 1+2 = 3 but in string 'a' + 'b' = 'ab'

print(int.__add__(1,2))             #3
# equivalent to print(1+2)
print(str.__add__('a', 'b'))        #ab
# equivalent to print('a'+'b')