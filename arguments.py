def greet(name, msg):
    print("Hello", +name+ ',' +msg)
    
greet("Mellisa", " Good morning!")

def hello(name,age):
    year=2022-age
    return f"Hello {name} you were born in {year}"
from ast import Num
from typing import KeysView


def my_country(country="Kenya"): 
    return f"My country is {country}"

def greet(name):
    return f"Hello {name}"
def greetings(*names):
    for name in names:
        print(f"Hello, {name}")
# Write a functions that accepts any number of intergers and returns the sum 
# of all of those intergers 
   
def sum(*int):
    num=0
    for v in int:
        num+=v
    return num

def multiply(*int):
    product=1
    for v in int:
        product*=v
    return product

def get_multiple(**kways):
    keys=kways.keys()
    values=kways.values()
    print(keys)
    print(values)

def greet_multiple(**kways):
    keys=kways.keys()
    if "coutry" in keys:
        return f"Hello {kways ['names']}from {kways['country']}"
    elif "age" in keys:
        year=2022 -kways["age"]
        return f"Hello {kways['name']} you were born in {year}"
    elif "name" in keys:
        return f"Hello {kways['name']}"
    else:
        return f"Hello anoynmous"
def function(*args,**kwargs):
    print(args)
    print(kways)      
 


