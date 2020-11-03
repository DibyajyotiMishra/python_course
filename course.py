import sqlite3 as lite


# TODO: fuctionality goes here

class DatabaseManage(object):
    def __init__(self):
        global dbcon
        try:
            dbcon = lite.connect('courses.db')
            with dbcon:
                cur = dbcon.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_Private BOOLEAN NOT NULL DEFAULT 0)") 
        except Exception:
            print("Unable to create a DB!")
            
    def add_data(self,data):
        try:
            with dbcon:
                cur = dbcon.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_Private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            print("Unable to add data to the DB!")

    def get_data(self):
        try:
            with dbcon:
                cur = dbcon.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            print("Unable to get data from the DB!")

    def delete_data(self,id):
        try:
            with dbcon:
                cur = dbcon.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
                
        except Exception:
            print("Unable to delete data from the DB!")

    



# TODO: provide interface to user

def main():
    print("*"*40)
    print("\n :: Course Manager :: \n")
    print("*"*40)
    print("\n")
    
    db = DatabaseManage()
    
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    print("\n")
    
    print("\n PRESS 1. Add a Course")
    print("\n PRESS 2. Show all Courses")
    print("\n PRESS 3. Delete a Course. Pass an ID for the same.") 
    print("#"*40)
    print("\n")
    
    choice = input("\n Enter your choice: ")
    
    if choice == "1" :
        name = input("\n Enter course name")
        description = input("\n Enter course description")
        price = input("\n Enter course price")
        is_Private = input("\n Do you to keep it Private (0/1)?")
        
        if db.add_data([name, description, price, is_Private]):
            print("Course created")
        else:
            print("Something went wrong")
            
    elif choice == "2" :
        print("\n :: Course  List ::")
        
        for index, item in enumerate(db.get_data()):
            print("\n Sl no: " + str(index+1))
            print("Course ID: " + str(item[0]))
            print("Course Name: " + str(item[1]))
            print("Course Description: " + str(item[2]))
            print("Course Price: " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Private: " + private)
            print("\n")
            
    elif choice == '3':
        record_Id = input("Enter course ID :")
        if db.delete_data(record_id): 
            print("Course is deleted")
        else:
            print("Something went wrong")
            
    else:
        print(" \n Invalid Input")
        
        
        
if __name__ == '__main__':
    main()
            
