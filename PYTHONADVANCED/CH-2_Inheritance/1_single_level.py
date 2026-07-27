class company:

    title:str = "consultancy"
    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
       # print(f"company name: {self.company_name} ")
        return "company name: {self.company_name}"

class employee(company):
    def __init__(self, employee_name:str,company_name:str):
        self.company_name:str = company_name
        self.employee_name:str = employee_name

    def employee_info(self):
        response = company.info(self)
        print(f"employee name: {self.employee_name},{response}")
    
obj = employee("Abhishek","TCS")
obj.employee_info()
