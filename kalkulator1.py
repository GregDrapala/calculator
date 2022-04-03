import logging
logging.basicConfig(level=logging.DEBUG)
def calculator():
    operation = input('''
Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
''')

    number_1 = float(input('Podaj skladnik 1: '))
    number_2 = float(input('Podaj skladnik 2: '))

    if operation == '1':
        logging.info('Dodaje {} i {}'.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '2':
        logging.info('Odejmuje {} i {}'.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        logging.info('Mnożę {} i {}'.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '4':
        logging.info('Dzielę {} i {}'.format(number_1, number_2))
        print(number_1 / number_2)
 
calculator()
