import cx_Oracle
import main
import random

def DLR_main():
    print ("Driver Licence Registration")
    print ("----------------------------------")
    print ("1.Registration of New Person")
    print ("2.Registration of New Driver")
    print ("0. Back to the Main Menu")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except TypeError:
            print("Invalid input! Please try again")
        finally:
            if (choice > 3) and (choice <0):
                print ("Invalid input! Please try again")
            else:
                break
    
    if choice == 0:
        return 
    if choice == 1:     #Registration of New Person
        reg_person()
    if choice == 2:
        reg_licence()
        
    return                  # return to the main menu

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


def reg_licence():
    print ("----------------------------------")
    print ("Registration of New Licence")
    
    while True:         # sin
        sin = input("Please enter the SIN number of the new driver: ")
        if len(sin) >15:
            print ("Invalid input! Please try again!")
            continue
        else:
            main.cursor.execute("SELECT people.sin FROM people WHERE people.sin = '%s'" % sin)
            exist = main.cursor.fetchone()
            if exist == None:  
                print ("The person with SIN: "+str(sin)+" is not in the database")
                while True:
                    c = input("Would you like to add this person to the database(Y/N)? ")
                    if c == 'Y' or c == 'y':
                        reg_person()
                        break
                    elif c == 'N' or c == 'n':
                        print ("Please try again!")
                        break
                    else:
                        print ("Invalid choice! Please try again!")
                        continue
            else:
                main.cursor.execute("SELECT drive_licence.sin FROM drive_licence WHERE drive_licence.sin = '%s'" % sin)
                d_exist = main.cursor.fetchone()
                if d_exist == None:
                    break
                else:
                    print ("The person has already got a driver licence! Please try again!")
                    continue
    
    while True:     # licence_no
        licence = input("Please enter the licence number: ")
        if len(licence) >15:
            print ("Invalid input! Please try again!")
            continue
        else:        
            main.cursor.execute("SELECT licence_no FROM drive_licence WHERE licence_no = '%s'" % licence)
            exist = main.cursor.fetchone()
            if exist == None:
                break
            else:
                print ("The person with licence number: "+str(licence)+" has already existed! Please try again")
                continue
        
    while True:
        try :   
            class_lv = int(input("Please enter the class of the driver licence(1-7): "))
        except :
            print ("Invalid Input!Please try agian")
        else:
            if class_lv > 7 and class_lv < 1:
                print ("Invalid Input!Please try agian")
                continue
            else:
                class_lv = 'Class' + str(class_lv)
                break
            
    while True:     # issuing date
        i_date = input("Please enter the issuing date(DD-MMM-YYYY): ")   
        try:
            b_date = i_date.split('-')
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
        
    while True:     # expiring date
        e_date = input("Please enter the expiring date(DD-MMM-YYYY): ")   
        try:
            b_date = e_date.split('-')
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
    
    while True:
        photo = input("Please enter the name of the photo(include the extension, like *.jpg, etc.): ")
        try:
            f_image = open(photo,'rb')
            break
        except IOError:
            print("File could not be opened. Please try again!")
            continue

    image = f_image.read()        
    
    
    while True:     # driving condition
        d_condition = input("Please enter the driving condition (None for no records): ")
        d_condition = d_condition.lower()
        if len(d_condition) > 1024:
            print ("Invlid input! Please try again!")
        else:
            break
        
    while True:
        c_id = random.randint(0,100000000)
        main.cursor.execute("SELECT c_id FROM driving_condition WHERE c_id = %d" %c_id)
        exist = main.cursor.fetchone()
        if exist == None:
            break
    
    main.cursor.execute("INSERT into DRIVE_LICENCE (LICENCE_NO, SIN, CLASS, PHOTO, ISSUING_DATE, EXPIRING_DATE)"
    +"values (:LICENCE_NO, :SIN, :CLASS, :PHOTO, :ISSUING_DATE, :EXPIRING_DATE)",{'LICENCE_NO':licence,'SIN':sin,'CLASS':class_lv,'PHOTO':image,'ISSUING_DATE':i_date,'EXPIRING_DATE':e_date})  
        
    main.cursor.execute("INSERT into DRIVING_CONDITION (C_ID,DESCRIPTION) "
    +"values (:C_ID,:DESCRIPTION)", {'C_ID':c_id,'DESCRIPTION':d_condition})

    main.cursor.execute("INSERT into restriction (LICENCE_NO,R_ID)"
    +"values (:LICENCE_NO,:R_ID)",{'LICENCE_NO':licence,'R_ID':c_id})
    
    print("Licence is successfully registered!")
    tmp = input("Press any key to continue...")    
    
    main.con.commit()    
    
    f_image.close()
    

                    