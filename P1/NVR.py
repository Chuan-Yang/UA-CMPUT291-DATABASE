import sys
import cx_Oracle
import main

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

def New_Vehicle_Registraion():
    primary_owner=[]
    secondary_owner=[]
               
    flag = True
    while flag:
        serial_no=input("Enter serial number: ")
        if len(serial_no)>=15 or len(serial_no)<=0:
            print("invalid inputs")
        else:
            if is_exist_car(serial_no):
                print("vehicle already existed, try agian")
            else:
                flag=False

    flag = True
    while flag:
        maker=input("Enter maker: ")
        if len(maker)>=20 or len(maker)<=0:
            print("invalid inputs")
        else:
            flag=False
    
    flag = True    
    while flag:
        model=input("Ener model: ")
        if len(model)>=20 or len(model)<=0:
            print("invalid inputs")
        else:
            flag=False
    
    flag = True    
    while flag:
        year=input("Enter year: ")
        if len(year)!=4:
            print("invalid inputs")
        else:
            flag=False
          
    
    flag = True        
    while flag:
        color=input("Enter color: ")
        if len(color)>20 or len(color)<=0:
            print("Error")
        else:
            flag=False
    
    main.cursor.execute("select type, type_id FROM vehicle_type")
    data = main.cursor.fetchall()
    vehicleType = dict((x.lower().strip(),y) for x,y in data)
    while True:
        vtype = input("Please enter the type of the vehicle ").lower()
        if vtype in vehicleType:
            type_id = vehicleType.get(vtype)
            break
        else: 
            print("Error: invalid vehicle type")    

    flag = True
    while flag:
        user_input1=input("Do you want add an owner for this vehicle? (y/n): ").lower()     
        if user_input1=="y":
            owner_id=input("Enter onwer id: ")
            primary=input("Is a primary owner? (y/n): ").lower()        
            if is_exist_person(owner_id):
                if primary =='y':
                    primary_owner.append(owner_id)
                elif primary=='n':
                    secondary_owner.append(owner_id)
                else:
                    print("Error, please try again")
            else:
                print("This person isn't in database, register this person.")
                reg_person()
                if primary =='y':
                    primary_owner.append(owner_id)
                elif primary=='n':
                    secondary_owner.append(owner_id)
                else:
                    print("Error, please try again")                
        elif user_input1=="n" and len(primary_owner)==0:
            print("Error, you have to have a primary owner for this vehicle.")
        elif user_input1 =="n" and len(primary_owner)>0:
            flag= False
        else:
            print("Error, please Enter y/n")
 
             
    try:

        main.cursor.execute(" insert into vehicle values('" + str(serial_no) + "','" + str(maker) +"','" + str(model) + "'," + str(year) + ",'" + str(color) + "'," + str(type_id) + ")")
    except:
        print("Sql error, try again.")
   
    for i in primary_owner:
        try:
            main.cursor.execute("insert into owner values('" + str(i) +"','" + str(serial_no) +"','y')")
        except:
            print("sql error, try again. ")
    
    for i in secondary_owner:
        try:
            main.cursor.execute("insert into owner values('" + str(i) +"','" + str(serial_no) +"','n')")
        except:
            print("sql error, try again. ")    
    
    
                   
def is_exist_car(serial_no):
    main.cursor.execute("select serial_no from vehicle where serial_no = '"+serial_no+"'")
    rows = main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True    


def is_exist_person(owner_id):
    main.cursor.execute("select owner_id from owner where owner_id = '"+owner_id+"'")
    rows=main.cursor.fetchone()
    if rows==None:
        return False
    else:
        return True


def NVR_main():
    print ("----------------------------------")
    print ("Registration for New vehicle")
    New_Vehicle_Registraion()
    print("registration finished")
    while True:
        user_input2=input("Do you want to register another car?(1/0) ").lower()
        print ("1. register a new car")
        print ("0. Back to the Main Menu")        
        if user_input2==1 or user_input2==0:
            if user_input2==1:
                New_Vehicle_Registraion()
            else:
                print("exit to main menu")
                main.main_menu()
        else:
            print("invalid input, try again")
            