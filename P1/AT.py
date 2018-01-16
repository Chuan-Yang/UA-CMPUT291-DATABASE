import sys
import cx_Oracle
import main
import NVR

def reg_person():
    print ("----------------------------------")
    print ("Registration of New Person")    
    while True:     # sin
        sin = input("Please enter the SIN number: ")
        if len(sin) >15:
            print ("Invalid input! Please try again!")
            continue
        else:
            main.cursor.execute("SELECT people.sin FROM people WHERE people.sin = '%s'" % sin)
            exist = main.cursor.fetchone()
            if exist == None:   # success
                break   
            else:
                print ("The sin number: "+str(sin)+" has already exsited. Please try agian!")
                continue
            
    while True:     #name
        name = input("Please enter the NAME: ")
        if len(name) > 40:
            print ("Invalid input! Please try again!")
            continue        
        else:
            break
        
    while True:     # height
        try:
            height = float(input("Please enter the HEIGHT(cm): "))
        except :
            print ("Invalid input! Please try again!")
            continue                    
        else:
            if height > 300:        # too high
                print ("Invalid input! Please try again!")
                continue        
            else:
                break        
        
    while True:     # weight
        try:
            weight = float(input("Please enter the WEIGHT(kg): "))
        except :
            print ("Invalid input! Please try again!")
            continue                    
        else:
            break
            
    while True:     # eye color
        eyecolor = input("Please enter the EYECOLOR: ")
        if len(eyecolor) > 10:
            print ("Invalid input! Please try again!")
            continue        
        else:
            break
        
    while True:     # hair color
        haircolor = input("Please enter the HAIRCOLOR: ")
        if len(haircolor) > 10:
            print ("Invalid input! Please try again!")
            continue        
        else:
            break    
    
    while True:     # addr
        addr = input("Please enter the ADDRESS: ")
        if len(addr) > 50:
            print ("Invalid input! Please try again!")
            continue        
        else:
            break        
        
    while True:     # gender
        gender = input("Please enter the GENDER(m/f): ")
        if gender != 'm' and gender != 'f':
            print ("Invalid input! Please try again!")
            continue        
        else:
            break    
        
    while True:     # insert
        date = input("Please enter the BIRTHDAY(DD-MMM-YYYY): ")   
        try:
            b_date = date.split('-')
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
                    if b_date[0] >30 or (b_date[0] <= 0):
                        print ("Invalid input! Please try again!")
                        continue
                else:
                    if b_date[0] >29 or (b_date[0] <= 0):
                        print ("Invalid input! Please try again!")
                        continue    
            break
        
    #insert = "INSERT INTO people (SIN,NAME, HEIGHT, WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY) VALUES ("
    #+str(sin)+','+str(name)+','+str(height)+','+str(weight)+','+str(eyecolor)+','+str(haircolor)+','+str(addr)+','
    #+str(gender)+','+str(date)+");"

    
    main.cursor.execute("INSERT INTO people (SIN,NAME, HEIGHT, WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY) VALUES ('"
    +str(sin)+"','"+str(name)+"',"+str(height)+","+str(weight)+",'"+str(eyecolor)+"','"+str(haircolor)+"','"+str(addr)+"','"
    +str(gender)+"','"+str(date)+"')")
    main.con.commit()  
    
    print("Person successfully added!")
    tmp = input("Press any key to continue...")
   
    return

