import json
from json import JSONEncoder
from typing import List

class Employee:
    def __init__(self, id, name, salary, department, position, hireDate):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        self.position = position
        self.hireDate = hireDate
    
    def Display(self):
        print(f"Employee Details: Id = {self.id}, Name = {self.name}, Salary = {self.salary}, Department = {self.department}, Position = {self.position}, Hire Date = {self.hireDate}")
    
class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class EmployeeList(object):
    def __init__(self, employees: List[Employee]):
        self.employees = employees

if __name__ == "__main__":
    empObj = Employee(1,"Arun", "2000000", "IT", "Architect","2000-01-01")
    empObj.Display()