x = input("Enter the password: ")

has_length = False
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*"

reasons = []

# Length check
if len(x) >= 8:
    has_length = True

# Character checks
for char in x:

    if char.isupper():
        has_upper = True

    if char.islower():
        has_lower = True

    if char.isdigit():
        has_digit = True

    if char in special_chars:
        has_special = True

# Add reasons AFTER checking everything

if not has_length:
    reasons.append("Minimum length should be 8")

if not has_upper:
    reasons.append("At least one uppercase character required")

if not has_lower:
    reasons.append("At least one lowercase character required")

if not has_digit:
    reasons.append("At least one digit required")

if not has_special:
    reasons.append("At least one special character required")

# Final output

if has_length and has_upper and has_lower and has_digit and has_special:
    print("It is a strong password")

else:
    print("It is a weak password because:")

    for reason in reasons:
        print("-", reason)