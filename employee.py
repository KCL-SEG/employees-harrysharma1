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
        return f'{self.name} works on a '
    
class ContractEmployee(Employee):
    def __init__(self, name, contractType, commisionType,hourlyRate,hoursWorked):
        super().__init__(name, contractType, commisionType)
        self.hourlyRate=hourlyRate
        self.hoursWorked=hoursWorked
    def get_pay(self):
        return self.hourlyRate*self.hoursWorked
    def __str__(self):
        return f'{super().__str__()}contract of {self.hoursWorked} hours at {self.hourlyRate}/hour.  Their total pay is {self.get_pay()}.'
    
class SalaryEmployee(Employee):
    def __init__(self, name, contractType, commisionType,monthlyRate):
        super().__init__(name, contractType, commisionType)
        self.monthlyRate=monthlyRate
    def get_pay(self):
        return self.monthlyRate
    def __str__(self):
        return f'{super().__str__()}monthly salary of {self.monthlyRate}.  Their total pay is {self.get_pay()}.'
    
    
class ContractComission_S(SalaryEmployee):
    def __init__(self, name, contractType, commisionType, monthlyRate,contracts,contractRate):
        super().__init__(name, contractType, commisionType, monthlyRate)
        self.contracts=contracts
        self.contractRate=contractRate
    def get_pay(self):
        return super().get_pay()+(self.contracts*self.contractRate)
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.monthlyRate} and receives a commission for {self.contracts} contract(s) at {self.contractRate}/contract.  Their total pay is {self.get_pay()}.'
        
class ContractComission_C(ContractEmployee):
    def __init__(self, name, contractType, commisionType, hourlyRate, hoursWorked, contracts,contractRate):
        super().__init__(name, contractType, commisionType, hourlyRate, hoursWorked)
        self.contracts=contracts
        self.contractRate=contractRate
    def get_pay(self):
        return super().get_pay()+(self.contracts*self.contractRate)
    def __str__(self):
        return f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyRate}/hour and receives a commission for {self.contracts} contract(s) at {self.contractRate}/contract.  Their total pay is {self.get_pay()}.'
        
class BonusComission_S(SalaryEmployee):
    def __init__(self, name, contractType, commisionType, monthlyRate,bonus):
        super().__init__(name, contractType, commisionType, monthlyRate)
        self.bonus=bonus
    def get_pay(self):
        return super().get_pay()+self.bonus
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.monthlyRate} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'
        
        
class BonusComission_C(ContractEmployee):
    def __init__(self, name, contractType, commisionType, hourlyRate, hoursWorked,bonus):
        super().__init__(name, contractType, commisionType, hourlyRate, hoursWorked)
        self.bonus=bonus
    def get_pay(self):
        return super().get_pay()+self.bonus
    def __str__(self):
        return f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyRate}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie','Salary','None',4000)
# print(f'{billie.get_pay()}')
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie','Hourly','None',25,100)
# (print(f'{charlie.get_pay()}'))
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = ContractComission_S('Renee','Salary','Commision',3000,4,200)
# print(f'{renee.get_pay()}')
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractComission_C('Jan','Hourly','Commision',25,150,3,220)
# (print(f'{jan.get_pay()}'))
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = BonusComission_S('Robbie','Salary','Bonus',2000,1500)
# print(f'{robbie.get_pay()}')
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel =BonusComission_C('Ariel','Hourly','Bonus',30,120,600)
# print(f'{ariel.get_pay()}')
print(str(ariel))