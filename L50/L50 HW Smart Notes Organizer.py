# Smart Note Organiser

# Read the whole note
file = open("L50/notes.txt", "r")
content = file.read()
print("All Notes:")
print(content)
file.close()

# Read lines into a list
file = open("L50/notes.txt", "r")
lines = file.readlines()
file.close()

# Filter important lines
print("\nImportant Notes:")
for line in lines:
    if "IMPORTANT" in line.upper():
        print(line.strip())

# Copy odd lines to a new file
odd_file = open("odd_notes.txt", "w")

for i in range(len(lines)):
    if i % 2 == 0:      # odd line numbers (1st, 3rd, 5th...)
        odd_file.write(lines[i])

odd_file.close()

# Loop through the new file
print("\nOdd Lines:")
odd_file = open("odd_notes.txt", "r")

for line in odd_file:
    print(line.strip())

odd_file.close()

print("\nSmart Note Organiser Finished!")