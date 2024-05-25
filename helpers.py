import random


def generate_email():
    login = ''
    for _ in range(3):
        login += random.choice('testfrdrsjmYtbjhb1234567890')
    domain = random.choice(['ya.ru', 'mail.ru', 'gmail.com'])
    email = f'{login}@{domain}'
    return email


def generate_password():
    characters = 'TeSstTeEstTestTTeetTesttt1234567890'
    length = random.randint(6, 10)
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password