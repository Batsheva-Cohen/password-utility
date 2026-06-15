import random
import string


def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Password should include lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password should include uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password should include numbers.")

    special_characters = string.punctuation
    if any(c in special_characters for c in password):
        score += 1
    else:
        feedback.append("Password should include special characters.")

    return {"score": score, "feedback": feedback, "is_strong": score == 5}


def generate_password(length: int = 12) -> str:
    if length < 4:
        raise ValueError("Length must be at least 4 to ensure variety.")

    all_lowercase = string.ascii_lowercase
    all_uppercase = string.ascii_uppercase
    all_digits = string.digits
    all_special = string.punctuation

    password_template = [
        random.choice(all_lowercase),
        random.choice(all_uppercase),
        random.choice(all_digits),
        random.choice(all_special),
    ]

    combined_chars = all_lowercase + all_uppercase + all_digits + all_special
    password_template += [
        random.choice(combined_chars) for _ in range(length - 4)
    ]
    random.shuffle(password_template)
    return "".join(password_template)

