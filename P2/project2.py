import os
import sys
import time
import bsddb3 as bsddb
import random
# Make sure you run "mkdir /tmp/my_db" first!
DB_FILE_btree = "/tmp/chuan1_db/btreedb.db"
DB_FILE_hash = "/tmp/chuan1_db/hashdb.db"
DB_FILE_index1 = "/tmp/chuan1_db/index1db.db"
DB_FILE_index2 = "/tmp/chuan1_db/index2db.db"
answerfile = ""

DB_SIZE = 100000
SEED = 10000000

db = ""
db2 = ""


def get_random():
    return random.randint(0, 63)
def get_random_char():
    return chr(97 + random.randint(0, 25))


def populate(type_option,created):    
    if created:
        print("Database has already been created!!!")
        input("Press Enter to return Main Menu...")
        return created
    
    creating = False          # use to record whether the database has created or not
    
    if created == True:
        print("Database has already been created! ")
        tmp = input("Press Enter to Return Main Menu...")
        return
    # Btree
    if type_option == "btree" :
        print("Database does not exist! And we will create one for you! ")
        db = bsddb.db.DB()
        db.open(DB_FILE_btree, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE)
            
    # Hash Table
    if type_option == "hash":
        print("Database does not exist! And we will create one for you! ")
        db = bsddb.db.DB()
        db.open(DB_FILE_hash, bsddb.db.DB_HASH, bsddb.db.DB_CREATE)
            
    # IndexFile
    if type_option == "indexfile" :
        print("Database does not exist! And we will create one for you! ")
        db = bsddb.db.DB()
        db.open(DB_FILE_index1, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE)        
        db2 = bsddb.db.DB()
        db2.open(DB_FILE_index2, None, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE)
            
    
    # Begin to create the data
    print ("Creating the Database, please wait...." )
    random.seed(SEED)    
    
    for index in range(DB_SIZE):
        krng = 64 + get_random()
        key = ""
        for i in range(krng):
            key += str(get_random_char())
        vrng = 64 + get_random()
        value = ""
        for i in range(vrng):
            value += str(get_random_char())
        #print (key)
        #print (value)
        #print ("")
        key = key.encode(encoding='UTF-8')
        value = value.encode(encoding='UTF-8')
        db.put(key, value)
        
        if type_option == "indexfile":
            db2.put(value, key)
        
    # cur = db.cursor()
    # iter = cur.first()
    # print the database
    # while iter:
    # print(iter[0].decode("utf-8"))
    # print(iter[1].decode("utf-8"))
      #  iter = cur.next()
    # print("------------------------")

    creating = True       # record that we have created the database  
    print ("Creating Database Done!")
    input("Press Enter to Continue...")
    
    return creating

#-------------------------------------------------------------------------------
def key_search(type_option, created):     
    global answerfile
    if not created:
        print("Please Create the Database first!!")
        input("Press Enter to Continue....")
        return    
    #Search with given key  
    if type_option == "btree" :
        db = bsddb.btopen(DB_FILE_btree, "r")
    elif type_option == 'hash' :
        db = bsddb.hashopen(DB_FILE_hash, "r")
    else:
        db = bsddb.btopen(DB_FILE_index1, "r")

    key = input("Please input the key that you want to search: ")
    key = key.encode(encoding='UTF-8')
    answer = 0
    
    start = time.time()
    if db.has_key(key):
        answer = 1
        answerfile.write("Key: "+str(key.decode(encoding='UTF-8'))+"\n")
        answerfile.write("Data: "+str(db.get(key).decode(encoding='UTF-8'))+"\n")
        answerfile.write("\n")      
        answerfile.flush()
        
    end = time.time()
    duration = (end - start) * 1000000

    print ("Time Used :",duration, "microseconds")
    print ("Total number of the searched key is :",answer)
    input ("Press Enter to Continue...")    
            
    db.close()         
    return 

#-------------------------------------------------------------------------------
def data_search(type_option,created):          # Retrieve records with a given data
    if not created:
        print("Please Create the Database first!!")
        input("Press Enter to Continue....")
        return
    
    global answerfile
    
    if type_option == "btree" :
        db = bsddb.btopen(DB_FILE_btree, "r")
    elif type_option == 'hash' :
        db = bsddb.hashopen(DB_FILE_hash, "r")
    else:
        db = bsddb.btopen(DB_FILE_index1, "r")
        db2 = bsddb.btopen(DB_FILE_index2, "r")
    
    answer = []             # use to save the keys
    
    data = input("Please input the data that you want to search: ")
    data = data.encode(encoding='UTF-8')
    
    if (type_option != "indexfile"):
        start = time.time()
        for (key, value) in db.iteritems():
            if value == data:
                answer.append(key)
                
        end = time.time()
        duration = (end - start) * 1000000
                
        print ("Time Used :",duration, "microseconds")
        print ("Total number of the searched data is :",len(answer))
        input ("Press Enter to Continue...")
        
        answerfile.write("The keys for data ("+str(data.decode(encoding='UTF-8'))+"): \n\n")
        num = 1
        for i in answer:
            answerfile.write("Key"+str(num)+": "+str(i.decode(encoding='UTF-8'))+"\n")
            answerfile.write("Data: "+str(data.decode(encoding='UTF-8'))+"\n")
            answerfile.write("\n")
            answerfile.flush()
            
        answerfile.write("\n\n")
            
    else:       # indexfile
        start = time.time()
        
        if db2.has_key(data):
            answer.append(db2.get(data).decode(encoding='UTF-8'))
        
        end = time.time()
        duration = (end - start) * 1000000
        
        print ("Time Used :",duration, "microseconds")
        print ("Total number of the searched data is :",len(answer))
        input ("Press Enter to Continue...")
        
        answerfile.write("The keys for data "+str(data.decode(encoding='UTF-8'))+" : \n")
        num = 1
        for i in answer:
            answerfile.write("Key"+str(num)+": "+str(i)+"\n")
            answerfile.write("Data: "+str(data.decode(encoding='UTF-8'))+"\n")
            answerfile.write("\n")  
            answerfile.flush()
        answerfile.write("\n\n")
        db2.close() 
        
    db.close() 
    return

