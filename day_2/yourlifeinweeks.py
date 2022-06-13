## Your life in weeks

# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age?")
years_left = 90-int(age)
months_left = 12 * years_left
weeks_left = 52 * years_left
days_left = 365 * years_left

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')