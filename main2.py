# print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")


# try:
#      print(hello)    
# except NameError as error:
#      print(error)

# print(123)



# try:
#      print(10/0)
#      print(hello)    
# except NameError as error:
#      print(error)
# except ZeroDivisionError as error:
#      print(error)
# else:
#      print('no error')

# print(123)

# def enterYourName(name):
#      if name == '':
#          raise NameError(f'sorry name could not be empty')
#      elif type(name) != str:
#          raise TypeError(f'sorry name could not be number')
#      else:
#           print(name)


# enterYourName('')


def PhoneNumber(phone_number):
    if not phone_number.startswith('+380'):
        raise ValueError("введіть правильний код країни '+380'")
    if len(phone_number) != 13:
        raise ValueError("номер повиннен мати 13 символів, включаючи код країни")
    operator = phone_number[3:6]
    operators = {'096', '050', '068'}
    if operator not in operators:
        raise ValueError("такий оператор не підтримується")
    print("номер телефону:", phone_number)

PhoneNumber('+380960123883')
