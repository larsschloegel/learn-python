import cmath
name = 'Lars Schlögel'
age = 30
height = 185 #cm

def cm_to_inches(cm):
    return cm / 2.54

print(f"Lass uns über {name} reden.")
print(f"Ich bin {height} hoch und {age} alt.")
print(f"If I add {age} and {height} I get {age + height}.")
print(f"{height} sind {round(cm_to_inches(height), 2)} inches.")