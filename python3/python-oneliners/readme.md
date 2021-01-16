# Python Oneliners

- [Python Oneliners](#python-oneliners)
  - [Python One-Liners - Trick 1 List Comprehension](#python-one-liners---trick-1-list-comprehension)
  - [Python One-Liners - Trick 2 Read File and Strip() Lines](#python-one-liners---trick-2-read-file-and-strip-lines)
  - [Python One-Liners - Trick 3 Lambda, Map, and Ternary Operator](#python-one-liners---trick-3-lambda-map-and-ternary-operator)

## Python One-Liners - Trick 1 List Comprehension

Suppose we have a employees dictionary. Now we need calculate the top earners.

```py
employees = {
    'Alice': 23,
    'Bob': 56,
    'Carol': 10,
    'Frank': 343,
    'Eve': 322
}
```

**General Code**:

```py
top_earners = []
for key, value in employees.items():
    if value >= 100:
        top_earners.append((key, value))

print(top_earners)
# [('Frank', 343), ('Eve', 322)]
```

**Python Oneliners Code**:

```py
"""
lst = [expression context]

Here is just two parts,
    1. expression
    2. context

1. Expression: (k, v) # or something like (x - 10), (a ** 2 + 2 * a * b + b ** 2)
2. context: for k, v in employees.items()
3. more_restrict_part: if v >= 100
"""

top_earners = [(k, v) for k, v in employees.items() if v >= 100]
print(top_earners)
# [('Frank', 343), ('Eve', 322)]
```

## Python One-Liners - Trick 2 Read File and Strip() Lines

```py
# General Code
filename = "./trick-2-read-files-and-strip-lines.py"

f = open(filename)  # open file
lines = []

for line in f:
    # strip() remove all leading and trailing spaces
    lines.append(line.strip())

print(lines)


# Oneliners Code
print([line.strip() for line in open('./trick-2-read-files-and-strip-lines.py')])
```

## Python One-Liners - Trick 3 Lambda, Map, and Ternary Operator

- **Lambda**: `lambda variable: context_part`
- **Map()**: `map(function, iterable) : return iterable`
- **Ternary Operator**: `True if condition else False`

```py
print(2 + 2 if 2 < 0 else 4 + 4)
# 8
```

Full Example:

```py
# variable = map(function, iterable)
# variable = map(function-> lambda variable: ternary operator, iterable -> txt)
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
print(list(mark))
```
