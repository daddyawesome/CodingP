class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
        
emp_1 = Employee('Mark','Russel', 50000)
emp_2 = Employee('Test', 'User', 40000)

print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)
