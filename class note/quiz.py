

print ('WELCOME TO THE MULTIPLE CHOICE TEST\n')
name = input('ENTER YOUR NAME\n ')
print ('\nHI THERE ' + name + '! LET''S START A QUIZ!\n')
print ('I will ask you 10 questions')
print('Negative mark is there ! For correct answer +10 mark and incorrect answer -5')
print ('\n.....................................................\n')

score = 0
score = int(score)

print ('QUESTION 1: WHAT IS THE LARGEST OCEAN IN THE WORLD?\n')
print ('A. The Indian Ocean')
print ('B. The Pacific Ocean')
print ('C. The Atlantic Ocean')
print ('')

Q1answer = "B"
Q1val= input('Your answer : ')

if (Q1val != Q1answer):
    print ('Sorry, that is incorrect!')
    score = score - 5
    print ('Your current score is ' + str(score) + ' out of 100')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 10

print ('Your current score is ' + str(score) + ' out of 100')
print ('\n........................................................\n')

print ('QUESTION 2: AUSTRALIA IS A ...\n')
print ('A. continent')
print ('B. island')
print ('C. very hot place')
print ('')

Q2answer = "A"
Q2val= input('Your answer : ')

if (Q2val != Q2answer):
    print ('Sorry, that is incorrect!')
    score = score - 5
    print ('Your current score is ' + str(score) + ' out of 100')
else:
    print ('Well done! ' + Q2response + ' is correct!')
    score = score + 10

print ('Your current score is ' + str(score) + ' out of 100') 
print ('\n.......................................................\n')





