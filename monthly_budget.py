def main():
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter total monthly budget: "))
        total_expenses = 0

        print("\nEnter your expenses one by one. Type 'done' to finish.")
        
        while True:
            entry = input("Enter expense amount: ").strip().lower()
            
            if entry == 'done':
                break
            
            try:
                expense = float(entry)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")

        # Calculate remaining balance
        balance = total_budget - total_expenses

        # Display results
        print("\n" + "-" * 30)
        print(f"Total Budget      : {total_budget:.2f} LKR")
        print(f"Total Expenses    : {total_expenses:.2f} LKR")
        print(f"Remaining Balance : {balance:.2f} LKR")
        print("-" * 30)

        # Warning Message
        if balance < 500:
            print("Warning: Low Funds")
        
        print()

    except ValueError:
        print("Invalid input. Please restart and enter a valid budget amount.")

if __name__ == "__main__":
    main()
