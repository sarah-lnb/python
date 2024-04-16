# score = 0
# height = 1.8
# isWinning = True
# # f-String
# print(f"Your score is {score}, your height is {height} and you are winning {isWinning}")

age = (input("What is your age?: "))
#print(type(age))

weeks = 52
#print(type(weeks))

remaining_age1 = (90 - int(age)) * weeks
remaining_age2 = (90 - int(age)) * 52

#print(remaining_age)

print(f"You have {remaining_age1} weeks left.")
print(f"You have {remaining_age2} weeks left.")