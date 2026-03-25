try:
    #Birth year as input from the user
    birth_year = int(input("Enter your birth year: "))

    # Current year 
    current_year = 2026

    # Checking for valid birth year
    if birth_year > current_year or birth_year <= 0:
        print("Please enter a valid birth year.")
    else:
        # Calculating age
        age_years = current_year - birth_year
        age_months = age_years * 12
        age_days = age_years * 365
        age_hours = age_days * 24
        age_minutes = age_hours * 60
        years_to_100 = 100 - age_years

        # Displaying results
        print("\nYour Age Details:")
        print("Age in years:", age_years)
        print("Age in months:", age_months)
        print("Age in days:", age_days)
        print("Age in hours:", age_hours)
        print("Age in minutes:", age_minutes)

        if years_to_100 > 0:
            print("Years left to reach 100:", years_to_100)
        else:
            print("You are already 100 years or older.")

except ValueError:
    print("Invalid input! Please enter a numeric year.")