from creat_password.password_checker import check_password_strength


def main() -> None:
    password = input("Enter password: ")
    result = check_password_strength(password)
    print(result)


if __name__ == "__main__":
    main()
