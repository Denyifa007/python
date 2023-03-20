#  Variables
'''name = "Oyeindenyifa"
num = 2
num_2 = 9.83
age  = 50
state = "Lagos"
print (state)
print(name)
print(num)
print(num_2)
print(age)
print(name, state, age)

full_name = name + ' Diegbegha'
print(full_name)
a,b,c = 2, 'ikeja', 'lagos'
print(a,b,c)'''

# Data Types
# - String
# - Numbers e.g int, float, complex
# - Sequence e.g lists, sets, tuples, 
# - Dictionary

# Strings
surname = 'RashFord'
first_name = ' Oliver'
full_name1 = surname + first_name
age = '33'
gender = 'Male'
bmi = 80
print(type(surname), (first_name), (full_name1), (age), (gender),)
print(type(bmi))
print(full_name1, 'is a', gender, 'and he is', age, 'years old' )


#  Strings methods len, upper, lower, slice, endwith, startwith
# len()
print(len(full_name1))
# index[]
print(surname[0])
print(surname[1])
print(surname[2])
print(surname[3])
print(surname[4])
print(surname[5])
print(surname[6])
print(surname[7])
# upper()
print(full_name1.upper())
# lower()
print(surname.lower())
#  slice [start:end]
print(full_name1[0:4])
name1 = "Oluremi"
print(name1[0:3])
print(name1[3:7]. capitalize())
print(full_name1[:8])
print(full_name1[9:])
acad = 'Techstudio'
print(acad[0:-6])
print(acad[4:].capitalize())

# title()
multi_str = 'My name is Blard, I love Python'
print(multi_str.title())
print(multi_str.endswith('on'))
print(multi_str.startswith('on'))


# String formatting f
more_tr = print(f'{multi_str} and javsscript at {acad} and am {age}')
print(multi_str.split(',')[0])

# //////////////////////////////////////////////////////////////////////////
print('=================Number==============')
# Number Date
num1 = 10
gravity = 9.81
com_num = 2j
print(num1, type(num1))
print(gravity, type(gravity))
print(com_num, type(com_num))
num3 = str(num1)
print(num3, type(num3))
my_sum = num1 + int(num3) - int(age)
print(my_sum)


a=4
b=10

print(f'the sum of {a} and {b} is {a+b}')
print('the sum of {} and {} is {}' .format(a,b, a+b))

first_name1= ' Oyeindenyifa'
last_name= 'Diegbegha'
age = 67
location="Lagos"
national= 'Nigeria'
occupation= 'Fullstack Developer'
gender= 'male'
full_name2= last_name + first_name1

print(f'My name is {full_name2}, i am a {gender} and am {age} years old, i\'m from {national}, live in {location} and am a {occupation}')

# Task one

s ='My name is Fred, A fullstack developer'
print(s.split (',')[0])
print(s.split (',')[1].strip().capitalize())

x='8'
y= 5
print(type(x))
print(type(y))

print(x*3)
print(x*y)

print(int(x)*y)
print(x)
print(y)

tech_stack = 'html,css,javascript,python,node'
front_end = back_end = tech_stack.upper().split(',')
print(front_end)
print(front_end[0], front_end[1], front_end[2])
print(back_end[3].title(), back_end[4].title(),)

# Booleans
a = 5
b = 10
c = '5'
print(a==b)
print(a<b)
print(a==c)
print(type(a==c))

# Operators
# 1 ASSIGNMENT OPERATOR =, <, >, +=, -+, *=, <=, >=

x = 8
y = 3
if x<y:
    print(x+y)
else: 
    print(y-x)
# ARITHMETIC OPERATORS +, -, *, /, //, %, **

m = 10
n = 231
p = -26

