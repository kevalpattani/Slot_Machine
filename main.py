import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winings(columns, Lines, bet, values):
    winings = 0
    wining_lines = []
    for line in range(Lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings += values[symbol] * bet
            wining_lines.append(line + 1)
        return winings, wining_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],"|",end = " ")
            else:
                print(column[row])
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break 
            else:
                print("Please enter a amount greater than 0.")
                continue
        else:
            print('Enter a valid number')
            continue
    return amount 

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            else:
                print("Enter a valid number of lines.")
                continue
        else:
            print('Enter a valid number for lines')
            continue
    return lines 

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount 

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    result_of_spin = print_slot_machine(slots)
    print(result_of_spin)
    winings, wining_lines = check_winings(slots,lines,bet,symbol_value)
    print(f"You Won ${winings}")
    print(f"You won on lines:",*wining_lines)
    return int(winings - total_bet)

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Please enter to spin (q to quit).")
        if answer == 'q':
            break
        balance = balance + spin(balance)
    print(f'you left with ${balance}')

main()
