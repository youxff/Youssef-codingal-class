# STUDY NOTES ORGANIZER
# Topics: with open() | split() | os.path.exists() | os.remove() | File Handling

import os

# PART 1 -- Read Notes
print("=== Study Notes ===")
with open("L51/study-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

# PART 2 -- Count Keywords
print("=== Keyword Count ===")
with open("L51/study-notes.txt", "r") as f:
    total_words = 0

    for line in f:
        words = line.split()
        total_words += len(words)
        print(len(words), "words ->", line.strip())

print("Total Words:", total_words)
print()

# PART 3 -- Create Revision Summary
print("=== Creating Revision Summary ===")

if os.path.exists("L51/revision-summary.txt"):
    print("revision-summary.txt already exists - overwriting")
else:
    print("Creating revision-summary.txt")

summary = ""

with open("L51/study-notes.txt", "r") as f:
    summary += "=== Revision Notes ===\n\n"

    for line in f:
        words = line.split()

        if len(words) > 0:
            summary += "- " + words[0] + "\n"

with open("L51/revision-summary.txt", "w") as out:
    out.write(summary)

print("Summary saved!")
print()

# PART 4 -- View Summary
print("=== Revision Summary ===")
with open("L51/revision-summary.txt", "r") as f:
    print(f.read())

# PART 5 -- Delete Summary
choice = input("\nDelete summary file? (yes/no): ")

if choice.lower() == "yes":
    if os.path.exists("L51/revision-summary.txt"):
        os.remove("L51/revision-summary.txt")
        print("revision-summary.txt deleted.")
else:
    print("File kept.")