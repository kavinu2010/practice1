'''print('welcome to my computer quiz!')
playing=input('Do you want to play? ')

if playing.lower()!='yes':
  quit()

print("okay! let's play:  ")
score=0

answer=input('what does CPU stands for? ')
if(answer.lower()=='central processing unit'):
  print('correct!')
  score+=1
else:
  print('Incorrect!')

answer=input(' what does GPU stands for? ')
if(answer.lower()=='graphic proceesing unit'):
  print('correct!')
  score+=1
else:
  print('Incorrect!')

answer=input('what does RAM stands for? ')
if(answer.lower()=='random access memory'):
  print('correct!')
  score+=1
else:
  print('Incorrect!')

answer=input('what does PSU stands for? ')
if(answer.lower()=='power supply'):
  print('correct!')
  score+=1
else:
  print('Incorrect!')

print(f'You got {score} , correct answer')
print(f'You got {(score/4)*100}% , correct answer')


print('welcome to my computer quiz!')
playing=input('Do you want to play? ')

if playing.lower()!='yes':
  quit()

print("okay! let's play:  ")



def question(que):
  score=0
 
  if(answer.lower()=='central processing unit'):
  
   print('correct!')
   score+=1
  else:
   print('Incorrect!')
  print(f'You got {score} , correct answer')
  print(f'You got {(score/4)*100}% , correct answer')



answer=(input('what does CPU stands for? '))
question(answer)
answer=(input(' what does GPU stands for? ') )
question(answer)
answer=(input('what does RAM stands for? '))
question(answer)
answer=(input('what does PSU stands for? '))
question(answer)
 '''



print('Welcome to the quiz game')
user_input=input('would you like to play the quiz?>>  ').lower()
if user_input!='yes':
  print('Thank you see you again')
  exit()

print('Ok will start the quiz now')
score=0

user_answer=input('what does CPU stands forn? ').lower()

if(user_answer=='central processing unit'):
  print('correct !')
  score+=1
else:
  print('Incorrect !')

user_answer=input('what does PAN stands forn? ').lower()
if(user_answer=='permanent account number'):
  print('correct !')
  score+=1
else:
  print('Incorrect !')

user_answer=input('what does NAN stands forn? ').lower()
if(user_answer=='not a number'):
  print('correct !')
  score+=1
else:
  print('Incorrect !')

print(f'your score is {score}')