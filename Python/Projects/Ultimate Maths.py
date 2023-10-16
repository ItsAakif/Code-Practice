print('''Options Present :-
    for add type ------------- "ad()"
    for subtract type -------- "sb()"
    for multiply type -------  "ml()"
    for divide type ---------  "dv()"
    for remainder type ------  "re()"
    for Table type ----------- "table()"
    ''''\n','\t')



def re():
    while True:
        a=int(input('Enter 1st number '))
        a1=int(input('Enter 2nd number '))
        b=a%a1
        print('\n','\t',b)
        print('\n','\t','\n','\t','Want to see about more remainders')
        print('Press  y or n')
        ch=input()
        if ch=='n':
            break

    print('''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for remainder type ------  "re()"
for Table type ----------- "table()"
''''\n','\t')


def dv():
    while True:
        a=int(input('Enter 1st number '))
        a1=int(input('Enter 2nd number '))
        b=a/a1
        print('\n','\t',b)
        print('\n','\t','\n','\t','Want to divide more numbers?')
        print('Press  y or n')
        ch=input()
        if ch=='n':
            break
    
    print(''''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for remainder type ------  "re()"
for Table type ----------- "table()"
''''\n','\t')


def ml():
    while True:
        a=int(input('Enter 1st number '))
        a1=int(input('Enter 2nd number '))
        b=a*a1
        print('\n','\t',b)
        print('\n','\t','\n','\t','Want to multiply more numbers?')
        print('Press  y or n')
        ch=input()
        if ch=='n':
            break
    
    print('''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for Table type ----------- "table()"
for remainder type ------  "re()"
''''\n','\t')


def ad():
    while True:
        a=int(input('Enter 1st number '))
        a1=int(input('Enter 2nd number '))
        b=a+a1
        print('\n','\t',b)
        print('\n','\t','\n','\t','Want to Add more numbers?')
        print('Press  y or n')
        ch=input()
        if ch=='n':
            break

    print('''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for remainder type ------  "re()"
for Table type ----------- "table()"
''''\n','\t')



def sb():
    while True:
        a=int(input('Enter 1st number '))
        a1=int(input('Enter 2nd number '))
        b=a-a1
        print('\n','\t',b)
        print('\n','\t','\n','\t','Want to subtract more numbers?')
        print('Press  y or n')
        ch=input()
        if ch=='n':
            break

    print('''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for remainder type ------  "re()"
for Table type ----------- "table()"
''''\n','\t')






def table():
    while True:
        n=int(input('Enter the Number '))
        for i in range(1,11):
            print(n,'x',i,'=',n*i)
        print('\n')    
        print('Want to know table of More numbers?')
        print('Press "Y" for YES or Press "N" for No ')
        ch=input()
        if ch=='n' or ch=='N':
              break

    print('''Options Present :-
for add type ------------- "ad()"
for subtract type -------- "sb()"
for multiply type -------  "ml()"
for divide type ---------  "dv()"
for remainder type ------  "re()"
for Table type ----------- "table()"
''''\n','\t')
