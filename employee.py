"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType,commisionType):
        self.name = name
        self.contractType=contractType
        self.commisionType=commisionType


    def get_pay(self):
        pass

    def __str__(self):
        return self.name
class HourlyEmployee(Employee):
    def __init__(self, name, contractType, commisionType):
        super().__init__(name, contractType, commisionType)
    
class SalaryEmployee(Employee):
    def __init__(self, name, contractType, commisionType):
        super().__init__(name, contractType, commisionType)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','Salary','None')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','Hourly','None')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','Salary','Commision')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','Hourly','Commision')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','Salary','Bonus')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','Hourly','Bonus')
