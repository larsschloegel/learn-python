from sys import argv
# read the WYSS section for how to run this
# => python filename first 2nd 3rd
# script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


math_operator = argv[1]

print("Dies ist ein Kalkulator kann zwei Zahlen addieren bzw. subtrahieren.")
operator_one = int(input("Bitte geben sie Operator eins ein: "))
operator_two = int(input("Bitte geben Sie Operator zwei ein: "))
if math_operator == "+":
    result = operator_one + operator_two
elif math_operator == "-":
    result = operator_one - operator_two
else:
    print(f"Unbekannter Operator: {math_operator}")
    exit(1)
print(f"{operator_one} {math_operator} {operator_two} = {result}")