def generate_tax(income,percentage):
    tax = income*percentage/100
    return tax
# print(generate_tax(2500,15))

def my_full_name(**f):
    full_name =  f"My name is {f['first']} {f['second']}, i am {f['age']} years old."
    return full_name 

# def my_full_name(first,second,age):
#     full_name = f'My name is {first} {second} and i am {age} years old'
#     return full_name

def print_pattern(n):
    for i in range(n+1):
        print('*'*i)
print_pattern(9)
     
from statistics import mean,median,stdev,mode,variance    
age= [20,15,30,40,35,33,29,40]

def mean_age():
        return mean(age)
    
def media_age():
       return median(age)
   
def stdev_age():
       return stdev(age)
   
def mode_age():
       return mode(age)
   
def variance_age():
       return variance(age)
   
def range_age():
    return max(age) - min(age)

import random,string
# print(string.ascii_letters)
def OTP_generator():
    chart_num = int(input('Enter a number: '))
    # num_OTPs = int(input('Number of OTPs to generate: '))
    for i in range(chart_num+1):
        OTP = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=9))
        print(f'Here is your OTP: {OTP}') 
        
# OTP_generator()
    
    
    
