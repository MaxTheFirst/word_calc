numbers = (1768, 8*10**6, 8*10**(-60), 10/3)


def format_number(number):
    if number > 10**5:
        result = '{:.2}'
    return '{:.0e}'.format(number)


for n in numbers:
    print(format_number(n))
