# func for result output
def convert_num(base):
    if base == '2':
        return bin(num)[2:]
    elif base == '8':
        return oct(num)[2:]
    elif base == '16':
        return hex(num)[2:]

# func for checking if base input is correct
def if_base_correct(base):
    if base in base_li:
        print(convert_num(base))
    else:
        base = input('Choose the base (2, 8, 16 only): ')
        if_base_correct(base)


# the main program cycle
while True:
    data_type = input('What do you want to convert (n - number, l - list): ')
    if data_type == 'n':
        # enter the number (dec)
        num = int(input('Enter the number (only decimal): '))

        # choose the base (bin, oct, hex)
        base = input('Choose the base (2, 8, 16 only): ')
        base_li = ['2', '8', '16']

        # convert a number
        if_base_correct(base)


    """# convert a list of numbers
    elif data_type == 'l':
        # enter the list (dec)
        li = [int(input()) for i in range(int(input()))]"""
    """# convert a list
    if data_type == 'l':
        res = []
        for i in li:
            if_base_correct(base)"""


    # ask for repeating
    if again := input('Do you want to convert another number? (y / n): ') == 'n':
        print('Goodbye!')
        break



