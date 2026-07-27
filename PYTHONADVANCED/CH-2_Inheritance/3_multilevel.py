class company:

    title:str = "consultancy"
    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f"company name: {self.company_name} ")
        return f"company name: {self.company_name}"

class manager(company):
    def __init__(self, manager_name:str,company_name:str):
        self.manager_name:str = manager_name
        self.company_name:str = company_name
    def info(self):
        response = company.info(self)
        print(f"manager name:{self.manager_name},{response}")
        return f"manager name:{self.manager_name},{response}"

class employee(manager):
    def __init__(self, employee_name:str,manager_name:str,company_name:str):
        self.employee_name:str = employee_name
        self.manager_name:str = manager_name
        self.company_name:str = company_name

    def info(self):
        response = manager.info(self)
        print(f"employee name: {self.employee_name},{response}")
        return f"employee name: {self.employee_name},{response}"
obj = employee("Abhishek","Ramesh","TCS")
obj.info()