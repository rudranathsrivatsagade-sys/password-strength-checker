password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_+=<>?/"

# Length check
if len(password) < 8:
    print("Weak password: Must be at least 8 characters")
else:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Strong password 💪")
    else:
        print("Weak password ❌")
        if not has_upper:
            print("- Missing uppercase letter")
        if not has_lower:
            print("- Missing lowercase letter")
        if not has_digit:
            print("- Missing digit")
        if not has_special:
            print("- Missing special character")
