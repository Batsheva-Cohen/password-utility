from creat_password.password_checker import check_password_strength
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Bat71234!!", {"score": 5, "is_strong": True, "feedback": []}),
        ("?Aa123957555", {"score": 5, "is_strong": True, "feedback": []}),
        (
            "?Aa1",
            {
                "score": 4,
                "is_strong": False,
                "feedback": ["Password is too short (minimum 8 characters)."],
            },
        ),
    ],
)
def test_password_length_validation(test_input, expected):
    result = check_password_strength(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Bat71234!!", {"score": 5, "is_strong": True, "feedback": []}),
        ("?Aa12395755", {"score": 5, "is_strong": True, "feedback": []}),
        (
            "?AAAAAAA1",
            {
                "score": 4,
                "is_strong": False,
                "feedback": ["Password should include lowercase letters."],
            },
        ),
        (
            "?aaaaaaa1",
            {
                "score": 4,
                "is_strong": False,
                "feedback": ["Password should include uppercase letters."],
            },
        ),
    ],
)
def test_password_requires_mixed_case_islower_and_isuper(test_input, expected):
    result = check_password_strength(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Bat71234!!", {"score": 5, "is_strong": True, "feedback": []}),
        (
            "Aa1239555",
            {
                "score": 4,
                "is_strong": False,
                "feedback": ["Password should include special characters."],
            },
        ),
        (
            "SAAAAAaA",
            {
                "score": 3,
                "is_strong": False,
                "feedback": [
                    "Password should include numbers.",
                    "Password should include special characters.",
                ],
            },
        ),
        (
            "?aaaaaaaA",
            {
                "score": 4,
                "is_strong": False,
                "feedback": ["Password should include numbers."],
            },
        ),
    ],
)
def test_password_requires_mixed_case_number_and_special_characters(test_input, expected):
    result = check_password_strength(test_input)
    assert result == expected
