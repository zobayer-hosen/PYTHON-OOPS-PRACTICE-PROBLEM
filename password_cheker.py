import  re

# password strength check conditions:
#min 8 chars, digit,uppercase, lowercase, special char

def check_password_strength(password):

    if len(password) <8:
        return  "weak : password must be at least 8 characher long."
    if not any(char.isdigit() for char in password):
        return " weak :password must include at least one number. "

    if not any(char.isupper() for char in password):
        return  "Weak: password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return  "weak: Password must include at least one lowercase letter ."
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Strong: Your password is secure!"
    else:
        return "Weak: Please include at least one special character like this !"


def password_checker():
    print("welcome to the password Strength checker")

    while True:
        password= input("\n enter your password (or type 'exit' to quit):")

        if password.lower() == "exit":
            print("Thank you for using the Password strength Checker! Goodby!")


        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    password_checker()




