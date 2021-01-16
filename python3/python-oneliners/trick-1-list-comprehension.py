employees = {
    'Alice': 23,
    'Bob': 56,
    'Carol': 10,
    'Frank': 343,
    'Eve': 322
}

# --------------------- General Answer -------------------------
top_earners = []
for key, value in employees.items():
    if value >= 100:
        top_earners.append((key, value))

print(top_earners)

# ---------------- Oneliners Answer ----------------------------
# First understand basic list comprehension
"""
lst = [expression context]
"""
# expression part : x
# context part    : for x in range(10)
# lst = [x for x in range(10)]
# print(lst)

# get square value
# lst = [x ** 2 for x in range(10)]
# print(lst)

# Now solve the above problem
# expression part : (k, v)
# context part : for k, v in employees.items() 
# after context more restrict part: if v >= 100
top_earners = [(k, v) for k, v in employees.items() if v >= 100]
print(top_earners)