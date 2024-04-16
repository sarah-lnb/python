
print("Welcome to the tip calcultor.")

total_amount = float(input("What was the total bill? $"))
#print(type(total_amount))

tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
#print(type(percent_choice))

number_ppl = int(input("How many people to split the bill? "))
#print(type(number_ppl))

amount_per_person = (total_amount / number_ppl) * (1 + (tip_percent / 100))

exact_amount_per_person = round(amount_per_person, 2)

print(f"Each person should pay: ${exact_amount_per_person}")



# each_person = total_amount/number_ppl
# amount_with_tip = each_person * (1 + (tip_percent/100))
# final_amount = round(amount_with_tip, 2)
# print(final_amount)