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
    
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        cls.raise_amt = amount
    
    
emp_1 = Employee('Mark','Russel', 50000)
emp_2 = Employee('Test', 'User', 40000)

emp_str_1 = 'Daddy-Awesome-20000'
emp_str_2 = 'John-Doe-11500'
emp_str_3 = 'Jane-Doe-40500'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
 
print('Total Number of Employee',Employee.num_of_emps)
