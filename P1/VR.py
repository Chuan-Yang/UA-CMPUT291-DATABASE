import cx_Oracle
import main
import random
import sys
import os

def VR_main():
    print ("Violation Record")
    print ("----------------------------------")   
    print ("1.Registration of New Violation Record")
    print ("0.Back to the Main Menu")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except :
            print("Invalid input! Please try again")
        finally:
            if (choice > 1) and (choice < 0):
                print ("Invalid input! Please try again")
            else:
                break    
    if choice == 0:
        return 
    if choice == 1:     # Registration of New Violation Record
        reg_NVR()
    
    return



def reg_NVR():
    while True:          # get a new ticket number
        ticket_no = random.randint(0,100000000)
        main.cursor.execute("SELECT t.ticket_no FROM ticket t WHERE ticket_no = %d" %ticket_no)
        exist = main.cursor.fetchone()
        if exist == None:
            print ("The ticket number is: %d" %ticket_no)
            break  

    while True:         # the violate vehicle number
        vehicle_no = input("Please enter the violated vehicle number: ")
        if len(vehicle_no) >15:
            print ("Invalid input! Please try again!")
            continue
        else:
            main.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = '%s'" % vehicle_no)
            exist = main.cursor.fetchone()
            if exist == None:          
                print ("The vehicle with serial_no: %s is not in our database. Please try again!" % vehicle_no)
                continue
            else:
                break            
    
    main.cursor.execute("SELECT owner_id FROM owner WHERE is_primary_owner = 'y' AND vehicle_id = '%s'" %vehicle_no)
    primary_owner = main.cursor.fetchone()
    print ("As for the Vehicle with serial number: %s," %vehicle_no)
    print ("The SIN number of the Primary Owner: %s" %primary_owner)
    while True:
        choice = input("Would you like to register this violation record for the primary owner (Y/N)? ")
        choice = choice.lower()
        if choice != 'y' and choice != 'n':
            print("Invalid input! Please try again!")
            continue
        else:
            if choice == 'n':    
                while True:         # the violator's SIN
                    violator_no = input("Please enter the SIN number of the violator: ")
                    if len(violator_no) >15:
                        print ("Invalid input! Please try again!")
                        continue
                    else:
                        main.cursor.execute("SELECT people.sin FROM people WHERE people.sin = '%s'" % violator_no)
                        exist = main.cursor.fetchone()
                        if exist == None:          
                            print ("The person with SIN: %s doesn't exist. Please try again!" % vioaltor_no)
                            continue
                        else:
                            break
            if choice == 'y':
                for i in primary_owner:
                    violator_no = i
            break
                        
            
    while True:           # the officer's SIN
        officer_id = input("Please enter the SIN number of the officer: ")
        if len(officer_id) >15:
            print ("Invalid input! Please try again!")
            continue
        else:
            main.cursor.execute("SELECT people.sin FROM people WHERE people.sin = '%s'" % officer_id)
            exist = main.cursor.fetchone()
            if exist == None:          
                print ("The person with SIN: %s doesn't exist. Please try again!" % officer_id)
                continue
            else:
                break        
    
    while True:         # ticket type
        main.cursor.execute("SELECT * FROM ticket_type")
        exist = main.cursor.fetchall()             
        print ("Ticket_type")
        print ("--------------------------------")
        ticket_list = []                    
        for row in exist:
            print ("%10s $%.2f" %(row[0].strip(), row[1]))                        
            ticket_list.append(row[0].strip())        
        vtype = input("Please select the ticket type from the above: ")
        if vtype not in ticket_list:
            print("Please enter a Ticket Type from the above")
            continue
        else:
            break
        
    while True:     # violation date
        v_date = input("Please enter the violation date(DD-MMM-YYYY): ")   
        try:
            b_date = v_date.split('-')
            b_date[0] = int(b_date[0])
            b_date[1] = b_date[1].lower()
            b_date[2] = int(b_date[2])
        except:
            print ("Invalid input! Please try again!")
        else:
            if b_date[1] in ('jan','mar','may','jul','aug','oct','dec'):
                if (b_date[0] > 31) or (b_date[0] <= 0):
                    print ("Invalid input! Please try again!")
                    continue
            elif b_date[1] in ('apr','jun','sep','nov'):
                if (b_date[0] > 30) or (b_date[0] <= 0):
                    print ("Invalid input! Please try again!")
                    continue                
            elif b_date[1] == 'feb':
                if b_date[2] % 4 == 0 :
                    if b_date[0] > 30 or (b_date[0] <= 0):
                        print ("Invalid input! Please try again!")
                        continue
                else:
                    if b_date[0] >29 or (b_date[0] <= 0):
                        print ("Invalid input! Please try again!")
                        continue    
            break        
        
    while True:     # violation place 
        place = input("Please enter the violation place: ")
        place = place.lower()
        if len(place) > 20:
            print ("Invlid input! Please try again!")
        else:
            break        
        
    while True:     # violation description
        descriptions = input("Please enter the descriptions for the violation: ")
        descriptions = descriptions.lower()
        if len(descriptions) > 1024:
            print ("Invlid input! Please try again!")
        else:
            break        
        
    print ("INSERT INTO ticket VALUES ("
                    +str(ticket_no)+",'"+str(violator_no)+"','"+str(vehicle_no)+"','"+str(officer_id)+"','"+str(vtype)+"','"+str(v_date)+"','"+str(place)+"','"+str(descriptions)+"')")
    main.cursor.execute("INSERT INTO ticket VALUES ("
                    +str(ticket_no)+",'"+str(violator_no)+"','"+str(vehicle_no)+"','"+str(officer_id)+"','"+str(vtype)+"','"+str(v_date)+"','"+str(place)+"','"+str(descriptions)+"')")    
    
    print("Violation successfully added!")
    tmp = input("Press any key to continue...")
    main.con.commit()       
    
