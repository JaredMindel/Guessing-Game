import os

os.chdir(r'C:\Users\jared\Dev-10 Module Exercises\Python\Python Basics\Guessing Game')
print(os.getcwd())

rules_file = open(r'Rules.txt')
rules = rules_file.read()
print(f'{rules}')