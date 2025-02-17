from Admin import Admin

def main():
    """
    the main function to be ran when the program runs
    """

    with open('LOGIN.txt', 'r') as file:
        line = file.readline().strip()  
        admin_data = line.split(',')
        admin_username = admin_data[0]
        admin_password = admin_data[1]
        admin_address = admin_data[2]
    admin = Admin(admin_username,admin_password,admin_address)
    
    while True:
        if admin.login():
            running = True
            print("Login Successful") 
            break
        else:
            print('Incorrect username or password.')

    while running:
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/ View patients')
        print(' 3- Discharge patients')
        print(' 4- View discharged patient')
        print(' 5- Assign doctor to a patient')
        print(' 6- Update admin detais')
        print(' 7- Quit')
        print(' 8- View patients by family')
        print(' 9- View Management report')
        print('10- Relocate doctor')

        op = input('Option: ')
        
        if op == '1':
          admin.doctor_management()

        if op=='2':
            admin.patient_management()

        elif op == '3':            
            admin.discharge()

        elif op == '4':
            admin.view_discharge()

        elif op == '5':
            admin.assign_doctor_to_patient()

        elif op == '6':
            admin.update_details()

        elif op == '7':
            print("Quitting..")
            break
        
        elif op=='8':
            Admin.view_patient_by_family()

        elif op=='9':
            Admin.report(admin)
        
        elif op=='10':
            admin.relocate_doctor()
        else:
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
