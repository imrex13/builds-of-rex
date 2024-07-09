# This is Fizz-Buzz Game where 
# If i is divicible by 3 its Fizz and if it's divicible by 5 it's Buzz
# If its divicible by both 3 & 5 It's FizzBuzz 
def first():
    for i in range(11):
        if i %3 == 0:
            print('Fizz')
        if i %5 == 0:
            print('Buzz')
        if i %3 == 0 and i%5 == 0:
            print('FizzBuzz')
        else:
            print(i)
def second():
    
    for i in range(11):
        out = ''
        if i %3 == 0:
            out += 'Fizz'
        if i %5 == 0:
            out += 'Buzz'
        elif  i %3 != 0 and i %5 != 0:
            out += str(i)
        print(out)
            
a = int(input('Enter 1 or 2: '))
if a == 1:
    first()
elif a == 2:
    second()
else:
    print('Enter the correct Option')

# By Rex on 06-04-2024 