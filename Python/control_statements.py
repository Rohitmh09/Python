
score  = 90

if(score >= 90):
    print("A")
elif(score >=80):
    print('B')
else: 
    print("C")


grade = "A" if score >=90 else 'B'
print(f'grade: {grade}')


#--------------------------------
email = 'ram@gmail.com'
password = 'dFdsf@Kls'

if not len(password) >= 8:
    print('password must be at least 8 characters')

elif not email != password:
    print('pass cant be equal to email')

elif not any(c.isupper() for c in password):
    print('password must be one upper case')

elif not any(p.islower() for p in password):
    print('password must be one lower case')
else:
    print('correct password')
          

print(any(c.isupper() for c in password)) # show combined result if any one is true return is