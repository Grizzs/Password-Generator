import random



char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%£&*().,?0123456789'


print('---- PASSWORD GENERATOR ----')
print()


length = input('How long does your password needs to be? ')
while (length.isdigit() == False):
    length = input('How long does your password needs to be? ')

length.isdigit()

    


length = int(length)

for PwD in range(length):
    password = ''
for C in range(length):
    password += random.choice(char)


print(password)
    
