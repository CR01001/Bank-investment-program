#Programmer: Conor Rimmer ID: 10824856 Date:16/09/2020
value = 10000
'''The formula below is the formula to use to calculate
the interest earnt over 5 years the formula calculates the
percentage gained from the original value.'''
Calculation_1 = value * (1+2/100) ** 5
'''The code below prints the statement along with the
calculation made after the interest added over 5 years.
The 'round()' command rounds the float to 2 decimal places.'''
print(str("While at your Bank, you will have £")+(str(round(Calculation_1, 2)))+(" after 5 years."))

Bank_2_1 = value * (1+1/100) ** 3
Bank_2_2 = Bank_2_1 * (1+5/100) ** 2

print(str("While at Bank 2, you will have £")+(str(round(Bank_2_2, 2)))+(" after 5 years."))

Bank_3_1 = value * (1+1/100) ** 4
Bank_3_2 = Bank_3_1 * (1+10/100) ** 1
round(Bank_3_1)

print(str("While at Bank 3, you will have £")+(str(round(Bank_3_2, 2)))+(" after 5 years."))

if(Calculation_1 > Bank_2_2):
    print("Your bank is the best choice.")
elif(Bank_2_2 > Bank_3_2):
    print("Bank 2 is the best choice.")
else:
    print("Bank 3 is the best choice.")
