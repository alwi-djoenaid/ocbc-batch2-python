### File Accessing

# try:
#    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#    print(f.tell())
#    # perform file operations
# finally:
#    f.close()


#################################################################

### Exception

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('windows' in sys.platform), "This code runs on Windows only."

# x = 22
# assert x == 20, 'Different number'

import sys

def os_interaction():
    # assert ('linux' in sys.platform), "This code runs on Linux only."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Do something')

try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed.')


try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
            file.close()
    except FileNotFoundError as error:
        print(error)
        print("Could not open file.log")
        print('file.log is not found in this directory')
finally:
    print('leaning up, irrespective of any exceptions.')