print(n+m-p**2/6*2)
print(n+m-p**2//6*2)
print(n/m)
print(n//m)
if n%m == 0:
    print('m is a factor of n')
else:
    print('this is all jazzzz!!  ' *4)
    
# LOGICAL OPERATOR and, or, not

j = 3
k = 8
l = -2
z = 6

_try = (k>j) and (l<k)
print(_try)
do_math = (k+l or k) == (z)
print(do_math)

if _try:
    print('We\'re good!')
else:
    print('Wahala dey oo!')
if not _try:
    print('We\'re good!')
else:
    print('Wahala dey oo!')
    
# Comparison Operators ==, !=, >, <, >=, <=
    
if (j != k):
    print('The parameters are not equal')
else:
    print('The parameters are equal')

# input() 
    
'''name = input('What is your name: ')
print(name)'''

'''def _sum(a,b):
    return a+b
print(_sum(2,3))'''

'''age = input('What is your age? ')
print(age,type(age))'''

'''def sth():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print(num1+num2)
sth()'''

'''def rec():
    length = int(input('Enter the length of the rectangle: '))
    breadth = int(input('Enter the breadth of the rectangle: '))
    area = length*breadth
    print(f'The area of the rectangle is {area}cm^2')
rec()'''

# Lists Data type
print('===LIST===')
# List is a  collection of items/(any data type) in a sq bracket []
# i.e array
'''my_arr = list()
print(type(my_arr))'''

'''lst = ['Boobs', 'Ass', 19, 10,9.2, True, [2,3], (1,2,5)]'''
# List method index, slice,len
# len()
'''print(len(lst))
# pop()
print(lst.pop())
a,b,c, *rest, d = lst
print(a)
print(b)
print(c)
print(*rest)
print(d)'''

# Slicing[start:end]
'''new_lst = lst[5:7]
print(new_lst)
print(new_lst[1] [1]) 

rev_lst = lst[::-1]
print(rev_lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0::2])
print(fruits[1::2])
print(fruits[::3])
'''

# Task 1
scores = [22, 19, 24, 25, 26, 24, 25, 24,15]
'''
a) Arrange the scores in ascending order
b) Arrange the scores in descending order
c) Print the even scores Hint: use list comprehension
d) Print only the maximum score
e) Print only the minimum score
'''
# Solution

scores = [22, 19, 24, 25, 26, 24, 25, 24,15]
print(scores.count(24))

# a
scores.sort()
print(f'In acsending order {scores}')
# b
scores.sort(reverse=True)
print(f'In decending order {scores}')
# c
# for i in range(len(scores)):
#     list1 = []
#     if i%2==0:
#         list1.append(i)
#         print(list1)
          
even_scores = [i for i in scores if (i % 2 == 0)]
odd_scores = [i for i in scores if (i % 2 != 0)]
print(f'Odd scores {odd_scores}')
print(f'Even scores  {even_scores}')
# d
print(F'MAX score {max(scores)}')
# e
print(f'MIN score {min(scores)}')
# print(len(scores))
# mid_index = len(scores)//2
# print(scores[mid_index])

# Task 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
a) Join the two lists above and store in a variable my_stacks
b) Copy the joined list and assign it to a variable full_stack.
c) Then insert 'Python' and SQL after 'Redux'.
'''
# Solution
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# a
my_stack= front_end + back_end
print(my_stack)
'''front_end.extend(back_end)
print(front_end)'''
'''back_end.extend(front_end)
print(back_end)'''
# b
full_stack = my_stack.copy()
print(full_stack)
index = full_stack.index('Redux')
full_stack.insert(index+1, 'Python')
full_stack.insert(index+2, 'SQL')
print(full_stack)

# Tuple
# Tuple is one of the four collection or sequence data type in python
# Tuple can be created using () or Tuple constructor function Tuple()


tpl = ('strings', -3, True)
print(tpl, type(tpl))
print(len(tpl))
print(tpl[1])
print(tpl[2])

tpl1 = tuple((3, 'funny', 3)) 
print(tpl1, type(tpl1))
# Accessing tuple 
print(tpl1[2])
print(tpl1[1])

# len()
print(len(tpl1))

# udating tuples
tpl1_lst = list(tpl1)
print(tpl1_lst)
tpl1_lst.insert(1, 'item1')
print(tpl1_lst, type(tpl1_lst))


# chnage bak to tuple
tpl1_lst=tuple(tpl1_lst)
print(tpl1_lst, type(tpl1_lst))
team = ('LVP', 'PSG', 'ARS', 'CHE', 'MAN')
new_team = team[1::2]
print(f'The wining team {new_team}')

# SETS
# Set is also a collection data type but its element are enclosed in a  curly braces {}
# set unordered, unindexed
# Once a set is created we cannot change any items buts we can add additional items.
# Set deos not recognize duplicate

# Creating sets
my_set = set({'smallville', 12.3, 10, True, 'food'})
print(my_set, type(my_set))
my_colors = {'black', 'blue', 'green', 'red', 'pink'}
'''print('green' in my_colors)'''

# Updateing sets update()
add_colors = {'purple', 'yellow', 'white', 'skyblue'}
my_colors.update(add_colors)
print(my_colors)

new_data = {1,8, 'black', False, True,0}
print(new_data)
# Removing item in an array
# new_data.remove('black')
# print(new_data)

# Since set is not ordered or indexed, we can only access it via looping, however we can add and remove items from the set
# use .add() to add one item only
# use .update() to add multiple item.
# use .remove() to a spe
# cified item

# Adding one item to set add()
new_data.add(3)
# print(new_data)

# adding multiple items .update()
extra_items = {2,9,'hello'}
new_data.update(extra_items)
# print(new_data)

# removing item
new_data.remove('black')
# print(new_data)

# pop() will remove random item and return the removed item
# clear() will clear will clear all the items, returns empty set
# del will delete the set whole set



# Controle flow if, elif, for, range, while

# a = 5
# b = 15
# if a < b:
    #   
#     input('Do you care for a drink?')
#     print(' Thanks boss!')
# else:
#     print('Nothing for you!')
# if a > b:
#     input('Do you care for a drink?')
#     print(' Thanks boss!')
# else:
#     input('Why?')
#     print('Because 5 is lesser than 15')
    
my_numbers = [0,1,2,3,4,5,6,7,8,9,10]
'''for i in my_numbers:
    int(input('Enter number'))
    if (i % 2) == 0:
            print('The number is even')
    else:
        print('The number is odd')'''

# using for loop
'''for i in range(3):
    try:
        
        my_numbers = int(input("Enter an integer: "))
        break
    except ValueError:
        print('Invalid input. Please enter an integer. ') 
