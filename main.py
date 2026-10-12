# ==============================
# SWIMMING POOL ENTRY CHECKER
# ==============================

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

# --------- collect the three answers ---------
# YOUR CODE HERE
age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)


# --------- PART 1: age group, using if / elif / else on a NUMBER ---------
# YOUR CODE HERE
if age < 4:
    print("Toddler  : splash pool only, always with an adult")
elif age < 12:
    print("Child    : main pool with an adult")
elif age < 18:
    print("Teen     : main pool alone if you can swim")
else:
    print("Adult    : all pools open to you")


# --------- PART 2: did they actually answer yes or no? ---------
# YOUR CODE HERE

# Validate the can_swim response
if can_swim != "yes" and can_swim != "no":
    print("Input error for swimming ability.")
    swim_known = False
else:
    swim_known = True

# Validate the adult_here response
if adult_here != "yes" and adult_here != "no":
    print("Input error for adult presence.")
    adult_known = False
else:
    adult_known = True


# --------- PART 3: AND - the deep pool ---------
# YOUR CODE HERE
# Allowed only when they CAN swim AND an adult IS present.
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool access: Allowed")
else:
    print("Deep pool access: Denied")


# --------- PART 4: OR - the shallow end ---------
# YOUR CODE HERE
# Warn when they are under 12 OR they cannot swim.
if age < 12 or can_swim == "no":
    print("Warning: Extra supervision required in the shallow end!")


# --------- PART 5: NOT - the lifeguard reminder ---------
# YOUR CODE HERE
# Remind when there is no adult – but only if adult_known is True.
if adult_known and not (adult_here == "yes"):
    print("Lifeguard Reminder: No adult present on deck.")


# --------- PART 6: the final verdict ---------
# YOUR CODE HERE
# First: if either answer was not understood, refuse to decide.
if not swim_known or not adult_known:
    print("Final Verdict: Refused to decide due to an invalid input answer.")

# Then work through the real cases with elif, ending in a plain else.
elif age < 4:
    if adult_here == "yes":
        print("Final Verdict: Access granted to Splash Pool (with adult).")
    else:
        print("Final Verdict: Entry Denied (Toddlers require an adult).")

elif age < 12:
    if adult_here == "yes":
        print("Final Verdict: Access granted to Main Pool (with adult).")
    else:
        print("Final Verdict: Entry Denied (Children under 12 require an adult).")

elif age < 18:
    if can_swim == "yes":
        print("Final Verdict: Access granted to Main Pool (alone).")
    elif adult_here == "yes":
        print("Final Verdict: Access granted to Main Pool (supervised).")
    else:
        print("Final Verdict: Entry Denied (Unaccompanied teen who cannot swim).")

else:
    print("Final Verdict: Access granted to all pools!")

print()
print("Have a safe swim!")




