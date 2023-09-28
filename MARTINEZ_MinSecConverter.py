# prompts the user to enter
secs = eval(input("Enter an integer in seconds: "))

# formulas
m = secs / 60
s = secs % 60

# display
print()
print("\t--", secs, "seconds is equal to", int(m), "minutes and", s, "seconds --")
