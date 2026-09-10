
def show_student_Data():
    name= input("enter name: ")
    print('student name is: ',name)

    age = int(input('enter your age:'))
    print('your age is:',age,' its Type is:',type(age))
    print('your age is:'+str(age))
    age = str(age)
    age = age +1
    print(age)


    isMale = bool(input('is you male:'))
    print('is male:',isMale)

    inputBlank = input('input blank data:')
    print('blank data:',inputBlank)


# show_student_Data()



# count function use to analyze substring in large string

sentence = """hello how are @% you i am hello and hello"""

print(sentence.count("Hello")) # its case sensative 

print(sentence.count('$'))
print(len(sentence))

#replace function

print(sentence.replace('hello','Hi',2)) #2 is pointer who indicate uptp how many values need to replace

num = "+41 (234)-343455"

print(num.replace('+','00').replace('(','').replace(')','').replace('-','').replace(' ',''))

print(f'this is num string: {num} and {sentence}') 

print(f"2+3= {2+3}") 
print(f'{{this is exporession}}') # directly {'this is'} not allowed need to write twice {{this is ...}}

# below is split seperator

detail = 'naman-24-student 24:44'

print(detail.split(' '))
detail = detail.split(' ')
print(detail[0].split('-'))

 # Transformation

print('ha'*4)
print('=W-'*4)

#Slicing

str_string = 'Hello ji'

print(str_string[0:3])
print(str_string[2:])
print(str_string[2::2])
print(str_string[-4:])

#---------lstrip(),rstrip(),strip()-----------
# by default it remove spaces at left and right
#If pass value to remove it remove any character as per value

normal_str = " open   "

print(normal_str.rstrip()) #trim spaces at right side
print(normal_str.lstrip()) #trim spaces at left side
print(normal_str.strip()) #trim spaces both side

text = "$$8&00".strip('0')
print(text)
#-----------lower(),upper()------------
#use to normalize or clean the case sensative issue in string

text = "new Color IS"
text_data = "new color is"

print(text.upper())
print(text.lower() == text_data)

#challange

ch = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
ch = ch.lower().replace('@','a').strip('968-').replace('(','').replace(')','').replace(';;',',').strip()
print(ch)
ch = ch.strip('y').split(',')
print(ch)
print(f'name: {ch[0]} | role: {ch[1].strip()} | age: {ch[2].strip()}')

#-------[search functions] startswith(),endswith(),in(),find()---------

phone = "+92-3444556677"
print('is Indian number:',phone.startswith('+91'))

#check is this google mail id
mailId= 'ram@gmail.com'
print('is google id:',mailId.endswith('gmail.com'))

url = 'loocalhost://3000/api/register'
print('api' in url) #it is as like for loop in oprator return true if present

#print only numbers not country code

num1 = '91-3366778899'
num2 = '+71-9900887766'
print(num1.find('-')) #get position of - so we can apply slicing

print(num1[num1.find('-')+1:])
print(num2[num2.find('-')+1:])

#----------------Validation--------------

country1 = 'INDIA'
country2 = 'USA2'
print(country1.isalpha()) #check only aphabetical characters
print(country2.isalpha()) #==>false 

num3='234234324'
print(num3.isnumeric()) #check only numbers not even float
num4 = '23'
print(num4.isnumeric())# ==>false

print('9'.isalnum()) # Refers to Alpha numeric

print("-----Operators-----")

a = [2,3,4]
b = [2,3,4]

print(a==b)
print(a is b)

x= 1
y= 1

print(x is y)

email = None

print(email != '' and email is not None) #email != '' is not find None value so use is not also we can use  not email == None

