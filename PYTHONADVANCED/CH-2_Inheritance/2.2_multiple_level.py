class company:

    title:str = "consultancy"
    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f"company name: {self.company_name} ")
        return "company name: {self.company_name}"
class client_company:
    title:str = "client"
    def __init__(self,client_company_name:str):
        self.client_company_name:str = client_company_name

    def info(self):
        print(f"client company name: {self.client_company_name} ")
        return "client company name: {self.client_company_name}"
class employee(company,client_company):
    def __init__(self, employee_name:str,company_name:str,client_company_name:str):
        self.company_name:str = company_name
        self.client_company_name:str = client_company_name
        self.employee_name:str = employee_name

    def employee_info(self):
        response = company.info(self)
        response1 = client_company.info(self)
        print(f"employee name: {self.employee_name},{response},{response1}")
        return f"employee name: {self.employee_name},{response},{response1}"

obj =employee("Abhi","Infosys","TCS")
obj.employee_info()


