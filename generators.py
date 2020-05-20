with open('10-million-password-list-top-1000000.txt') as file:
    content = file.read()
    password_list = content.split('\n')


def generate_popular_passwords(state):
    """
    The function takes popular password from txt.file
    States is needed in order to know what time they are called
    and read the list. So we can iterate over to the next passwords.
    """
    if state is None:
        state = 0
    if state >= len(password_list):
        return None, None
    return password_list[state], state + 1


login_list = ['egor', 'bogdan']  # users that we want to hack


def generate_logins(state):
    """
    Factory of logins
    """
    if state is None:
        state = 0
    if state >= len(login_list):
        return None, None
    return login_list[state], state + 1


# you can add some different symbols in the alphabet in order to increase the amount passwords
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def generate_passwords_brute_force(state):
    """
    Method - Brute-Force Attack
    This function generates passwords from 0
    until the password become is right
    """
    if state is None:
        state = [0, 0]

    password_length, current_step = state

    password = ''

    i = current_step
    while i > 0:
        remainder = i % base
        password = alphabet[remainder] + password
        i = i // base

    password = alphabet[0] * (password_length - len(password)) + password

    current_step += 1
    if password == alphabet[-1] * password_length:
        password_length += 1
        current_step = 0

    return password, [password_length, current_step]
