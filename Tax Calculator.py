# Tax Calculator

print("\nWelcome to my tax calculator program (UK) - 2025/2026! \n")
print("All you need to do is enter your annual salary, and I will tell you how much tax you'll be paying as well as your net income.")

salary = float(input("\nPlease enter your annual salary: £"))

if salary <= 12570:
    print(f"\nYou will not need to pay any tax. Therefore your net income will be £{salary:,.2f}.")
    print("\nThanks for using my Tax Calculator Program! Goodbye!\n")
    quit()

elif salary >= 12571 and salary <= 50270:
    taxable_income = salary - 12570
    calculating_salary = (taxable_income * 20) / 100
    new_salary = round(salary - calculating_salary, 2)

    print(f"\nYour total tax is £{calculating_salary:,.2f}, so your net income will be £{new_salary:,.2f}.")
    print("\nThanks for using my Tax Calculator Program! Goodbye!\n")
    quit()

elif salary >= 50271 and salary <= 125140:
    calculating_salary = (50270 - 12570) * 20 / 100 + (salary - 50270) * 40 / 100
    new_salary = round(salary - calculating_salary, 2)

    print(f"\nYour total tax is £{calculating_salary:,.2f}, so your net income will be £{new_salary:,.2f}.")
    print("\nThanks for using my Tax Calculator Program! Goodbye!\n")
    quit()

elif salary >= 125141:
    calculating_salary = (50270 - 12570) * 20 / 100 + (125140 - 50270) * 40 / 100 + (salary - 125140) * 45 / 100
    new_salary = round(salary - calculating_salary, 2)

    print(f"\nYour total tax is £{calculating_salary:,.2f}, so your net income will be £{new_salary:,.2f}.")
    print("\nThanks for using my Tax Calculator Program! Goodbye!\n")
    quit()

