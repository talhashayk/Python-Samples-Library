class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "Name: {},\tEmail: {},\tSalary: {}".format(self.full_name, self.email, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name) - 1

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print("Deleted Name!")
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @ classmethod  # Affects all instances
    def set_raise_amt(cls, amount):  # cls = class
        cls.raise_amount = amount

    @ classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split("-")
        return cls(first_name, last_name, pay)

    @ staticmethod  # Doesn't need to access the class or an instance
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):  # Inherits from Employee

    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_language):
        super().__init__(first_name, last_name, pay)
        self.prog_language = prog_language


class Manager(Employee):  # Inherits from Employee

    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, employee_list=None):
        super().__init__(first_name, last_name, pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list

    def add_emp(self, emp):
        if emp not in self.employee_list:
            self.employee_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee_list:
            self.employee_list.remove(emp)

    def print_employee_list(self):
        for employee in self.employee_list:
            print("--> ", employee.full_name)
