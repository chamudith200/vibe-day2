def main():
    while True:
        # Ask for student's name
        name = input("Enter student name (or type 'Exit' to quit): ")
        
        # Check if the user wants to exit
        if name.strip().lower() == 'exit':
            print("Exiting program.")
            break

        # Ask for 3 subject marks
        try:
            mark1 = float(input("Enter mark for subject 1: "))
            mark2 = float(input("Enter mark for subject 2: "))
            mark3 = float(input("Enter mark for subject 3: "))

            # Calculate the average
            average = (mark1 + mark2 + mark3) / 3

            # Determine grade
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"

            # Display clean formatted output
            print("-" * 30)
            print(f"Name    : {name}")
            print(f"Average : {average:.1f}")
            print(f"Grade   : {grade}")
            print("-" * 30 + "\n")
            
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.\n")

if __name__ == "__main__":
    main()
