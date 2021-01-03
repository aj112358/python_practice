# Exercise 57: Cell Phone Bill

BASE_CHARGE = 15.00
BASE_MINS = 50
BASE_TEXT = 50
EXTRA_MINS = 0.25
EXTRA_TEXT = 0.15
FEE_911 = 0.44
TAX_RATE = 0.05

num_mins = int(input("How many minutes? "))
num_texts = int(input("How many texts? "))

mins_charge = 0
text_charge = 0

print("Base charge:   %6.2f" % BASE_CHARGE)
if num_mins > BASE_MINS:
    mins_charge = (num_mins-BASE_MINS)*EXTRA_MINS
    print("Extra minutes: %6.2f" % (mins_charge))
if num_texts > BASE_TEXT:
    text_charge = (num_texts-BASE_TEXT)*EXTRA_TEXT
    print("Extra texts:   %6.2f" % (text_charge))
print("911 fee:       %6.2f" % FEE_911)
total_gross = BASE_CHARGE+text_charge+mins_charge+FEE_911
print("Tax:           %6.2f" % (total_gross*TAX_RATE))
print("Total:         %6.2f" % (total_gross*(1+TAX_RATE)))

