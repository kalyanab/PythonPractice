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
    
class contractor(company):
    def __init__(self, contractor_name:str,company_name:str):
        self.company_name:str = company_name
        self.contractor_name:str = contractor_name

    def contractor_info(self):
        response = company.info(self)
        print(f"contractor name: {self.contractor_name},{response}")
obj = employee("Abhishek","TCS")
obj.employee_info()
obj_contractor = contractor("John","TCS")
obj_contractor.contractor_info()
