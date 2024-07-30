def main():
  income = 60000  # Example user-defined income
  brackets = getBrackets(income)
  taxOwed = 0

  for i in range(len(brackets)):
      if i == 0:
          taxOwed += brackets[i][0] * brackets[i][1]
      elif i < len(brackets) - 1:
          taxOwed += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1]
      else:
          taxOwed += (income - brackets[i-1][0]) * brackets[i][1]

  print("Tax Owed: $" + str(taxOwed))

def getBrackets(income):
  taxBrackets = [(11000, 0.12), (44000, 0.22), (74000, 0.24), (116000, 0.32)]
  brackets = []

  for i in range(len(taxBrackets)):
      if income > taxBrackets[i][0]:
          brackets.append(taxBrackets[i])
      else:
          break
  return brackets

if __name__ == "__main__":
  main()