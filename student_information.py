#Starting with main function for orogram flow
def main():

#Creating dictionary of student info
#Each data will be a nested dictionary
    Student_information = {
        "Jim": {
            "ID": 1,
            "GPA": 3.1,
            "CREDITS-COMPLETED": 97.0,
            "GRADES": [80, 50, 100, 98]
        },
       #----------------------------------------
        "Sarah": {
            "ID": 2,
            "GPA": 3.6,
            "CREDITS-COMPLETED": 40.0,
            "GRADES": [80, 98]
            }       
    }
    #Print full dictionary
    print(Student_information)

    #List of students
    print("\nList of Students")
    for name in Student_information.keys():
        print(name)

    #Tabulated Student information
    print("\nStudent Information")
    print("Student\tID\tGPA\tCredits Completed\tGrades")

    #Using items() to access key/value pairs
    for name, info in Student_information.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['CREDITS-COMPLETED']}\t{info['GRADES']}")

    ##Accessing Student Information Using the Key in a Loop
    print("\nAccessing Student Information Using the Key in a Loop")
    for name in Student_information:
        print(f"{name}: {Student_information.get(name)}")

    #Remove student
    print("\nSarah has dropped out, removing from student info registry")
    removed = Student_information.pop("Sarah")
    print(Student_information)

    #Access GPA using get()
    print("\nGetting Jim's GPA")
    GPA = Student_information.get("Jim").get("GPA")
    print(GPA)

    #Clear Dictionary 
    print("\nStudents have graduated, clearing the student registry")
    Student_information.clear()
    print(Student_information)

    print("\nCompleted by, Keith Gama")
    
if __name__ == "__main__":
    main()    
        
