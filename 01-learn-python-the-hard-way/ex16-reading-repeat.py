from sys import argv

script, filename = argv

txt = open(filename)

print(f"Print the file {filename}:")
print(txt.read())