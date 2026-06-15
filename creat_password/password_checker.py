import string


def check_password_strength(password: str):
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