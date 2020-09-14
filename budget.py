''' 
    Author: Xiana Carrera Alonso
    Date: 23/08/2020
    This is a program made for the 'Scientific Computing with Python' course of freeCodeCamp.
    This code corresponds to the third assigment, 'Budget App'.
    The purpose of the code is to 'create a "Category" class that can be used to create different budget categories'
    and then to create a function in order to show the percentage spent in each category passed.
    Complete instructions for this assigment can be found at
    https://repl.it/@freeCodeCamp/fcc-budget-app#README.md
'''

class Category:
    
    def __init__(self, nam):
        self.name = nam
        self.ledger = []    # The ledger will register the movements of the category
        
    def __str__(self):
        # Shows a title and the complete ledger, with descriptions and the amounts deposited/withdrawn
        res = ""
        res = res + self.name.center(30, "*") + "\n"
        
        for item in self.ledger:
            res = res + item["description"][:23].ljust(23)
            if len(str(item["amount"])) > 7 :       # Too long for a single line (more than 30 characters)
                res = res + "\n" + f"{float(str(item['amount'])):.2f}".rjust(30) + "\n"
            else:
                res = res + f"{float(str(item['amount']).rjust(8)):.2f}".rjust(7) + "\n"
        
        res = res + "Total: " + str(self.get_balance())
        return res 
    
    def deposit(self, am, desc = ""):
        self.ledger.append({"amount" : am, "description" : desc})
        
    def get_balance(self):
        tot = 0
        for i in range(len(self.ledger)):
            tot += self.ledger[i]["amount"]
        return tot
    
    def check_funds(self, comp):
        if self.get_balance() >= comp:
            return True     # There are enough funds
        else :
            return False
        
    def withdraw(self, am, desc = ""):
        check = self.check_funds(am)
        if check:
            self.deposit(-am, desc)     
            # am is positive, so its negative counterpart is 'deposited'
        return check
    
    def transfer(self, am, destiny):
        check = self.check_funds(am)
        if check:
            self.withdraw(am, "Transfer to " + destiny.name)
            destiny.deposit(am, "Transfer from " + self.name)
        return check


def create_spend_chart(cat_list):
    # Creates a bar chart showing the percentages of each category on the list regarding the total spent
    
    rep = len(cat_list)
    
    percentages = []
    withdrawn = []
    total = 0
        
    for i in range(rep):
        withdrawn.append(0)    
        for oper in cat_list[i].ledger:
            if oper["amount"] < 0:
                withdrawn[i] -= oper["amount"]  # oper["amount"] is a negative number
        total += withdrawn[i]
    
    lines = []
    largest = 0
    for i in range(rep):
        # Percentages are rounded down to the nearest 10
        percentages.append((int(100 * withdrawn[i] / total) // 10) * 10)

        # Formatting
        lines.append([])
        for j in range(10 - percentages[i] // 10):
            lines[i].append("   ")
        for j in range(percentages[i] // 10 + 1):   # 1 extra because of the 11 marks (see lines 99 and 100 of the code)
            lines[i].append(" o ")
        lines[i].append("---")
        for character in str(cat_list[i].name): 
            lines[i].append(" " + character + " ")      # The names must be displayed vertically. Characters are stored one by one
            if len(str(cat_list[i].name)) > largest :
                largest = len(str(cat_list[i].name))
        
    chart = "Percentage spent by category\n"

    first_line = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|",
        " 20|", " 10|", "  0|"]
    last_line = []
    
    for i in range(11):
        last_line.append(" \n")
    last_line.append("-\n")
    
    for i in range(largest - 1):
        first_line.append("    ")
        last_line.append(" \n")
    
    first_line.append("    ")
    first_line.append("    ")
    last_line.append(" ")   # The last line must not start a new line
    
    # Each line needs to be filled with blank so that they all have same length (in other case, zip() would shorten them)
    for i in range(rep):
        for j in range(largest - len(str(cat_list[i].name))):
            lines[i].append("   ")
        
    reverse = zip(first_line, *lines, last_line)    # The lines are reversed in order to print them correctly

    for items in reverse:
        for item in items:
            chart = chart + item
    
    return chart
    
        
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
