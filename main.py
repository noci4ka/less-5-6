import requests 
 
def first_function(): 
    pass 
 
class Human: 
    pass 
  
rq = requests 
first_f = first_function 
nick = Human 
  
print(requests.__name__) 
print(rq.__name__) 
print(first_function.__name__) 
print(first_f.__name__) 
print(Human.__name__) 
print(nick.__name__) 
print(__name__)

data = "text" 
  
print(hasattr(data, 'reverse')) 
print(hasattr(data, 'index'))

print(getattr(data, 'startswith')) 
print(getattr(data, 'startswith', None)) 
print(getattr(data, 'reverse', None))

data = "text" 
  
def first_func(): 
    pass 
  
print(callable(data)) 
print(callable(first_func))

class First_class: 
    pass 
  
class Second_class(First_class): 
    pass 
  
obj_from_class_2 = Second_class() 
  
print(isinstance(obj_from_class_2, Second_class)) 
print(isinstance(obj_from_class_2, First_class))