else:
    print('Max attempts reached. Exiting program..')
    exit()
    
if my_numbers % 2 == 0:
            print('The number is even')
else:
    print('The number is odd')'''
    
# a = 5
# b = 9
# c = 9

    
# for n in range(4):
#     try:
#         a = int(input("Enter the right interger: "))
#         b = int(input("Enter the right interger: "))
#         c = int(input("Enter the right interger: "))
#         break
#     except:
#         print('Invalid input added. Please enter the right interger.')
# else:
#     print('You have exhausted your attempts. Existing page..')
    
# for Loop

cars = ['mercedes', 'lexus', 'Toyota', 'Rangerover', 'Rolls royce', 'Honda', 'BMW']
# for car in cars:
    # print(f'My favourite car is {car}')

# for brand in cars:
#     if brand == 'Rolls royce':
#         print(f'My best car is {brand}')
 
# epl= ('CHE', 'LIV', 'MANU', 'ARS', 'EVE')
# for club in epl:
#     if 'A' in club:
#         print(club)
        
# for w in range(11):
#     print(w)
# for double in range(1,20,2):
#     print(double)
    
# While Loop
i = True
# while i:
#     print('While loop running...')
#     break

c = 0 
while c <  3:
    print(f'My best car brand {cars[c]}')
    c += 1
# Dictionary
# Dict is one of the four collection data type
# dict are key-value pair of data stored in a curly braces {}

dct = {'key1': 'value1' ,
       'key2' : 'value2' ,
       'key3': 'value3',
       'key4' : 'value4'
       }

data = {
    "name" : 'Denyifa',
    'age' : '60',
    'gender' : 'Male',
    'occupation' : 'fullstack dev',
    'state' : 'Lagos',
    "fav_food" : {'fried rice', 'platain', 'beans', 'indomie'},
    'DOB' : {
        'day' : '15th',
        'month' : 'sept',
        'year' : '1970',
  
    },   
    'Address': {
        'No' : 124,
        'street': 'omole estate'
    },
    }

# Accessing dict
# print(dct['key1'])
# print(dct.get('key2'))

print(data['Address']['street'])
print(data['fav_food'])
# print(data['DOB']['month'])

dob1 = data['DOB']["day"] 
dob2 = data['DOB']["month"] 
dob3 = data['DOB']["year"] 
print(dob1,dob2,dob3)

# Adding items to a dict

dct['key4'] = [1,2,3,4, True, 'sexy']
print(dct)

# Checking for a Key
print('key5' in dct)

# Removing key-value from a dict
# pop(key) removes any specific key
# print(dct.pop('key2'))

# last item
# pop take off the last item in a dict and print it in a tuple
print(dct.popitem())
print(dct)

# del dct[]
del dct['key1']
print(dct)

# it highlights the dict in a tuple
print(dct.items())
 
# .keys is used to fecth key items in a dict and print it out in a tuple
print(dct.keys())

# ASSIGNMENT 

'''Exercise: One 
1) Create a tuple containing names of your sisters.
2) Create a tulle containing names of your brothers. (imaginary siblings are fine)
3) Join brothers and sisters tuples and assign it to siblings
4) Print the total number of your siblings (total _siblings)
5) Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
6) Unpack siblings and parents from family_members.'''

# SOLUTION 1
# 1
names_sisters= ('prasie', 'timi', 'vick', 'tokoni', 'rose')
print(names_sisters)
# 2
names_brothers = ('Ebiye', 'Preye', 'Tarila', 'Andre', 'Tombra')
print(names_brothers)
# 3
siblings = names_sisters + names_brothers
print(siblings)
# 4
total_siblings = len(siblings)
print(total_siblings)
# 5
parents = ('Abamu', 'Helen')
family_members = siblings + (parents)
print(family_members)
# 6
new_family = list(family_members)
print(new_family)

a,b,c,d,*rest = new_family
print(a)
print(b)
print(c)
print(d)
print(*rest)


# Excercise two
z= range(1,100,3)
for d in z:
    print(d)
    
for count in range(0,11):
    multiply = count * count
    print(count, 'X', count, '=', multiply)
    
num = 8
for a in range(1,13):
    print(num, 'X', a, '=', num*a)
    
for count in range(0,12,1):
    x = count +1
    multiply = count*(x)
    print(count,'X', x, '=', multiply)
    
# ALternatively
n = 0
while n < 11:
    print(f'{n} x {n+1} = {n*n}')
    n = n+1
    
# WEEK TWO
# Functions
# Function is a block of code performing a specific task.

# syntax
# Delcaring a function
# def function_name():
            # codes
            # codes
# calling a function
# function_name()

def example_function():
    print('This is a function')
example_function()

def add_numbers():
    num_one= 12
    num_two= 32
    total = num_one + num_two
    print(total)
add_numbers()

# Class work
# A = PI*r**2  PI = 3.142
# when r = 3.5

PI= 3.142
R= 3.5
calc_area= PI*R**2
print(calc_area)

def calc_area():
        PI = 3.142
        R=3.5
        A= PI*R**2
        print(int(A))
calc_area()

def cal_area1(PI, R):
    A = PI * R**2
    print(A)
cal_area1(3.14,3.5)

# Function with parameters
def full_name(first_name, last_name):
    print(f'My name is {first_name} {last_name}')
full_name('Denyifa', 'Samuel')

def sum_of_numbers(s):
    total = 0
    for w in range(s+1):
        total+=w
    print(total)
sum_of_numbers(10)
# print(sum_of_numbers(10)) 
# print(sum_of_numbers(100)) 

# Abitrary arguments, *arg
siblings = ['Denyifa', 'Preye', 'Rose', 'Sylvia', 'Vick']
def my_family1():
    for name1 in siblings:
        print(f'My family members are {name1}')
my_family1()

def my_siblings(*b):
    print(f'The youngest child is {b[3]}')
    print(f'The eldest child is {b[4]}')
    print(f'The smartest child is {b[0]}')
    print(f'The richest child is {b[2]}')
my_siblings('Denyifa', 'Preye', 'Rose', 'Sylvia', 'Vick')

#   keyword argument **arg
# Key1 = value
def mycal(l,b,h):
    Vol = l*b-h
    print(f'Volum is {Vol}cm^3')
mycal(4,6,2)

def mycals(**g):
    print('Volume is ' + g['key3'])
    print('Volume is ' + g['key1'])
    print('Volume is ' + g['key2'])
mycals(key1='Taiwo', key2= 'Praise', key3='Denyifa')

def cal_vols(**z):
    vol = z['key7'] *z['key6']-z['key5']
    print(f'the Volum is {vol}cm^3')
cal_vols(key5 = 3, key6 = 6, key7 = 9)

# Return statement
def my_return(first,second):
    return f'My full name is {first} {second}'
print(my_return('Rashford' ,'Marcus'))

def do_sum(a,b):
    return a+b*a-b
print(do_sum(5,6))

# pass
def do_pass():
    # Empty function
    pass
do_pass()

# continue
fruits = ['apple', 'orange', 'lemon', 'kiwi', 'grapes', 'mango']
def fav_fruit():
    for fruit in fruits:
        if fruit =='lemon':
            continue
        print(f'mY Favourite fruit is {fruit}')
fav_fruit()

def find_even_num(n):
    evens = []
    
    for r in range(n+1):
        if r % 2 == 0 :
            if r == 0 :
                continue
            evens.append(r)
    return evens
print(find_even_num(20))

# Lambda function
# lambda args : expression
my_sum = lambda a: a**2
print(my_sum(10))


cylindar_vol = lambda r, h: 3.14159 * r**2 * h
vol = cylindar_vol(4,8)
print(int(vol))

# Assignment

# Write different functions which take lists. They should calculate_mean,
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).

# what is a module
# A modul is a file containing a set of codes or  a set of functions which
# can be included to an application. A module could be a file containing a s ingle varialble, a function or big code base.

# import modules
# print(modules.generate_tax(2500,15))

from modules import generate_tax as my_tax, my_full_name as title, mean_age as cal_mean, media_age as cal_media, stdev_age as cal_stdev, mode_age as cal_mode, variance_age as cal_variance, range_age as cal_range
print(my_tax(2500,15))

print(title(first= 'Oyeindenyifa', second = ' Diegbegha', age=' 50'))


# import Built-in Modules
# like other programming languages we can also import modules by importing the file/function
# using the key worj import. Lets import the common module  we will use most of the time.
# some of the common built-in modules: math, datetime, os, sys, random, satatistics, collections,
# json, re.

# Math module
import math
print(math.pi)
print(math.floor(math.sqrt(434)))
print(math.ceil(math.sqrt(434)))
print(math.pow(2,5))
print(math.log10(100))

# from math import pi, [importing only one math method]

from random import randint, random 
print(random())
print(randint(1,10))

# statistics
from statistics import mean,median,stdev,mode
print(cal_mean())
print(cal_media())
print(cal_stdev())
print(cal_mode())
print(cal_variance())
print(cal_range())

# random, randint

# re

'''
Regular Expressions
A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

