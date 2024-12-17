class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  
        self.department = f"F02 {department}" 
        Manager.mgr_count += 1  
    def display_employee(self):
        """Overrides the display_employee method to include department"""
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

mgr1 = Manager("Tudor Ion", 70000, "HR")
mgr2 = Manager("Pana Alina", 75000, "IT")
mgr3 = Manager("Alex Eli", 9000, "Logistics")
mgr4 = Manager("Popescu Ana", 4500, "Finance")
mgr5 = Manager("Roman Alin", 300, "Customer Service")

print("\nManager 1:")
mgr1.display_employee()

print("\nManager 2:")
mgr2.display_employee()

print("\nManager 3:")
mgr3.display_employee()

print("\nManager 4:")
mgr4.display_employee()

print("\nManager 5:")
mgr5.display_employee()
print("\nNames of Managers :")
def display_names(*employees):
    """Afișează doar numele managerilor cu prefixul F02"""
    for emp in employees:
        if isinstance(emp, Manager): 
            print(f"F02 {emp.name}")

display_names(mgr1, mgr2, mgr3, mgr4, mgr5)


print("\nEmployee count:", Employee.empCount)
print("Manager count:", Manager.mgr_count)


