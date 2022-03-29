# Another warm up exercise to practice the fundamentals of python


#1 | While loops

a = 10
b = 40
c = 30

while a <= b:
    print('a is {} and b is {}'.format(a, b))
    break
if b <= c:
    print('b is {} and c is {}'.format(b, c))
else:
    if a or b > c:
        print('a, b, and c are {}, {}, {}'.format(a, b, c))

        

#2 | Using range in a for loop

for num in range(0, 10):
    if num % 2 == 0:
        print(num)

        
        
#3 | Additional way to get our last answer with range

for num in range(0, 10, 2): # this gives us the same answer as our last block of code
    print(num) # prints num in range starting at 0, up to 9, at a step count of 2.

    
    
#4 | Index counting for a string

index_count = 0

for letter in 'abcde':
    print('At index {}, the letter is {}'.format(index_count, letter))
    index_count += 1
    

#5 | Using enumerate

string = 'Practice every day'

for index, letter in enumerate(string):
    print(index, letter)