The re Module
After importing the module we can use it to detect or find patterns.

import re
'''
import re 
# re.match()
email = 'Denyifasamuel@hotmail.com'
match_it = re.match('@', email[13:],)
print(match_it)

# re.search
search_it = re.search('.com', email)
print(search_it)

find_it = re.search('denyifa', email, re.I)
print(find_it)

# re.findall
txt2 = 'Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language.'
match_py = re.findall('Python', txt2,re.I)
print(match_py)

# re.sub
sub_py = re.sub('[Pp]ython', 'Javascript', txt2,re.I)
print(sub_py)

regex_pattern = r'Language'
my_regex_match = re.findall(regex_pattern,txt2,re.I)
print(my_regex_match)

# '''Assignment
# Change the dictionary "person_dict" to a JSON "person_json". 
# a) Print(person_dict)
# b) Print(type(person_dict))
# c) Print(person_json)
# d) Print(type(person_json))'''
# person_dict = {
#     "name": "Blard",
#     "country": "Nigeria",
#     "city": "Lagos",
#     "skills": ["JavaScrip", "React", "Python"]
# }

# Solution
person_dict = {
    "name": "Denyifa",
    "country": "Nigeria",
    "state of origin": 'Bayelsa',
    "age": '40',
    "city of residence": "Lagos",
    "skills": ['Bootstrap',"JavaScript", "React", "Python", 'Dgango']
} 
print(person_dict)
print(type(person_dict))

