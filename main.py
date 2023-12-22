import csv

# Formats the currency to the appropriate dollar format
def format_currency(amount):
    return "${:,.2f}".format(amount)

# Read the CSV file and return its contents as a list of rows
def read_csv(filename):
    with open(filename, "r") as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        return list(csv_reader)

# Calculate the 2012 Expenses
def calculate_expenses(data):
    expenses = {} # Dictionary to hold the total expenses for each department

    # Process each row in the CSV file
    for row in data:
        department = row[0]

        # Skip rows with empty department names
        if not department.strip():
            continue

        # Parse the '2012 Actual' column
        try:
            actual_2012 = float(row[3]) if row[3] else 0
        except ValueError:
            actual_2012 = 0

        # Sum the expenses for each department
        expenses[department] = expenses.get(department, 0) + actual_2012
    
    return expenses

# Function to print the expenses in the formatted manner
def print_expenses(expenses):
    # Finding the longest department name for formatting
    longest_dept_name = max(len(dept) for dept in expenses)

    print(f"{'Department':<{longest_dept_name}}    {'2012 Expenses'}")
    print('-' * (longest_dept_name + 22))

    # Print each department's expenses - sorted and formatted
    for department, total in sorted(expenses.items(), key=lambda x: x[1], reverse=True):
        print(f"{department:<{longest_dept_name}}     {format_currency(total)}")

# Main function to sum and print the department expenses
def main(filename):
    data = read_csv(filename)
    expenses = calculate_expenses(data)
    print_expenses(expenses)

# Call the function with the CSV path
main('data.csv')