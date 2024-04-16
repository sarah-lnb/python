# print(3*3+3/3-3)
# print(3*(3+3)/3-3)

# 1st input: enter height in meters e.g: 1.65
height = (input("Enter height in meters: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = (input("Enter weight in kilograms: "))

# Convert str data for calculation:
height2 = float(height)
weight2 = int(weight)

# Check data types:
print(type(height2))
print(type(weight2))

# BMI calculation
BMI = weight2 / height2 ** 2
print(int(BMI))