import json
person_json = json.dumps(person_dict)
print(person_json) 
print(type(person_json)) 

# To change jsonnback to dict you use json.loads()
new_list = json.loads(person_json)
print(new_list, type(new_list))

# 00P
# Classes
# Python is an object oreinted programming language, with its properties and methods.
# Everything in python is an object of a correspoding built-in class.
# We instantiate a class to create an object, however the class defines the attributes and behaviour of the object.

# Creating a class
# To create a class, we use the 'class' keyword.

# Class Classname:
        # codes to run

class Person:
    pass
print(Person)

person1 = Person()
print(person1)

class Person:
    def __init__(self, first_name, last_name,gender,age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.city = city
        self.stacks = []
    def person_info(self, income):
        self.icome = income
        return f"My name is {self.first_name} {self.last_name}, I am a {self.gender} and am {self.age} years old. I live in {self.city} and the list of my statcks are {s.stacks}. and i earn {income} monthly. "
    def add_stack(self, para, stackS, states):
        self.stacks.append(para) 
        self.stacks.append(stackS) 
        self.stacks.append(states) 
        
s=Person("Denyifa", 'Diegbegha', 'male', 40, "Eko",)
s.add_stack('JAVASCRIPT', 'PYTHON', 'DJANGO')
more_stacks = ['CSS', 'React']
s.stacks.extend(more_stacks)
print(s.stacks)
print(s.person_info('15000'))

    
# p= Person("Denyifa", 'Diegbegha', 'male', 40, "Eko")
# print(p.person_info()) 
      
             
# person1 = Person('Denyifa', 'Diegbegha', 'male', 40)
# print(f'My name is {person1.first_name} {person1.last_name}, am a {person1.gender} and i am {person1.age} years old')

# Class inheritance using the super()
# The super() built-in function gives child class access to the main/parent properties. However, when we add the init() function, the child class will no longer inherit the child class will no longer inherit the parent's init() funtion.

class Small_person(Person):
    def __init__(self, first_name, last_name, gender, age, city, job):
        self.job = job
        super().__init__(first_name, last_name, gender, age, city)
        
    def small_person_info(self):
            return f"My stacks is {t.stacks} and my job is {t.job}"

            
    
    
    
t = Small_person('Marcus', 'Rashford', 'male', 24, 'Manchester', "Fullstack dev")
new_stack = ['tailwind', 'node.js']
s.stacks.extend(new_stack)
print(t.person_info(10000))
print(t.job)
print(t.age)
t.add_stack('Html', 'Django', 'Python')

print(t.small_person_info())

# Task
'''
1) Create a class 'Bank_account' with contructor that has two parameters, 'name' and 'money'
2) Create inside the Bank_account class three methods, one for 'deposit', 'withdraw', 'checkbalance'.
3) Create an instance of BankAccount. i.e b1 = Bankaccount('Denyifa', 400)
4) Print(b1.withdraw(500)). nd: this should show a msg
"Insufficent funds" since 400<500
5) Deposit 500 using b1.deposit(500) method and check the available balance using print(b1.checkbalance()) method.'''

# SOLUTION
# 1)
class bank_account:
    def __init__(self, name,money):
        self.name = name
        self.money = money
    def deposit(self, money):
        self.money += money 
    
    def withdraw(self, dec):
        if self.money > dec:
            self.balance = self.money - dec
            return self.money
        else:
            return 'Insufficent funds! you no get money'
        
    def check_balance(self):
        return self.balance
       
            
        
  
        
    
        
b1 = bank_account('Denyifa', 400) 
print(b1.name)
print(b1.money)
b1.deposit(500)
print(b1.money)
print(b1.withdraw(600))
print(b1.check_balance())










    
    
    
    










    

    

        
    
         
    
    
        
          
        
        
























