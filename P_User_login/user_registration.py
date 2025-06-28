def validate_name(name):
    if not isinstance(name, str) or len(name.strip()) < 2:
        raise ValueError("Name Must be atleast 2 Charactor")
    return True

def validate_email(email):
    if not isinstance(email, str) or '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("Enter Valid email")
    return True

def validate_password(password):
    if (
        not isinstance(password, str) or 
        len(password) < 8 or 
        not any(c.isupper() for c in password) or
        not any(c.isdigit() for c in password)
    ):
        raise ValueError("Password must be at least 8 characters long, include a number and a capital letter.")
    return True

def validate_user(name, email, password):
    validate_name(name)
    validate_email(email)
    validate_password(password)
    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except ValueError as e:
        print(f"❌ Registration failed: {e}")
        return False  # 👈 returns False on failure

    # ✅ Only runs if validation succeeded
    user = {
        "name": name,
        "email": email,
        "password": "#" * len(password)  # masked here directly
    }

    return user
