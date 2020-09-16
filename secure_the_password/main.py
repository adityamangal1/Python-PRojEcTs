
'''
Author: Aditya Mangal 
Date:  22 september,2020
Purpose: python practise problem

'''

secure = (('s', '$'), ('o', '0'), ('1', '!'), ('a', '@'), ('f', '#'),('l','|'),('q','*'))


def secure_password(password):
    for a, b in secure:
        password = password.replace(a, b)
    return password


if __name__ == "__main__":
    user = input('Enter your password\n')
    password_secured = secure_password(user)
    print(f"Your secures password is {password_secured}")
