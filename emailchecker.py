def email_validator(email):
    if "@" not in email:
        return False
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if len(username) == 0:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


# Main Program
email = input("Enter your email: ")

if email_validator(email):
    print("✅ Valid Email Address")
else:
    print("❌ Invalid Email Address")