#-------------------------------------------------------------------------------
def range_search(type_option, created):
    if not created:
        print('Please Create the database first!')
        drop = input('Press Enter to continue...')
    else:
        if type_option == "btree" :
            db = bsddb.btopen(DB_FILE_btree, "r")
        elif type_option == 'hash' :
            db = bsddb.hashopen(DB_FILE_hash, "r")
        else:
            db = bsddb.btopen(DB_FILE_index1, "r")
        result = []
        global answerfile
        lower = input('Please enter a lower bound for key search: ')
        upper = input('Please enter a upper bound for key search: ')
        if upper > lower:
            lower = lower.encode(encoding = 'UTF-8')
            upper = upper.encode(encoding = 'UTF-8')
            if type_option == 'hash':
                #Search when db1 is HASH
                start = time.time()
                for key in db.keys():
                    if key <= upper and key >= lower:
                        result.append(key)
                        #Using append to reduce Python operation cost
                end = time.time()
                time_used = (end - start) * 1000000     #Convert time to microsec
                print("Found " + str(len(result)) + " results")
                print("Search finished in " + str(time_used) + " microseconds")
            else:           #Search when db1 is BTREE or INDEXFILE
                start = time.time()
                try:
                    start_point = db.set_location(lower)[0]
                    # print(start_point)
                    result.append(start_point)
                    key = db.next()[0]
                    while key <= upper:
                        result.append(key)
                        key = db.next()[0]
                    end = time.time()
                    time_used = (end - start) * 1000000
                    print("Found " + str(len(result)) + " results")
                    print("Search finished in " + str(time_used) + " microseconds")
                except:
                    end = time.time()
                    time_used = (end - start) * 1000000
                    print("Found 0 results")
                    print("Search finished in " + str(time_used) + "microseconds")
                
            for key in result:
                answerfile.write(key.decode()+'\n')
                answerfile.write(db[key].decode()+'\n')
                answerfile.write('\n')
                answerfile.flush()
            drop = input('Press Enter to continue...')
        else:
            print('Your input is invalid')
            drop = input('Press Enter to continue...')
            
        db.close()
        return

def destroy(type_option, created):          # destroy the existing database
    if created:
        if type_option == 'btree':
            os.remove(DB_FILE_btree)
        if type_option == 'hash':
            os.remove(DB_FILE_hash)
        if type_option == 'indexfile':
            os.remove(DB_FILE_index1)
            os.remove(DB_FILE_index2)
        print("Database Destroyed")
    else:
        print("You don't have existing database")
        
    input ("Press Enter to Continue...")   
    created = False
    return created
    
    
def main(argv):
    # Take the Type Option   
    created = False
    type_option = ""        # use to get the type option
    while True:
        try:
            option = argv[1]
        except:
            print("Invalid input! Please try again")
            return
        else:
            if option != "btree" and option != "hash" and option != "indexfile":
                print("Invalid Database! Please try again!")
                return             
            else:
                type_option = option      
                break
            
    
    # Open or Create the Answer File
    try:
        os.chdir("/tmp/chuan1_db")
    except:
        os.mkdir("/tmp/chuan1_db")
                
    global answerfile            
    answerfile = open("answers", "w")
    
    
    # Begin 
    while True:
        # Show the MainMenu
        os.system("clear")
        print ("The database type option :",option) 
        print("1. Create and populate a database")
        print("2. Retrieve records with a given key")
        print("3. Retrieve records with a given data")
        print("4. Retrieve records with a given range of key values")
        print("5. Destroy the database")
        print("0. Quit")
        
        while True:
            try:
                choice = int(input("Please Enter Your Choice >>> "))
            except:
                print("Invalid Input! Please try again!")
                continue
            else:
                if choice >= 0 and choice <= 5:
                    break
                else:
                    print("Invalid Input! Please try again!")  
                    continue
        
        # Cases 
        if choice == 1:     # Create and populate a database
            created = populate(type_option,created)
            continue
        
        if choice == 2:     # Retrieve records with a given key
            key_search(type_option,created)
            continue
        
        if choice == 3:     # Retrieve records with a given data
            data_search(type_option,created)
            continue        


        if choice == 4:     # Retrieve records with a given range of key values
            range_search(type_option,created)
            continue        
        
        if choice == 5:     # Destroy the database
            created = destroy(type_option,created)
            continue   
        
        if choice == 0:     # Quit
            if created:
                created = destroy(type_option,created)           
            break        

    print ("Thanks for using!")
    tmp = input("Press Enter to End...")



if __name__ == "__main__":
    main(sys.argv[0:])