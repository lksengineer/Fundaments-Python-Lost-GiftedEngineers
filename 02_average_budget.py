# Global values
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
budgets = []
average = 0

# start
print("*****Software Budget Average*****")
for month in months:
    print("\b")
    budget = float(input(f"{month} budget: "))
    budgets.append(budget)
    while month != "April":
        answer = input(f"{months[len(budgets)]} budget? Y / N ? ").upper()
        if answer.isalpha():
          break
    if answer == 'N':
      break

for budget in budgets:
  average += budget

print("\b")
print(f"The average is {(average / len(budgets)):.2f}")
