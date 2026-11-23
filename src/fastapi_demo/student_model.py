# the pydantic needed for validate the fields because normal Disctionary data types can accept any value

# {
#     "name":"", #wrong
#     "age":34,
#     "email":"this is my mail" #wrong
# }

from pydantic import BaseModel


class ValidStudent(BaseModel): #BaseModel varifies the data type and Inputs are correct or not
    name: str
    age: int
    email: str


s1 = ValidStudent(name="Ram",age='24',email="ram@gmail.com")
# s2 = ValidStudent(name="Ram",age='dd',email="ram@gmail.com") #Show error of:Input should be a valid integer, 
print(s1)