# General Code

filename = "./trick-2-read-files-and-strip-lines.py"

f = open(filename)  # open file
lines = []

for line in f:
    # strip() remove all leading and trailing spaces
    lines.append(line.strip())

print(lines)

# Oneliners Code
"""
list_comprehension has two parts expression and context part
1) Expression: line
2) 
"""
print([line.strip() for line in open('./trick-2-read-files-and-strip-lines.py')])