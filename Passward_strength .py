password = input("Enter a password: ")

errors = []

if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")

if not any(ch.islower() for ch in password):
    errors.append("Use at least one lowercase letter.")

if not any(ch.isupper() for ch in password):
    errors.append("Use at least one uppercase letter.")

if not any(ch.isdigit() for ch in password):
    errors.append("Use at least one number.")

if not any(not ch.isalnum() for ch in password):
    errors.append("Use at least one special character.")

# No whitespace allowed
if any(ch.isspace() for ch in password):
    errors.append("Whitespace is not allowed.")

# No emojis allowed
for ch in password:
    if ord(ch) > 127:
        errors.append("Emojis are not allowed.")
        break

if errors:
    print("\nPassword is not valid:")
    for error in errors:
        print("-", error)
else:
    print("Strong Password")