def Auto_transacation():
    while True:
        transaction_id=input("Please enter the transaction_id: ")
        try:
            transaction_id=int(transaction_id)
            if is_exist_transaction(transaction_id):
                print("transaction_id already existed, please enter another one")
            else:
                break
        except ValueError:
            print("Value Error")
    while True:
        vehicle_id=input("Plesse enter the vehicle id: ")
        if(len(vehicle_id)>15):
            print("Please enter a valid input. ")
        else:
            if is_exist_car(vehicle_id):
                break
            else:
                userinput1=("This vehicle does't register, register it now?(y/n): ").lower()
                if userinpu1=='y':
                    NVR.NVR_main()
                else:
                    print("Plese try again. ")
    
    while True:
        seller_id=input("Please enter the seller_id: ").lower()
        if(len(seller_id)>15):
            print("Please enter a valid input. ")
        else:            
            if is_exist_person(seller_id):
                if is_owner(seller_id):
                    break
                else:
                    print("This person doesn't own this vehicle, try again")
            else:
                print("this person doesn't register.")
            
    while True:
        primary_buyer_id=input("Please enter the primary buyer's id: ")
        if(len(primary_buyer_id)>15):
            print("Please enter a valid input. ")
        else:                
            if is_exist_person(primary_buyer_id):
                break
            else:
                userinput2=input("This person doen't register, register now? (Enter y to continue): ").lower()
                if userinput2=='y':
                    reg_person()
                else:
                    print("Please enter a exist buyer's id. ")
    while True:
        buyers=[]
        is_other_buyers=input("Do you want to add a secondary buyer? (Enter y to continue): ").lower()
        if is_other_buyers=='y':
            secondary_buyers_id=input("Please enter the secondary buyer's id: ")
            if is_exist_person(secondary_buyers_id):
                buyers.append(secondary_buyers_id)
            else:
                userinput2=input("This person doen't register, register now? (Enter y to continue): ").lower()
                if userinput2=='y':
                    reg_person()
                    buyer.append(secondary_buyers_id)
                else:
                    print("Please enter a exist buyer's id. ")                
        else:
            break

        
    while True:
        price=input("Please enter the price : ")
        if( len(price) <= 9):
                    break;
        else:
            print("Error: value too large")

    
    while True:     # sale date
        s_date = input("Please enter the sale date(DD-MMM-YYYY): ")   
        try:
            b_date = s_date.split('-')
            b_date[0] = int(b_date[0])
            b_date[1] = b_date[1].lower()
            b_date[2] = int(b_date[2])
        except:
            print ("Invalid input! Please try again!")
        else:
            if b_date[1] in ('jan','mar','may','jul','aug','oct','dec'):
                if (b_date[0] > 31 or b_date[0]<=0):
                    print ("Invalid input! Please try again!")
                    continue
            elif b_date[1] in ('apr','jun','sep','nov'):
                if (b_date[0] > 30 or b_date[0]<=0):
                    print ("Invalid input! Please try again!")
                    continue                
            elif b_date[1] == 'feb':
                if b_date[2] % 4 == 0 :
                    if b_date[0] >29 or b_date[0]<=0:
                        print ("Invalid input! Please try again!")
                        continue
                else:
                    if b_date[0] >29 or b_date[0]<=0:
                        print ("Invalid input! Please try again!")
                        continue    
            break        


    main.cursor.execute("DELETE FROM owner WHERE ( owner_id ="+str(seller_id)+")")
    main.cursor.execute(" insert into auto_sale values('" + str(transaction_id) + "','" + str(seller_id) +"','" + str(primary_buyer_id) + "','" + str(vehicle_id) + "','" + str(s_date) + "','" + str(price) + "')")
    for i in range(len(buyers)):
        if i==0:
            main.cursor.execute(" insert into owner values('" + str(buyers[0]) + "','" + str(vehicle_id) + "','y')")
        else:
            main.cursor.execute(" insert into owner values('" + str(buyers[0]) + "','" + str(vehicle_id) + "','n')")

def is_exist_transaction(transaction_id):
    main.cursor.execute("select transaction_id from auto_sale where transaction_id = '"+str(transaction_id)+"'")
    rows=main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True
                   
def is_exist_car(serial_no):
    main.cursor.execute("select serial_no from vehicle where serial_no = '"+serial_no+"'")
    rows = main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True    

def is_owner(Id):
    main.cursor.execute("select owner_id from owner where owner_id = '"+Id+"'")
    rows=main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True
def is_exist_person(Id):
    main.cursor.execute("select sin from people where sin = '"+Id+"'")
    rows=main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True
    
    
def Auto_sale_main():
    print ("----------------------------------")
    print ("welcome to Auto sale ")    
    Auto_transacation()
    print("transaction finished")
    while True:
        user_input=input("Do you want to make another transaction? ").lower()
        print ("1. make a new transaction")
        print ("0. Back to the Main Menu")
        if user_input==1 or user_input==0:
            if user_input2==1:
                New_Vehicle_Registraion()
            else:
                print("exit to main menu")
                main.main_menu()
        else:
            print("invalid input, try again")    