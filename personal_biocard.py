# Storing personal details in variables
name = "Ashley"
age = 21
course = "Generative AI"
college = "ABC"
email = "ash@stars.com"

# Printing the bio card in a box format
print("╔════════════════════════════════╗")
print("║        STUDENT BIO CARD        ║")
print("╠════════════════════════════════╣")
print(f"║ Name    : {name:<18} ║")
print(f"║ Age     : {age} years{' ' * 11}║")
print(f"║ Course  : {course:<18} ║")
print(f"║ College : {college:<18} ║")
print(f"║ Email   : {email:<18} ║")
print("╚════════════════════════════════╝")