from cryptography.fernet import Fernet

master_pwd=input('what is ur master password? ')


'''def write_key():
  key=Fernet.generate_key()
  with open('key.key', 'wb') as key_file:
    key_file.write(key)'''

def load_key():
  key=Fernet.generate_key()
  with open('key.key', 'wb') as key_file:
    key_file.write(key)

def view():
  with open('passwords.txt','r') as f:
    for line in f.readlines():
      data=line.rstrip()
      user, pwds=data.split('|')
      print('username:',user, 'password:',pwds)

 

def add():
  name=input('Account name: ')
  pwd= input('Password : ')

  with open('passwords.txt','a') as f:
    f.write(name + '|' + pwd)


while(True):
  mode = input('would u like to add a new password or view existing password (view, add) press q to quit ?').lower()
  if mode=='q':
    break

  if mode=='view':
    view()
  elif mode == 'add':
    add()
  else:
    print('Invalid mode')
    continue

