# -----------------------------------------
# 1. for loop - Iterating over a list
# -----------------------------------------
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# -----------------------------------------
# 2. for loop with range()
# -----------------------------------------
for i in range(5):  # 0 to 4
    print("Number:", i)

# Start, Stop, Step
for i in range(1, 10, 2):  # Odd numbers from 1 to 9
    print(i)

# -----------------------------------------
# 3. while loop - Repeats while condition is True
# -----------------------------------------
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Don't forget to update the condition

# -----------------------------------------
# 4. break statement - Exit the loop early
# -----------------------------------------
for i in range(10):
    if i == 5:
        break  # Stops when i is 5
    print("Break example:", i)

# -----------------------------------------
# 5. continue statement - Skip to next iteration
# -----------------------------------------
for i in range(5):
    if i == 2:
        continue  # Skips printing 2
    print("Continue example:", i)

# -----------------------------------------
# 6. else with loops
# -----------------------------------------
for i in range(3):
    print("Looping:", i)
else:
    print("Finished for loop!")  # Executes when loop completes normally

# while loop with else
x = 0
while x < 3:
    print("While loop:", x)
    x += 1
else:
    print("While loop ended.")

# -----------------------------------------
# Summary:
# - Use `for` when looping over items
# - Use `while` when repeating until a condition is false
# - Use `break` to exit early, `continue` to skip current iteration
# - Optional `else` runs after normal loop completion
# -----------------------------------------
