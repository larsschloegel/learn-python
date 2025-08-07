# commands for files

'''
close - close the file (like save in editor)
read - read the contents of the file
readline - read just on line of a text file
truncate - empties the file (Datei leeren)
write('stuff') - Write "stuff" to the file
seek(0) - Move the read/write location to the beginning of the file

'''

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-c (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

content = f"{line1}\n{line2}\n{line3}\n"
target.write(content)
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

