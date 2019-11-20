class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
        #Use employee not self because the number is for all employee
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('Mark','Russel', 50000)
emp_2 = Employee('Test', 'User', 40000)

emp_2.raise_amount = 1.05

print(emp_1.pay)
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
print(emp_2.raise_amount)
emp_2.apply_raise()
print(emp_2.pay)

print('Total Number of Employee',Employee.num_of_emps)
