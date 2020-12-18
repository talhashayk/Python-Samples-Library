from Employee_Classes import Employee, Manager, Developer
import datetime

emp_3 = Employee("Tee", "Shayk", 70000)
print(emp_3.email + "\n")

# Same thing
print("{} {}".format(emp_3.first_name, emp_3.last_name))
print(emp_3.full_name)
#print(Employee.full_name(emp_3) + "\n")

print(emp_3.pay)
emp_3.apply_raise()
print(str(emp_3.pay) + "\n")

print(Employee.raise_amount)
print(emp_3.raise_amount)
Employee.raise_amount = 1.05  # Changed for class, i.e. all instances
print(Employee.raise_amount)
print(emp_3.raise_amount)

Employee.set_raise_amt(1.07)  # Changed for class, i.e. all instances
print(Employee.raise_amount)
print(str(emp_3.raise_amount) + "\n")

emp_3.raise_amount = 1.06  # Only changed for instance
print(Employee.raise_amount)
print(str(emp_3.raise_amount) + "\n")


print(str(emp_3.__dict__) + "\n")


emp_1 = Employee("Test", "User", 60000)
emp_2 = Employee("New", "Used", 50000)
print(str(Employee.num_of_emps) + "\n")

emp_strs = ["Tee-Shayk-65000", "Mo-Polio-43000",
            "Kay-Juice-79000", "Aitch-Kay-100000"]

for emp in emp_strs:
    new_emp = Employee.from_string(emp)
    print(new_emp.__dict__)
print()

my_date = datetime.date(2020, 7, 1)
print(str(Employee.is_workday(my_date)) + '\n')

# Uses methods inherited from 'Employee'
dev_1 = Developer("Test", "Developer", 60000, "Python")
dev_2 = Developer("New", "Developer", 70000, "Java")
print(dev_1.__dict__)
print(str(dev_2.__dict__) + "\n")

print(dev_1.pay)
print(dev_2.pay)
dev_1.apply_raise()  # Will use inherited raise amount unless Developer raise amount exists
print(dev_1.pay)
print(dev_2.pay, "\n")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.__dict__)
mgr_1.print_employee_list()
print()
mgr_1.add_emp(dev_2)
mgr_1.print_employee_list()
print()
mgr_1.remove_emp(dev_1)
mgr_1.print_employee_list()

# Can use isinstance and issubclass methods to ascertain inheritance

print("\n" + str(emp_3))
print(repr(emp_3))
print(emp_3)
print(emp_1+emp_2)  # Adds salaries
print(len(emp_3))  # Length of full name

emp_4 = Employee("Big", "Donny", 80000)

print("\n" + emp_4.first_name)
print(emp_4.last_name)
print(emp_4.full_name)
print(emp_4.email)

emp_4.full_name = "Bigger Donner"
print("\n" + emp_4.first_name)
print(emp_4.last_name)
print(emp_4.full_name)
print(emp_4.email)

del emp_4.full_name
print("\n", emp_4.first_name)
print(emp_4.last_name)
print(emp_4.full_name)
print(emp_4.email)
print(emp_4.pay)
