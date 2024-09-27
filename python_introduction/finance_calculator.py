monthlyIncome = int(input("Enter your monthly income: "))
totalExpenses = int(input("Enter your total monthly expenses: "))
interest = float(0.05)
monthlySavings =  monthlyIncome - totalExpenses
print("Your monthly savings are " + str(monthlySavings) + "$")
ProjectedSavings = (monthlySavings*12) + (monthlySavings * 12 * interest)
print("Projected savings after one year, with interest, is: " + str(ProjectedSavings) + "$")