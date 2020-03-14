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


# We could also do like this to run this.
