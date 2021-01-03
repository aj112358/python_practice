# Exercise 13: Making Change

cents = int(input("How many cents: "))

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
TOONIE = 200

num_toonies = cents // TOONIE
num_loonies = (cents - num_toonies*TOONIE) // LOONIE
num_quarters = (cents - num_toonies*TOONIE - num_loonies*LOONIE) // QUARTER
num_dimes = (cents - num_toonies*TOONIE - num_loonies*LOONIE - num_quarters*QUARTER) // DIME
num_nickels = (cents - num_toonies*TOONIE - num_loonies*LOONIE - num_quarters*QUARTER - num_dimes*DIME) // NICKEL
num_pennies = (cents - num_toonies*TOONIE - num_loonies*LOONIE - num_quarters*QUARTER - num_dimes*DIME - num_nickels*NICKEL) // PENNY

print(f"Use {num_toonies} toonies")
print(f"Use {num_loonies} loonies")
print(f"Use {num_quarters} quarters")
print(f"Use {num_dimes} dimes")
print(f"Use {num_nickels} nickels")
print(f"Use {num_pennies} pennies")

#num_toonies = cents // TOONIE
#num_loonies = (cents - cents % TOONIE) // LOONIE
#num_quarters = (cents - cents % TOONIE - cents % LOONIE) // QUARTER
#num_dimes = (cents - cents % TOONIE - cents % LOONIE - cents % QUARTER) // DIME
#num_nickels = (cents - cents % TOONIE - cents % LOONIE - cents % QUARTER - cents % DIME) // NICKEL
#num_pennies = (cents - cents % TOONIE - cents % LOONIE - cents % QUARTER - cents % DIME - cents % NICKEL) // PENNY