#call/import random module from library to be used for removing
#grade choice, when a random grade is selected
import random

#Function 1 - Collect grates
#but returns a value, which will be the list
#No papameters used because data comes from input, not arguments
def Collect_grade():
    grades = [] # create empty list
    while True:
        grade = int(input("Please enter the grade or -1 to stop: "))
        if grade == -1:
            break
        else:
            grades.append(grade)
    return grades
#--------------------------------------------------------------------
#Function 2 - Remove lowest grade
#function will have parameter, and modify list
#List is passed as parameter, to work with existing data
def Delete_lowest(grades):
     print("\nRemoving lowest grade")
     lowest = min(grades)
     index=grades.index(lowest) #get position of lowwest grade
     grades.pop(index)          #remove item with pop()
     print(grades)
#-------------------------------------------------------------------
#Function 3 - Remove random choice
#function will have parameter and use random.choice()
#Used a parameter here because the function
#depends on the list created in main()
def Delete_random(grades):
    print("\nRemoving random grade")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print(grades)
#--------------------------------------------------------------------
#function 4 - Edit grade
#function will have parameter, but no return
#loop will be used to validate
def Edit_grade(grades):
    print("\nEdit a grade")
    #give index and value
    for i, grade in enumerate(grades, start=1):
       print(f"{i}.{grade}")
    #Ask which grade to edit
    choice = int(input("Which grade do you want to edit: "))
    #loop for validation
    while choice < 1 or choice > len(grades):
        print("Please enter a valid grade!")
        #redisplay
        for i, grade in enumerate(grades, start=1):
            print(f"{i}. {grade}")

        choice = int(input(f"Which grade do you want to edit (enter a number between 1 and 7): "))
    new_grade = int(input("Enter the new grade: "))
    #Update list
    grades[choice - 1] = new_grade
    print(grades)
#-------------------------------------------------------------------
#function 5 - Sort and reverse
#function will have parameters and will use list methods
def Sort_and_reverse(grades):
    print("\nSorting and Reversing List")
    #arrange list with sort()
    grades.sort()
    #flip order with reverse
    grades.reverse()
    print(grades)
#---------------------------------------------------------------------
#function 6 - Calculate Total and average
#function will have paprameter, and display the total and average value
def Total_and_Average(grades):
    print("\nGetting Grades Total and Average")
    total = sum(grades)
    average = total / len(grades)
    print("Total:", total)
    print("Average:", average)
#---------------------------------------------------------------------
#Main Function
def main():
    #Call Collect_grade() and store in grades variable
    grades = Collect_grade()
    print(grades)
#list in grades is passed as argument to other functions
#value is passed not variable
#Calling other functions  
    Delete_lowest(grades)
    Delete_random(grades)
    Edit_grade(grades)
    Sort_and_reverse(grades)
    Total_and_Average(grades)
    print("\nCompleted by, Keith Gama")

#call main function
if __name__ == "__main__":
    main()
    
