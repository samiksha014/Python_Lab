#correct code

from datetime import datetime

# Create grids
def create_grid(rows, columns):
    grid = []
    for row in range(rows):
        grid.append([""] * columns)
    return grid

# Display grid
def display_grid(grid):
    for r in grid:
        print(" ".join(str(x).rjust(2) if x else "  " for x in r))

# Month logic to get exact number of days and month name
def month_logic(month, year):
    month_dict = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    days = 0
    month_name = ""
    if month in month_dict:
        month_name = month_dict[month]

        # Defining the number of days each month carries
        if month == 2:
            days = 28
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29
        elif month in {4, 6, 9, 11}:
            days = 30
        else:
            days = 31
    return days, month_name

# Function to get the first day of the month
def first_day_of_month(year, month):
    # Using datetime to find the weekday of the first day
    first_day = datetime(year, month, 1)
    return first_day.weekday()  # Monday is 0, Sunday is 6

# Create a calendar format for a single month
def calendar_month_format(year, month):
    no_of_days, month_name = month_logic(month, year)
    start_day = first_day_of_month(year, month)

    calendar = create_grid(6, 7)  # Max 6 rows and 7 columns (weeks and days)

    # Fill the grid with days of the month
    day = 1
    for week in range(6):
        for weekday in range(7):
            # Skip the initial empty days
            if week == 0 and weekday < start_day:
                continue
            if day > no_of_days:
                break
            calendar[week][weekday] = day
            day += 1

    # Convert grid to a formatted string
    output = f"{month_name} {year}\nMo Tu We Th Fr Sa Su\n"
    for r in calendar:
        output += " ".join(str(x).rjust(2) if x else "  " for x in r) + "\n"
    return output.strip()

# Display the full year in grid format
def display_year_calendar(year, rows, cols):
    total_months = 12
    grid = create_grid(rows, cols)
    month = 1

    # Fill the grid with calendar month formats
    for r in range(rows):
        for c in range(cols):
            if month <= total_months:
                grid[r][c] = calendar_month_format(year, month)
                month += 1

    # Display all months in the grid
    for r in grid:
        row_lines = [m.splitlines() for m in r if m]
        max_lines = max(len(rl) for rl in row_lines)
        for i in range(max_lines):
            print("   ".join(rl[i] if i < len(rl) else " " * 20 for rl in row_lines))
        print("\n")

# Determine the day of the week for a specific date
def get_day_of_date(year, month, day):
    try:
        specific_date = datetime(year, month, day)
        return specific_date.strftime("%A")
    except ValueError:
        return "Invalid date!"

# Main program
def main():
    year = int(input("Enter the year: "))
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    print("\nYear Calendar:\n")
    display_year_calendar(year, rows, cols)
    
    print("\nEnter a specific date to find the day:")
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day: "))
    day_of_week = get_day_of_date(year, month, day)
    print(f"The day on {day}/{month}/{year} is {day_of_week}.")

# Run the program
main()   




    


    
    
        



