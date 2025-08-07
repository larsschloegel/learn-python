from sys import argv

# first command line argument save in script and second in filename
script, filename = argv

# open text file and return a stream (vergleichbar mit einem DVD-Player)
txt = open(filename)

# display a txt file name
print(f"Here's your file {filename}:")
# display the content of the test file (ex15_sample.txt)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())