import os

print(os.getcwd())    # need to "import os" first

my_file = 'pi_digits.txt'

with open(my_file) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


with open(my_file) as file_object:
    for line in file_object:
        print(line, end='')

with open(my_file) as file:
    lines = file.readlines()
print('')
for line in lines:
    print(line)