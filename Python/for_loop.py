

for r in ('hii','kay','by'):
    print(f'value: {r}')


for k in 'karnunar':
    print(k,end=',\t')

source = [12,22,34,55]
total=0
for val in source:
    total += val

print(f'\n Sum value: {total}')


print('-------------------')

files = ['data.cSv','Collection.TXT','demo.CSV']

for file in range(0,len(files)):
    files[file] = files[file].strip().lower().replace('txt','csv')

print(files)


table_no =7
for t in range(1,11):
    print(f'{table_no} x {t} = {t*table_no}')

print('*****pyramid******')
# *
# **
# ***
# ****
# *****
# ******
for r in range(0,6):
    for k in range(0,r+1):
        print('*' if k<=r else '',end='')
    print()


#       *
#      **
#     ***
#    ****
#   *****
#  ******
for r in range(6,0,-1):
    for k in range(0,7):
        if k >=r:
            print("*",end='')
        else:
            print(' ',end='')
    print()


#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * * 
for r in range(6,0,-1):
    for k in range(0,7):
        if k >=r:
            print("* ",end='')
        else:
            print(' ',end='')
    print()


# * * * * * * 
# *         * 
# *         * 
# *         * 
# *         * 
# * * * * * * 
mainloop = 6
innerloop=6
for r in range(0,mainloop):
    for k in range(0,innerloop):
        if r==0 or r==mainloop-1:
            print('* ',end='')
        else:
            if(k==0 or k==innerloop-1):
                print('* ',end='')
            else:
                print('  ',end='')
    print()



days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

for day in days:
    if day in ('Sun','Sat'):
        continue
    print(f'Day is: {day}')

    # if day.strip()=='Tue':
    #     print(f'break day {day}')
    #     break


#Else Loop
#--Useful when we wanted to check all iteration are properly complete in loop or not
#--if break/crash happen in this case else not run

for f in ['banan','apple','gua']:
    print(f)
    # if(f =='gua'):    #BECAUSE OF BREAK NOT PRINT ELSE BLOCK
    #     break
else:
    print('Loop printed')