import csv

class EmployeeManager :
    def __init__(self):
        self.employees = {}
        self.load_from_csv()
        
    def load_from_csv(self):
           try:
               with open("EmployeeManager.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file,delimiter=';')
                for row in reader:
                    emp_id = row["ID"]
                    self.employees[emp_id]={"Name":row["Name"],
                                        "Position":row["Position"],
                                        "Salary":row["Salary"],
                                        "Email":row["Email"]}     
           except FileNotFoundError:
                pass
            
    def save_to_csv(self)    :
        with open("EmployeeManager.csv", mode="w", newline="") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer =csv.DictWriter(file,fieldnames=fieldnames,delimiter=';')
            writer.writeheader()
            
            for emp_id,data in self.employees.items():
                   row={"ID":emp_id,
                        "Name":data["Name"],
                        "Position":data["Position"],
                        "Salary":data["Salary"],
                         "Email":data["Email"]} 
                   writer.writerow(row)
           
           
           
    def add_employee(self)    :
        emp_id=input("enter your ID:  ")
        Name =input("enter your full name:  ")
        Position=input("enter your last position:  ")
        Salary=input("enter your salary:  ")
        Email=input("enter your email:  ")
        try:
            Salary = float(Salary)
        except ValueError:
            print("\n---Salary must be a number.---")
            return

        if emp_id in self.employees:
            print("ID already exist")
            return
            
        else :
            self.employees[emp_id]={
            "Name": Name,
            "Position": Position,
            "Salary": Salary,
            "Email": Email}
            print("Employee added successfully.")

        
        self.save_to_csv()
        
    def view_all_employees(self):
        print("All employee data")
        if len(self.employees)== 0:
            print ("NO employees Exist")
            return
        
        for emp_id,data in self.employees.items():
            print(f"ID: {emp_id}")
            print(f"Name: {data['Name']}")
            print(f"Position: {data['Position']}")
            print(f"Salary: {data['Salary']}")
            print(f"Email: {data['Email']}")

            print("-" * 30)
     
        
    def  update_employee(self):
        emp_id =input("enter the ID of the employee that you want to update:  ")
        
        if emp_id in self.employees:
            employee =self.employees[emp_id]
            print(employee) 
            
            new_name=input("enter the new name (leave blank to keep current):  ")
            if new_name:
                employee["Name"]=new_name
                
            new_position= input("enter the new position (leave blank to keep current):  ")
            if new_position:
                employee["Position"] =new_position
            
            new_Email=input("enter the new email(leave blank to keep current):  ")
            if new_Email:
                employee["Email"] =new_Email
                
            new_salary= input("enter the new Salary(leave blank to keep current):  ")
            if new_salary:
                try:
                     new_salary= float(new_salary)
                     employee["Salary"]= new_salary
                except ValueError:
                     print("Salary must be a number.")
                     return
            print(employee)
            
            self.save_to_csv()
            
            
        else :
            print("Employee does not exist.")
            return
        
            
    
    def delete_employee(self):
        fired= input("enter the ID of the employee you want to delete:  ")
        if fired in self.employees:
            del self.employees[fired]
            print("Employee deleted succesfully")
            self.save_to_csv()
        else:
            print("Employee does not exist")
        
        
        
    def search_employee(self): 
        emp_id =input("enter the employee ID:  ")
        if emp_id in self.employees:
            print(self.employees[emp_id])
      
        else :
            print("Employee does not exist")
   
    
    def exit_program(self):
        print("Exiting the program... Goodbye!")
        exit()
        
if __name__ == "__main__":
    manager = EmployeeManager()    
    while True:
            print("\n-- Employee mangment system ---")
            print("1. add employee")
            print("2.update employee")
            print("3.delete employee")
            print("4.search employee")
            print("5.show all employee")
            print("6.Exit")
            
            choise =input("enter your choise: ")
            if choise == "1":
                manager.add_employee() 
            elif choise == "2":
                manager.update_employee()
            elif choise == "3":
                manager.delete_employee()
            elif choise == "4":
                manager.search_employee()
            elif choise == "5":
                manager.view_all_employees()
            elif choise == "6":
                print("Exiting the program... Goodbye!")
                break

            else:
                print("enter valied numper betweem 1:6")
            

            
            
    