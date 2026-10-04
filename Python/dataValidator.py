

class DataValidator:
    def __init__(self):
        self.errors = []

    def email_validator(self,email):
        if '@' not in email:
            self.errors.append(f'invalid email: {email}')
            return False
        return True

    def age_validator(self,age):
        if not age.is_integer():
            self.errors.append(f'Invalid age not a number: {age}')
            return False
        if age < 0 or age >200:
            self.errors.append(f'Invalid age: {age}')
            return False
        return True

    def call_validator(self,email,age):
        self.email_result = self.email_validator(email)
        self.age_result = self.age_validator(age)
        print(f'is email correct: {self.email_result}')
        print(f'is age correct: {self.age_result}')

        if self.email_result ==False or self.age_result ==False:
            print('Error List: \n',self.errors)


if __name__ =='__main__':
    email = 'child@gmail.com'
    age = 201
    child = DataValidator()
    if child.email_validator(email) and child.age_validator(age):
        print('correct mail and age')
    else:
        print(child.errors)

    child.call_validator(email,age)

