# plan for erros
try:
    file = open('a_file.txt',mode='r')

    dic= {'key':'number'}

except FileNotFoundError:
    file = open('a_file.txt',mode='r')
    file.write('something')
except KeyError as error_massage:
    print(f'That key Does not exist errort: {error_massage}')
else:
    contents = file.read()
    print(contents)
finally:
    raise KeyError('This is not supose to happend get the cs enginer here now ')

