# from Doctor import Doctor
import matplotlib.pyplot as plt

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print("-----Login-----")

        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        if self.__username==username and self.__password==password:
            return username
    
    def find_index(self,index,doctors):       
        if index in range(0,len(doctors)):         
            return True
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name=input("Enter doctor's First name: ")
        surname=input("Enter doctor's Surname: ")
        speciality=input("Enter doctor's Speciality: ")

        return first_name,surname,speciality
    

    def view_doctors(self):
        print("-----List of Doctors-----")
        try:
            with open("DOCTORS.txt","r") as file:
                doctors=file.readlines()
                if not doctors:
                    print("No doctors registered.")
                    return
                print('ID |          Full name           |  Speciality')
                for index,line in enumerate(doctors):
                    first_name,surname,speciality=line.strip().split(",")
                    print(f"{index+1:<3}|{first_name:>13}{surname:<17}|  {speciality}")
        except FileNotFoundError:
            print("Doctors file not found")


    def view_patient(self):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")

        try:
            with open("PATIENTS.txt","r") as file:
                patients=file.readlines()
                if not patients:
                    print("No patients registered.")
                    return
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
                for index,line in enumerate(patients):
                    parts = line.strip().split(",")
                    if len(parts) < 6:
                        print(f"Skipping malformed line: {line.strip()}")
                        continue

                    full_name = parts[0]
                    doctor_name = parts[1].strip() if parts[1].strip() else "Not Assigned"
                    age = parts[2]
                    mobile = parts[3]
                    Postcode = parts[4]
                    symptom=parts[5]
                    
                    print(f"{index+1:<3}|{full_name:^30}|{doctor_name:^30}|{age:<5}| {mobile:^14}|{Postcode:^8}")
        except FileNotFoundError:
            print("patient file not found")

    def view_patient_by_family():
        with open("PATIENTS.txt", "r") as file:
            lines = file.readlines()

        surname_group = {}
        for line in lines:
            details = line.strip().split(",")  
            if len(details) < 4:
                continue  

            full_name=details[0]
            last_name = full_name.split()[-1]  

            if last_name not in surname_group:
                surname_group[last_name] = [] 
            surname_group[last_name].append((details))

        for last_name,patients in surname_group.items():
            print(f"\nPatients with surname '{last_name}':")
            print('ID |          Full Name           |      Doctor`s Full Name       | Age  |    Mobile     | Postcode ')
            for index,patient in enumerate(patients,start=1):
                print(f"{index:<3}| {patient[0]:^29}| {patient[1]:^30}| {patient[2]:<5}| {patient[3]:^14}| {patient[4]:^8}")
                
    def doctor_management(self):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        print("-----Doctor Management-----")

        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op=input("Enter your choice: ")
        if op.isdigit()==True: 
            op=int(op)

            if op == 1:
                first_name,surname,speciality=self.get_doctor_details()
                print("-----Register-----")

                print('Enter the doctor\'s details:')
                
                with open("DOCTORS.txt","r") as file:
                    doctors=file.readlines()  
                for doc in doctors:
                    try:
                        first_name_from_file,surname_fromfile=doc.strip().split(",")                  
                        if first_name_from_file== first_name() and surname_fromfile == surname():
                            print('Name already exists.')
                            return
                    except ValueError:
                        print(f"Name already exists")
                        continue

                with open ("DOCTORS.txt","a") as file:
                    file.write(f"{first_name}, {surname}, {speciality}\n")                               
                print('Doctor registered.')

            elif op == 2:
                print("-----List of Doctors-----")
                self.view_doctors()
                  
            elif op == 3:
                while True:
                    print("-----Update Doctor`s Details-----")
                    self.view_doctors()
                    try:         
                        with open("DOCTORS.txt","r") as file:
                            doctors=file.readlines() 
                        index = int(input('Enter the ID of the doctor: '))-1
                        doctor_index = self.find_index(index,doctors)
                        if doctor_index!=False:
                            doctor_data=doctors[index].strip().split(",")
                            break
                        else:
                            print(f"Doctor with that ID was not found")

                    except ValueError:
                        print('The ID entered is incorrect. Enter a numeric ID.')

                # menu
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
         
                while True:
                    op = input('Input: ')
                    if op.isdigit()==True: 
                        op=int(op)
                        if op==1:
                            doctor_data[0]=(input("Enter new first name: "))
                            break
                        elif op==2:
                            doctor_data[1]=(input("Enter new surname: "))
                            break
                        elif op==3:
                            doctor_data[2]=(input("Enter new Speciality: "))
                            break
                        else:
                            print("Invalid input, Try 1/2/3")
                    else:
                        print("Enter a valid number")
                doctors[index] = " ,".join(doctor_data) + "\n"
                with open("DOCTORS.txt", "w") as file:
                    file.writelines(doctors)  
            
            elif op == 4:
                print("-----Delete Doctor-----")
                self.view_doctors()
                with open("DOCTORS.txt","r") as file:
                    doctors=file.readlines()
                index = input('Enter the ID of the doctor to be deleted: ')
                if index.isdigit()==True: 
                    index=int(index)-1
                    doctor_index = self.find_index(index,doctors)
                    if 1<=doctor_index<=len(doctors):
                        doctors.pop(doctor_index)

                        with open("DOCTORS.txt","w")as file:
                            file.writelines(doctors)
                        print("Doctor deleted.")
                    else:
                        print(" The id entered was not found")
                else:
                    print("Invalid Input.Please try a valid number.")
            else:
                print("Invalid Input. Try 1/2/3/4 ")
        else:
            print('Invalid operation choosen. Check your spelling!')
    

    def patient_management(self):
        print("-----Patient Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')

        op=input("Enter your choice: ")
        if op.isdigit()==True: 
            op=int(op)

            if op==1:
                print("-----Register Patient-----")
                full_name=input("Enter the paitent's full name: ")
                age=input("Enter the paitent's age: ")
                ph_number=input("Enter the paitent's mobile number: ")
                Postcode=input("Enter the paitent's Postcode: ")
                symptom=input("Enter the paitent's symptom: ")

                with open("PATIENTS.txt","r") as file:
                    doctors=file.readlines()  
                for doc in doctors:
                    try:
                        fullName_from_file=doc.strip().split(",")[0]                 
                        if fullName_from_file== full_name:
                            print('Name already exists.')
                            return
                    except ValueError:
                        print(f"Name already exists")
                        continue
                
                with open ("PATIENTS.txt","a") as file:
                    file.write(f"{full_name}, , {age}, {ph_number}, {Postcode}, {symptom}\n")                               
                print('New patient registered.')

            if op==2:
                self.view_patient()
            
            else:
                print("Invalid input range. Try 1/2 ")
        else:
            print("Invalid input. Try a valid number.")


    def assign_doctor_to_patient(self):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        self.view_patient()

        patient_index = input('Please enter the patient ID: ')
        with open("PATIENTS.txt","r") as file:
            patients=file.readlines()
        try:
            patient_index = int(patient_index) -1
        except ValueError:
            print('The ID entered is incorrect. Please enter a number.')
            return 
        if patient_index>= len(patients)-1:  
            print('The ID entered was not found.')
            return 
        
        patient_details = patients[patient_index].strip().split(",")

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patient_symptom=patient_details[-1]
        print(patient_symptom)

        print('--------------------------------------------------')
        self.view_doctors()
        doctor_index = input('Please enter the doctor ID: ')
        with open("DOCTORS.txt","r") as file:
            doctors=file.readlines()
        try:
            doctor_index = int(doctor_index) -1
            if self.find_index(doctor_index,doctors)!=False:
                    
                doctor_details = doctors[doctor_index].strip().split(",")
                dr_name=f'{doctor_details[0]} {doctor_details[1]}'
                patient_details[1] = dr_name

                patients[patient_index] = ", ".join(patient_details) + "\n"
                with open("PATIENTS.txt", "w") as file:
                    file.writelines(patients)
                
                print('The patient is now assign to the doctor.')

            else:
                print('The id entered was not found.')

        except ValueError:
            print('The id entered is incorrect')


    def discharge(self):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        while True:
            print("-----Patients-----")
            self.view_patient()
            op=input("Do you want to discharge a patient(Y/N): ").upper()
            if op=="Y":
                print("-----Discharge Patient-----")
                try:
                    with open("PATIENTS.txt","r") as file:
                        patients=file.readlines()
                    patient_index = int(input('Please enter the patient ID: '))
                    bp=input("Do you want to discharge a patient(Y/N): ").upper() 
                    if bp=="Y":   
                        if 1<=patient_index<=len(patients):
                            del_patient=patients.pop(patient_index-1)
                            with open("DISCHARGED_PATIENTS.txt", "a") as file:
                                file.writelines(del_patient)  
                                print(f"Patient {del_patient[0]} has been discharged.")
                            with open("PATIENTS.txt", "w") as file:
                                file.writelines(patients)    
                        else:
                            print("Invalid patient ID. Please enter a valid ID.")
                    elif bp=="N":
                        print("No more discharging. Exiting..")
                        break
                    else:
                        print("Invalid option. Choose (Y/N)")

                except ValueError:
                    print("invalid input. Please enter a numeric patient ID")
            elif op=="N":
                print("No more discharging. Exiting..")
                break
            else:
                print("Invalid option. Choose (Y/N)")
        
    def view_discharge(self):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        try:
            with open("DISCHARGED_PATIENTS.txt","r") as file:
                dis_patients=file.readlines()
                if not dis_patients:
                    print("No patients registered.")
                    return 
                print("Discharged Patients:")  
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
                for index,line in enumerate(dis_patients):
                    for index,line in enumerate(dis_patients):
                        parts = line.strip().split(",")
                        
                        if len(parts) < 6:
                            print(f"Skipping malformed line: {line.strip()}")
                            continue

                        full_name = parts[0]
                        doctor_name = parts[1].strip() if parts[1].strip() else "Not Assigned"
                        age = parts[2]
                        mobile = parts[3]
                        Postcode = parts[4]
                        symptom=parts[5]
                    
                        print(f"{index+1:<3}|{full_name:^30}|{doctor_name:^30}|{age:<5}| {mobile:^14}|{Postcode:^8}")
        except FileNotFoundError:
            print("patient file not found")

    def report(self):
        print("-----Management Report-----")
        print('Choose the report you want to view:')
        print(' 1 - Total number of doctors in the system')
        print(' 2 - Total number of patient per doctor')
        print(' 3 - Total number of appointments per month per doctor')
        print(' 4 - Total number of patients based on the illness type')

        op=input("Input: ")
        if op.isdigit()==True:
            op=int(op)

            if op==1:
                height=1
                self.view_doctors()
                with open("DOCTORS.txt","r") as file:
                    doctors=file.readlines()
                line_count = len(doctors) 
                print(f'Total number of doctors in the system are "{line_count}"')
            
                plt.figure(figsize=(1, 4))
                plt.bar(1,line_count, color='skyblue')
                plt.xlabel("Doctors",fontsize=12, fontweight='bold')
                plt.ylabel("Total No. of doctors",fontsize=12, fontweight='bold')
                plt.show()

            elif op==2:
                print("-----Total number of patients per doctor-----")
                with open("PATIENTS.txt","r") as file:
                    patients=file.readlines()
                dr_per_patient = {}
 
                for line in patients:
                    
                    patient_details = line.strip().split(",") 
                    if len(patient_details) < 2:
                        continue 
                    doctor_name = patient_details[1].strip() 
                    if doctor_name == '':
                        continue 

                    if doctor_name in dr_per_patient:
                        dr_per_patient[doctor_name] += 1 
                
                    else:
                        dr_per_patient[doctor_name] = 1   
                for doctor, count in dr_per_patient.items():
                    print(f"Dr. {doctor}: {count} patients")

                doctors = list(dr_per_patient.keys())
            
                patient_counts = list(dr_per_patient.values())

                plt.figure(figsize=(6, 4))
                plt.bar(doctors, patient_counts, color='skyblue')
                plt.xlabel("Doctors",fontsize=12, fontweight='bold')
                plt.ylabel("Number of Patients",fontsize=12, fontweight='bold')
                plt.title("Number of Patients Per Doctor",fontsize=12, fontweight='bold')
                plt.xticks(rotation=20)
                plt.show()
                
            elif op==3:
                print("-----Total number of appointments per month per doctor-----")
                with open("PATIENTS.txt","r") as file:
                    patients=file.readlines()
                dr_per_patient = {}
 
                for line in patients:
                    
                    patient_details = line.strip().split(",") 
                    if len(patient_details) < 2:
                        continue 
                    doctor_name = patient_details[1].strip() 
                    if doctor_name == '':
                        continue 

                    if doctor_name in dr_per_patient:
                        dr_per_patient[doctor_name] += 1 
                
                    else:
                        dr_per_patient[doctor_name] = 1   
                for doctor, count in dr_per_patient.items():
                    print(f"Dr. {doctor} had {count} appointments this month")

                doctors = list(dr_per_patient.keys())
            
                patient_counts = list(dr_per_patient.values())

                plt.figure(figsize=(6, 4))
                plt.bar(doctors, patient_counts, color='skyblue')
                plt.xlabel("Doctors",fontsize=12, fontweight='bold')
                plt.ylabel("Monthly Appointment",fontsize=12, fontweight='bold')
                plt.title("Total number of appointments per month per doctor",fontsize=12, fontweight='bold')
                plt.xticks(rotation=20)
                plt.show()
                
            elif op==4:
                print("-----Total number of patients based on the illness type-----")
                with open("PATIENTS.txt","r") as file:
                    patinets=file.readlines()
                symptom_per_patinet = {}

                for line in patinets:
                    
                    patient_details = line.strip().split(",")  
                    if len(patient_details) < 2:
                        continue
                    symptom_of_patinet = patient_details[-1].strip()  
                    if symptom_of_patinet == '':
                        continue

                    if symptom_of_patinet in symptom_per_patinet:
                        symptom_per_patinet[symptom_of_patinet] += 1 
                    else:
                        symptom_per_patinet[symptom_of_patinet] = 1 

                for symptom,patinet in symptom_per_patinet.items():
                    print(f" {symptom}: {patinet} patients")
                
                symptoms = list(symptom_per_patinet.keys())
                patient_counts = list(symptom_per_patinet.values())

                plt.figure(figsize=(6, 4))  # 8 inches wide, 5 inches tall
                plt.bar(symptoms, patient_counts, color='lightcoral')
                plt.xlabel("Illness Type", fontsize=12, fontweight='bold')
                plt.ylabel("Number of Patients", fontsize=12, fontweight='bold')
                plt.title("Number of Patients Per Illness Type", fontsize=14, fontweight='bold')
                plt.xticks(rotation=20)
                plt.show()
                
            else:
                print("Enter a number 1/2/3/4")


        else:
            print("Enter a valid Number")

    def relocate_doctor(self):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Relocate Doctor-----")

        print("-----Patients-----")
        self.view_patient()

        patient_index = input('Please enter the ID in which you want to relocate the doctor: ')
        with open("PATIENTS.txt","r") as file:
            patients=file.readlines()
        try:
            patient_index = int(patient_index) -1

            if patient_index>= len(patients)-1:
                print('The id entered was not found.')
                return 

        except ValueError:
            print('The id entered is incorrect')
            return
        
        patient_details = patients[patient_index].strip().split(",")

        print("-----Doctors Select-----")
       
        print('--------------------------------------------------')
        self.view_doctors()
        doctor_index = input('Please enter the doctor ID whom you want to relocate: ')
        with open("DOCTORS.txt","r") as file:
            doctors=file.readlines()
        try:
            doctor_index = int(doctor_index) -1
        except ValueError:
            print('The ID entered is incorrect. Please enter a number.')
            return 
        if patient_index>= len(patients)-1:  
            print('The ID entered was not found.')
            return     

        try:
            doctor_index = int(doctor_index) -1
            if self.find_index(doctor_index,doctors)!=False:
                doctor_details = doctors[doctor_index].strip().split(",")
                dr_name=f'{doctor_details[0]} {doctor_details[1]}'
                patient_details[1] = dr_name

                patients[patient_index] = ", ".join(patient_details) + "\n"
                with open("PATIENTS.txt", "w") as file:
                    file.writelines(patients)
                
                print('New doctor has been assigned to the patient.')

            else:
                print('The id entered was not found.')
                return

        except ValueError: 
            print('The id entered is incorrect')    

    def update_details(self):
            """
            Allows the user to update and change username, password and address
            """
            try:         
                with open("LOGIN.txt","r") as file:
                    user=file.readline().strip()
                    user_data=user.split(",")
                    while len(user_data) < 3:
                        user_data.append("")
                    
            except FileNotFoundError: 
                print('Error: LOGIN.txt file not found.')

            print('Choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            while True:
                op = input('Input: ')
                if op.isdigit()==True: 
                    op=int(op)
                    if op==1:
                        user_data[0]=(input("Enter new Username: "))
                        break
                    elif op==2:
                        user_data[1]=(input("Enter new Password: "))
                        break
                    elif op==3:
                        user_data[2]=(input("Enter new Address: "))
                        break
                    else:
                        print("Invalid input, Try 1/2/3")
                else:
                    print("Enter a valid number")
            new_user_data= " ,".join(user_data) + "\n"
            with open("LOGIN.txt", "w") as file:
                file.writelines(new_user_data)   

       

